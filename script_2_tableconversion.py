import pandas as pd
import sys
import csv
import numpy as np
import os
import readline
import functions.microfim as mf
import functions.microdir as md
import functions.microimport as mi


""" This script can be used to convert a otu/esv/taxa table into a list of transactions.
At this stage, do not worry about the format of the input. The script will ask
you which is the separator.

The output will be saved as a list of transactions into input directory.

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


# import taxa/otu/esv table
data_table = input('Insert your data table:\n')
print(f'> You entered: {data_table}\n\n')


# sep
data_sep = input('Declare the column separate of your otu/taxa/esv table:\n \
E.g. , for commas\n')
print(f'> You entered: {data_sep}\n\n')

# SET OUTPUT NAME
file_name = mi.output_file_name(data_table)


# import files
## import data table (otu, esv or taxa table)
data_table = mi.import_data_table(data_table, data_dir, data_sep)
print(data_table)

# CONVERT DATA TABLE IN TRANSACTIONAL data

t_list = mf.convert_in_transaction_list(data_table, data_table)
print(t_list)


# save file
mf.save_transaction_list(data_dir, t_list, file_name)


# convert commas in spaces (for the next steps)
# remove old output to clean folder
output = 'transactions_' + file_name[0]
print(f'\n\n> Otu table converted!\n \
Now run from your command line in {data_dir}:\n\n \
sed -i -e "s/,/ /g" {output}\n\n \
rm {output}-e # if necessary\n\n')
