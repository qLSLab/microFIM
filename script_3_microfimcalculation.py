import fim
import pandas as pd
import csv
import os
import sys
from csv import writer
import readline

import functions.microfim as mf
import functions.microdir as md
import functions.microimport as mi


""" This script calculate microbial patterns!
Input files:
- transactionsal data of your otu/esv/taxa table (previously converted with script_2)
- file with parameters in .csv format (support, minimum length and maximum length)
    template available in the tutorial folder

"""


# details about input and output
details = input("Do you want details about input and output files?\n \
Please press Y or N:\n\n")
print(f'> You entered: {details}\n\n')

if details == 'Y':
    print('Input file is a list of transactions, as:\n\n \
    Sample 1    taxa1, taxa2, taxa3\n \
    Sample 2    taxa4, taxa2, taxa5\n \
    Sample 3    taxa2, taxa3, taxa5\n \
    Etc...\n \
    ...\n \
    ...\n\n \
    You can convert your otu/taxa table in a list of transactions using the script\n \
    script_1_tableconversion.py\n\n\n \
    Both input and output files are in CSV format.\n\n')
else:
    pass


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


# import trans file
trans_file = input('Insert your transactional data:\n')
print(f'> You entered: {trans_file}\n\n')


# import files with parameters
par_file = input("Insert your file with fim parameters:\n\n")
print(f'> You entered: {par_file}\n\n')


# import parameters file and transactions
## import transactions
t = mf.read_transaction(os.path.join(data_dir, trans_file))

## import file with paramaters
minsupp, zmin, zmax= mi.itemsets_parameters(data_dir, par_file)


# which target to calculate?
to_calculate = input("What do you want to calculate?\n\n \
Please press one of the following to answer:\n \
i = itemsets\n \
c = closed frequent itemsets\n \
m = maximal frequent itemsets \n\n")
print(f'> You entered: {to_calculate}\n\n')

report= '[asS'

# output file name
output_file = input("Insert your output file name (without extensions):\n\n")
print(f'> You entered: {output_file}\n\n')

# calculate patterns
results = mf.fim_calculation(t, to_calculate, minsupp, zmin, zmax)
print('Patterns extracted')

# write patterns results
file, out_file, new_out_file = mf.write_results(results, data_dir, output_file)


# convert itemsets results into a dataframe
df = mf.itemsets_dataframe(new_out_file)
print(df)

# export as a csv
mf.export_dataframe(df, data_dir, output_file)

print('Results saved as ' + new_out_file + ' in ' + data_dir + '\n\n')
