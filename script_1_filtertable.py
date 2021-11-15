import os
import pandas as pd
import readline
import sys
import functions.microdir as md
import functions.microimport as mi
import functions.microfim as mf


""" This script can be used to filter your otu/taxa/esv table based on a list of samples
(metadata file including only the samples you want to analyse).
Files required and mandatory instructions:
* otu/esv/taxa table - the column name of OTU or TAXA must be '#ID'
* sample list  - the first row of your sample list must be '#SampleID'

The script will ask you to set the input directory and the two files mentioned -
otu/esv/taxa table and sample list. The format of the file does not matter at this stage,
the script will ask you the type of separator.

The output file will be a filtered CSV file saved into the input directory.

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



# filtering options

# import sample list
metadata = input('Insert the list of samples to filter your table (use also metadata file):\n')
print(f'> You entered: {metadata}\n\n')

# sep
meta_sep = input('Declare the column separate of your metadata file:\n \
E.g. , for commas\n')
print(f'> You entered: {meta_sep}\n\n')


# import taxa/otu_table
data_table = input('Insert your data table:\n')
print(f'> You entered: {data_table}\n\n')

# sep
data_sep = input('Declare the column separate of your otu/taxa/esv table:\n \
E.g. , for commas\n')
print(f'> You entered: {data_sep}\n\n')


# IMPORT FILES
## import metadata
metadata = mi.import_metadata(metadata, data_dir, meta_sep)
print(metadata)

## import data table (otu, esv or taxa table)
data_table = mi.import_data_table(data_table, data_dir, data_sep)
print(data_table)


# FILTER DATA TABLE VIA SAMPLE METADATA
filter_table = mf.filter_data_table(metadata, data_table)
print(filter_table)


# write file
file_name = input('Insert your output file name (without extensions):\n')
print(f'> You entered: {file_name}\n\n')

# save as csv
filter_table.to_csv(os.path.join(data_dir, file_name + '.csv'), index=False)

print('File filtered and saved as ' + file_name + '.csv' + ' in inputs dir!\n\n')
