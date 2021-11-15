import os
import sys
import pandas as pd
import numpy as np
import csv
from csv import writer
import readline
import re
import string

import fim
import functions.microdir as md
import functions.microfim as mf
import functions.microimport as mi
import functions.microinterestmeasures as mim


""" microFIM example code on test/test2.csv files
of microFIM github repository
Input files to run microFIM:
- test2.csv
- transactional file 2 (can be obtained with microFIM_example_code_1.py)
- metadata_test2.csv
- parameters_test2.csv

Default is itemsets patterns (i), but also closed (c) and maximal (m) can be calculated.

Finally, two pattern tables can be generated:
- complete pattern table (patterns + interest measures)
- clean pattern table

"""

# set fim options
to_calculate = 'i' # default (can be changed in c or m)

# setting files
## dir
set_dir = 'test'

## metadata
metadata = 'metadata_test2.csv'
meta_sep = ','

## otu/esv/taxa table
data_table_name = 'test2.csv'
data_sep = ','

## parameter file
par_file = 'parameters_test2.csv'

# transactional file
trans_file = 'transactions_test2'

# set output name
output_file = 'patterns_test2'
add_interest_file = 'addm_patterns_test2'
output_pattern_table = 'pattern_table_test2'


# SETTINGS
## set dir
data_dir = md.set_inputs_dir_rev(set_dir)

## SET OUTPUT NAME
file_name = mi.output_file_name(data_table_name)


# import files

# IMPORT FILES
## import metadata
metadata = mi.import_metadata(metadata, data_dir, meta_sep)

## import data table (otu, esv or taxa table)
data_table = mi.import_data_table(data_table_name, data_dir, data_sep)

# import parameters file

## import transactions
t = mf.read_transaction(os.path.join(data_dir, trans_file))

## import file with paramaters
minsupp, zmin, zmax= mi.itemsets_parameters(data_dir, par_file)


# FILTER DATA TABLE VIA SAMPLE METADATA
filter_table = mf.filter_data_table(metadata, data_table)

# calculate patterns
results = mf.fim_calculation(t, to_calculate, minsupp, zmin, zmax)

# write patterns results
file, out_file, new_out_file = mf.write_results(results, data_dir, output_file)

# convert itemsets results into a dataframe
df = mf.itemsets_dataframe(new_out_file)
print(df)

# export as a csv
mf.export_dataframe(df, data_dir, output_file)

print('Results saved as ' + new_out_file + ' in ' + data_dir + '\n\n')



# CALCULATE ADDITIONAL METRICS
## import patterns dataframe
df = mi.import_pattern_dataframe(data_dir, output_file)

# calculate and add all-confidence values
data_allc_update = mim.add_interest_measures(data_table, df, trans_file, data_dir)

# export dataframe
mim.add_table_export(data_allc_update, data_dir, add_interest_file)
print('Results saved as df_' + add_interest_file + '.csv in ' + data_dir + '\n\n')



# GENERATE PATTERN TABLE
## generate pattern table with patterns and interest measures
pattern_table_complete = mf.generate_pattern_table(data_allc_update, df, data_dir, trans_file, metadata, meta_sep)
print(pattern_table_complete)

## export pattern table as cv
mf.export_pattern_tables(pattern_table_complete, data_dir, output_pattern_table)
