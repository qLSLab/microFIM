import pandas as pd
import os
import sys
import numpy as np
import re
import string
import readline

import functions.microfim as mf
import functions.microdir as md
import functions.microinterestmeasures as mim
import functions.microimport as mi


""" This script calculate additional interest measures that can be used
to filter results.
In particular:
- allConfidence (Ref: https://michael.hahsler.net/research/association_rules/measures.html#all-confidence)

Input file:
- pattern dataframe;
- transactional file.

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


## import trans file
trans_file = input('Insert your transactional data:\n')
print(f'> You entered: {trans_file}\n\n')

# import data table (esv/otu/taxa)
data_table = input('Insert your data table:\n')
print(f'> You entered: {data_table}\n\n')

data_sep = input('Declare the column separate of your otu/taxa/esv table:\n \
E.g. , for commas\n')
print(f'> You entered: {data_sep}\n\n')


data_table = mi.import_data_table(data_table, data_dir, data_sep)


# import pattern dataframe
pattern_df = input('Insert your dataframe with patterns:\n')
print(f'> You entered: {pattern_df}\n\n')

## import patterns dataframe
df = mi.import_pattern_dataframe_rev(data_dir, pattern_df)


# CALCULATE ADDITIONAL METRICS
# calculate and add all-confidence values
data_allc_update = mim.add_interest_measures(data_table, df, trans_file, data_dir)

# set output file name
add_interest_file = input('Insert your output file name (without extensions):\n')
print(f'> You entered: {add_interest_file}\n\n')

# export dataframe
mim.add_table_export(data_allc_update, data_dir, add_interest_file)
print('Results saved as df_' + add_interest_file + '.csv in ' + data_dir + '\n\n')
