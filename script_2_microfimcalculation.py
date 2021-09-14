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
Files:
- otu/esv/taxa table previously converted in transactions
- file with parameters in .csv format (support, zmin and zmax + type of report)
    template available in the tutorial folder """


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

# set dirs
data_dir = input('Do you want to change input directory?\nType Y or N: ')
print(f'> You entered: {data_dir}\n\n')

if data_dir == 'Y':
    new_data_dir = input('Which is the new input directory?')
    input_dir = md.set_inputs_dir(new_data_dir)
    print('New input directory setted!')

else:
    input_dir = md.set_inputs_dir()
    print('Default input directory will be used.')


# import
# list files of inputs dir
files = os.listdir(input_dir)
print('Here the list of files in your input directory: ', files, '\n\n')

# set input dir and autcompletion
os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


input_file = input("Insert your input file:\n\n")
print(f'> You entered: {input_file}\n\n')

par_file = input("Insert your file with fim parameters:\n\n")
print(f'> You entered: {par_file}\n\n')


# import transactions and file with paramaters
t = mf.read_transaction(os.path.join(input_dir, input_file))
print(t)


# parse parameter file
minsupp, zmin, zmax= mi.itemsets_parameters(input_dir, par_file)
print(minsupp, zmin, zmax)


# which target to calculate?
to_calculate = input("What do you want to calculate?\n\n \
Please press one of the following to answer:\n \
i = itemsets\n \
c = closed frequent itemsets\n \
m = maximal frequent itemsets \n\n")
print(f'> You entered: {to_calculate}\n\n')

report= '[asS'


# run eclat
if to_calculate == 'i':
    results = fim.eclat(t, target='s', supp=minsupp, zmin=zmin, report=report)
elif to_calculate == 'c':
    results = fim.eclat(t, target='c', supp=minsupp, zmin=zmin, report=report)
elif to_calculate == 'm':
    results = fim.eclat(t, target='m', supp=minsupp, zmin=zmin, report=report)

print(results)


#sys.exit()



# output file name
output_file = input("Insert your output file name (without extensions):\n\n")
print(f'> You entered: {output_file}\n\n')


# set output dir
output_dir = input('Do you want to change output directory?\nType Y or N: ')
print(f'> You entered: {output_dir}\n\n')

if output_dir == 'Y':

    # set autcompletion
    os.chdir("..")
    readline.set_completer_delims(' \t\n=')
    readline.parse_and_bind("tab: complete")

    # new
    new_out_dir = input('Which is the new input directory?')
    out_dir = md.set_outputs_dir(new_out_dir)
    print('New output directory setted!')

else:
    out_dir = md.set_outputs_dir()
    print('Default output directory will be used.')


# opening the csv file in 'w+' mode 3022021
# crea funzione qui x cleaning
file = open(out_dir + '/' + output_file + '.csv', 'w+', newline ='')
# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(results)


out_file = out_dir + '/' + output_file + '.csv'
new_out_file = out_dir + '/df_' + output_file + '.csv'
with open(out_file, 'r') as f, open(new_out_file, 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", "").replace('),[', ')/[').replace(')', '').replace('(', '').replace('[', '').replace(']', ''))



## convert itemsets results into a dataframe
df = mf.itemsets_dataframe(new_out_file)
df.to_csv(new_out_file, index=False)

print('Results saved!')


## remove the second output
