# microFIM

![alt text](microFIM_framework.jpg)

## Overview
microFim is a Python tool for the integration of Frequent Itemset Mining into microbiome pattern analysis.
(tbd)

## Installation
1. Download Python 3 if you haven’t already at https://www.python.org/
2. Clone github repository (link: https://github.com/qLSLab/microFim.git) and:
    * Download ZIP from microFIM github home page, then decompress it\
    or 
    * Use git from command line: `git clone https://github.com/qLSLab/microFim.git`

3. We suggest to install Conda or Mininconda to run microFIM - here you can find how to install Miniconda3: https://conda.io/projects/conda/en/latest/user-guide/install/index.html

4. Once Miniconda is installed, create the conda environment with the command below: \
`conda create --name microFIM --file requirements.txt --channel default --channel conda-forge --channel plotly`

5. (Optional) Test microFIM before starting with your analysis - see Tutorial section for details

## Usage
microFIM can be used via guided scripts or python functions. \
Please see [microfim_tutorial_notebook](microfim_tutorial_notebook.ipynb) for complete tutorials for both usage.

### Input/output files format
Before starting, be sure to set the following requirements:
* #ID \
In the taxa table, the column describing taxa must be filled as #ID. You can rename it with `sed -i 's/SEARCH_REGEX/REPLACEMENT/g' INPUTFILE` \
or a text editor
* #SampleID \
If you want to filter your taxa table with a list of samples or metadata file, the column name must be filled as #SampleID 
* CSV/TSV format \
Taxa table, metadata file and sample list file must be provided as CSV or TSV. Template file is already defined as CSV in input_templates directory on this Github repository.

### Structure
* Step 1: microbiome data as taxa table importing and filtering;
* Step 2: conversion into a transactional dataset;
* Step 3: pattern calculation via a template file to be filled;
* Step 4: calculation of additional interest measures;
* Step 5: creation of the pattern table;
* Step 6: visualization of results.

## Cite us
Link
