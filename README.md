# microFIM

![alt text](microFIM_framework.jpg)

## Overview
microFim (microbial Frequent Itemset Mining) is a Python tool for the integration of Frequent Itemset Mining approach (also known as Association Rule Mining - ARM) into microbiome pattern analysis.
The tool is developed to create a bridge between microbial ecology researchers and ARM technique, integrating the common microbiome outputs (in particular, OTU and taxa table), metadata files typically used in microbiome analysis, and it provides similar microbiome outputs that help scientists to integrate ARM in microbiome applications. In detail, microFIM generates the **pattern table** - an OTU table built with the patterns extracted via ARM (see Figure above as an example)- that can be used to further statistical analysis, as biodiversity analysis based on distance metrics, and microbiome visualization strategies - as pattern-based heatmaps.

Below, installation, instructions of use and tutorials are provided.

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
Below, recomendations about input files format and explanation about the structure and functions module available.

### Input/output files format
Before starting, be sure to set the following requirements:
* #ID \
In the taxa table, the column describing taxa must be filled as #ID. You can rename it with `sed -i 's/SEARCH_REGEX/REPLACEMENT/g' INPUTFILE` \
or a text editor;
* #SampleID \
If you want to filter your taxa table with a list of samples or metadata file, the column name must be filled as #SampleID; 
* CSV format \
Taxa table, metadata file and sample list file must be provided as CSV files. Template file is already defined as CSV in [input_templates](input_templates) directory.

### Structure
Guided scripts are defined in **6 main phases**, also represented in [microFIM_framework](microFIM_framework.jpg) figure.
In addition, we provided python function modules that follow the previous structure. Here we describe the main steps and their respectives modules.
In particular:
* Step 1: microbiome data as taxa table importing and filtering;
* Step 2: conversion into a transactional dataset;
* Step 3: pattern calculation via a template file to be filled;
* Step 4: calculation of additional interest measures;
* Step 5: creation of the pattern table;
* Step 6: visualization of results.

## Cite us
Link
