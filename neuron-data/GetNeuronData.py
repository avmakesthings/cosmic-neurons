try:
  from urllib2 import urlopen, Request
except ImportError:
  from urllib.request import urlopen, Request

import re
import json
import base64
import os.path


# "constants"
NEUROMORPHO_URL = "http://neuromorpho.org"
NEURON_QUERY_URL = "http://neuromorpho.org/api/neuron/select?q=species:human&page={}&size={}&sort=neuron_id"
MAX_NEURONS_PER_PAGE = 500
NEURON_METADATA_FILENAME = "neuron_metadata.json"

def load_from_json(file_name):
    with open(file_name, 'r') as infile:  
        return json.loads(infile.read())

def write_json_file(file_name, results):
    with open(file_name, 'w') as outfile:  
      json.dump(results, outfile, indent=4, sort_keys=True )

def get_all_neurons_of_species():
    more_to_load = True
    results = []
    current_page_num = 0
    while more_to_load:
        url = NEURON_QUERY_URL.format(current_page_num, MAX_NEURONS_PER_PAGE)
        response = json.loads(urlopen(url).read())
        for n in response["_embedded"]["neuronResources"]:
            results.append(n)

        more_to_load = response["page"]["number"] != response["page"]["totalPages"]-1
        current_page_num = response["page"]["number"]+1

    write_json_file(NEURON_METADATA_FILENAME, results)

    return results

#function based on https://github.com/NeuroBox3D/neuromorpho
def get_swc_by_neuron_name(neuronName):
  url = "%s/neuron_info.jsp?neuron_name=%s" % (NEUROMORPHO_URL, neuronName)
  html = urlopen(url).read()
  p = re.compile(r'<a href=dableFiles/(.*)>Morphology File \(Standardized\)</a>', re.MULTILINE)
  m = re.findall(p, html)
  swc_file_names = []
  for match in m:
     fileName = "./swc/"+match.replace("%20", " ").split("/")[-1]
     swc_file_names.append(fileName)
     print(urlopen("%s/dableFiles/%s" % (NEUROMORPHO_URL, match)).getcode())
    #  response = urlopen("%s/dableFiles/%s" % (NEUROMORPHO_URL, match)).getcode()

    #  open(fileName, 'w').write(response.read())
  return swc_file_names


def get_complete_neuron_data(neuron_data):
    for n in neuron_data:

      if not "measurements" in n:
        print("Fetching measurements for {}".format(n["neuron_name"]))
        url = n["_links"]["measurements"]["href"]
        response = json.loads(urlopen(url).read())
        n["measurements"] = response
      
      # swc_file_name = "{}.swc".format(n["neuron_name"])
      if not "swc_files" in n:
        print("Fetching SWC file for {}".format(n["neuron_name"]))
        swc_file_names = get_swc_by_neuron_name(n["neuron_name"])
        n["swc_files"] = swc_file_names

      write_json_file(NEURON_METADATA_FILENAME, neuron_data)

# data = get_all_neurons_of_species()
neuron_data = load_from_json(NEURON_METADATA_FILENAME)
get_complete_neuron_data(neuron_data)
