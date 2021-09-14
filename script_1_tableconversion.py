import pandas as pd
import sys
import csv
#import fimLib as fil # usare l'altra
import functions.microfim as mf
import functions.microdir as md
import numpy as np
import os
import readline


""" This script can be used to convert a otu/esv/taxa table into a list of transactions.
At this stage, do not worry about the format of the input. The script will ask
you which is the separator.

The output will be saved as a list of transactions into input directory.
"""

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



# list files of inputs dir
files = os.listdir(input_dir)
print(files, '\n\n')


# set input dir and autcompletion
os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


# input
input_file = input('Insert otu/taxa table to convert:\n')
print(f'> You entered: {input_file}\n\n')

sep = input('Declare the column separate of your otu table:\n \
E.g. , for commas\n')
print(f'> You entered: {sep}\n\n')


#import as df
df = pd.read_csv(os.path.join(input_dir, input_file), sep=sep, header=0, index_col=None)
print(df)

# sys.exit()

# name
file_name = input_file.split('.')
print(file_name)

# remove space from ID column
df['#ID'] = df['#ID'].str.replace(' ','_')

print(df)

n_cols = df.shape[1] - 1
print(n_cols)
n_rows = df.shape[0] - 1
print(n_rows)


t_list = mf.write_transactions(n_cols, n_rows, df)
print(t_list)

# save as transaction list
with open(input_dir + '/' + 'transactions_' + file_name[0], 'w') as f:
    wr = csv.writer(f)
    wr.writerows(t_list)

# convert commas in spaces (for the next steps)
# remove old output to clean folder
output = 'transactions_' + file_name[0]
print(f'\n\n> Otu table converted!\n \
Now run from your command line in {input_dir}:\n\n \
sed -i -e "s/,/ /g" {output}\n\n \
rm {output}-e\n\n')
