# Cosmic Neurons (?? TBD :P )

Working directory for aggregating neuron data / developing cosmic web & neuron ML model

## Description

The scripts in the neuron-data folder of the repo are mainly for reference or in case someone needs to fetch more data from http://neuromorpho.org/. Feel free to make additional folders for other parts of the project.

NOTE: The neuron data files (.swc) are not located in this repo.  A zip of all 4041 human neurons can be downloaded at this link: https://drive.google.com/file/d/17n0hL-ECJ_JJNJu30__qOU8FDEC-DbSu/view?usp=sharing

.swc filenames = the name of the neuron

The metadata is located in this repo in the file neuron_metadata.json

### .swc file format
The description below is sourced from this FAQ : http://neuromorpho.org/myfaq.jsp

```
Q:	What is SWC format?
A: 	The three dimensional structure of a neuron can be represented in a SWC format (Cannon et al., 1998). 
SWC is a simple Standardized format. Each line has 7 fields encoding data for a single neuronal compartment:

  * an integer number as compartment identifier
  * type of neuronal compartment
       0 - undefined
       1 - soma
       2 - axon
       3 - basal dendrite
       4 - apical dendrite
  * x coordinate of the compartment
  * y coordinate of the compartment
  * z coordinate of the compartment
  * radius of the compartment
  * parent compartment

Every compartment has only one parent and the parent compartment for the first point in each file is 
always -1 (if the file does not include the soma information then the originating point of the tree will 
be connected to a parent of -1). The index for parent compartments are always less than child compartments. 
Loops and unconnected branches are excluded. All trees should originate from the soma and have parent 
type 1 if the file includes soma information. Soma can be a single point or more than one point. When the 
soma is encoded as one line in the SWC, it is interpreted as a "sphere". When it is encoded by more than 1 line, 
it could be a set of tapering cylinders (as in some pyramidal cells) or even a 2D projected contour ("circumference").
```

## Deployment 

Recommended to run in a virtualenv.   Pip install if you don't have it ;) 


## Contributors

* **Anastasia Victor** - *Initial work* - [Link](https://github.com/avmakesthings)
* **Mark Neyrick**
* **Michael Silver**
* **Miguel Angel Aragon Calvo**
* **Trevor Owens**


## Usful Links

* http://neuromorpho.org/ - Open source neuron data
* https://github.com/mcellteam/swc_mesher - Blender add-on for .swc files

