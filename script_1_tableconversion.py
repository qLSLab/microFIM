import pandas as pd
import sys
import csv
#import fimLib as fil # usare l'altra
import functions.microfim as mf
import functions.microdir as md
import numpy as np
import os

""" This script can be used to convert a otu/taxa table into a list of transactions.
At this stage, do not worry about the format of the input. The script will ask
you which is the separator.

The output will be saved as a list of transactions into input directory.
"""


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


# input
input_file = input('Insert otu/taxa table to convert:\n')
print(f'> You entered: {input_file}\n\n')

# sep = input('Declare the column separate of your otu table:\n \
# E.g. , for commas\n')
# print(f'> You entered: {sep}\n\n')



df = pd.read_csv(os.path.join(input_dir, input_file),  header=0, index_col=None)



# name
file_name = input_file.split('.')
print(file_name)


n_cols = df.shape[1] - 1
print(n_cols)
n_rows = df.shape[0] - 1
print(n_rows)


t_list = mf.write_transactions(n_cols, n_rows, df)
# per ogni colonna, se a quella riga x > 0 prendi il nome della riga e aggiungilo alla lista della colonna
# t_list = []
#
# # trasformare in funzione?
# for c in np.arange(1, n_cols+1):
#     list = []
#     for r in np.arange(0, n_rows+1):
#         #print(df.iloc[r,c])
#         if df.iloc[r,c] > 0:
#             item = df.iloc[r,0]
#             #print(item)
#             list.append(item)
#         else:
#             pass
#
#     t_list.append(list)

print(t_list)

# save as transaction list
with open(input_dir + '/' + file_name[0] + '_transactions', 'w') as f:
    wr = csv.writer(f)
    wr.writerows(t_list)

output = file_name[0] + '_transactions'
print(f'\n\n> Otu table converted!\n \
Now run from your command line in {input_dir}:\n\n \
sed -i -e "s/,/ /g" {output}\n\n \
rm {output}-e\n\n')


# questi ultimi due comandi vanno fatti girare dentro lo script! #
