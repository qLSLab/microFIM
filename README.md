# microFim
### Extending association rule mining to microbiome pattern analysis: tools and guidelines to support real applications
microFim is a Python tool for the integration of Frequent Itemset Mining into microbiome pattern analysis.

## Structure
The tool is written as Python library, download with all its requirements from conda-forge website (link). 
It is built by two main modules, the tool to calculate patterns and rules and the microbiome visualization module.
Each module is available by command-line or interactive dashboard.

## Installation
1. Download Python 3 if you haven’t already at https://www.python.org/
2. Clone github repository (link: https://github.com/qLSLab/microFim.git) and:
    * Download ZIP from microFIM github home page, then decompress it\
    or 
    * Use git from command line: `git clone https://github.com/qLSLab/microFim.git`

3. We suggest to install Conda or Mininconda to run microFIM - here you can find how to install Miniconda3: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

4. Once Miniconda is installed, create the conda environment with the command below, modifying 'myExTaxsIenv' with the name that you prefer: \
`conda create --name microFIM --file requirements.txt`

5. (Optional) Test microFIM before starting with your analysis - see Tutorial section for details

## Usage
* Guided scripts
* Python functions

## Input files format
* #ID
* #SampleID
* .csv/.tsv
