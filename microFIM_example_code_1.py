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


""" microFIM example code on test/test1.csv files
of microFIM github repository
Input files to run microFIM:
- test2.csv
- metadata_test2.csv
- parameters_test2.csv

"""

# setting files
## dir
set_dir = 'test'

## metadata
metadata = 'metadata_test2.csv'
meta_sep = ','

## otu/esv/taxa table
data_table_name = 'test2.csv'
data_sep = ','

# SETTINGS
## set dir
data_dir = md.set_inputs_dir_rev(set_dir)
print(data_dir)

## SET OUTPUT NAME
file_name = mi.output_file_name(data_table_name)

# IMPORT FILES
## import metadata
metadata = mi.import_metadata(metadata, data_dir, meta_sep)
print(metadata)

## import data table (otu, esv or taxa table)
data_table = mi.import_data_table(data_table_name, data_dir, data_sep)
print(data_table)


# FILTER DATA TABLE VIA SAMPLE METADATA
filter_table = mf.filter_data_table(metadata, data_table)
print(filter_table)


# CONVERT DATA TABLE IN TRANSACTIONAL data

t_list = mf.convert_in_transaction_list(filter_table, data_table_name)
print(t_list)

# save file
mf.save_transaction_list(data_dir, t_list, file_name)


# TO BE PRINT WHEN RUNNING THIS SCRIPT
# remove old output to clean folder
output = 'transactions_' + file_name[0]

print(f'\n\n> File converted and saved as ' + output + '.csv' + ' in ' + data_dir + '\n\n')

print(f'\n\n> Now run from your command line in {data_dir}:\n\n \
sed -i -e "s/,/ /g" {output}\n\n \
rm {output}-e\n\n')
