import pandas as pd
import os
import sys
import readline

import functions.microfim as mf
import functions.microdir as md
import functions.microinterestmeasures as mim
import functions.microimport as mi


""" This script can be used to create the pattern table.
Inputs:
- pattern results;
- metadata file;
- transactional file.

The output will be saved as a CSV dataframe (with and without
inrerest measures) into input directory.
"""

# set autcompletion
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

# set dir
data_dir = input('Set your project directory:\n')
print(f'> You entered: {data_dir}\n\n')

data_dir = md.set_inputs_dir_rev(data_dir)
print('Project directory:', '\n\n', data_dir)
print('\n\n')

# list files of inputs dir
files = os.listdir(data_dir)
print('Here is the list of files in the project directory: \n')
print(files, '\n\n')

# set input dir and autcompletion
os.chdir(data_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


# IMPORT
# import pattern dataframe
itemset_input = input('Insert your dataframe with patterns:\n')
print(f'> You entered: {itemset_input}\n\n')

## import patterns dataframe
itemset_input = mi.import_pattern_dataframe_rev(data_dir, itemset_input)

## import trans file
trans_file = input('Insert your transactional data:\n')
print(f'> You entered: {trans_file}\n\n')

# import metadata
metadata = input('Insert your metadata file:\n')
print(f'> You entered: {metadata}\n\n')

# sep
meta_sep = input('Declare the column separate of your metadata file:\n \
E.g. , for commas\n')
print(f'> You entered: {meta_sep}\n\n')

metadata = mi.import_metadata(metadata, data_dir, meta_sep)
print(metadata)


# GENERATE PATTERN TABLE
## generate pattern table with patterns and interest measures
pattern_table_complete = mf.generate_pattern_table(itemset_input, itemset_input, data_dir, trans_file, metadata, meta_sep)
print(pattern_table_complete)

# output file name
output_pattern_table = input("Insert your output file name (without extensions):\n\n")
print(f'> You entered: {output_pattern_table}\n\n')

## export pattern table as cv
mf.export_pattern_tables(pattern_table_complete, data_dir, output_pattern_table)
