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
to filter results. In particular:
- allConfidence (ref)
- crossSupport (ref) """


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

files = os.listdir(input_dir)

output_dir = input('Do you want to change output directory?\nType Y or N: ')
print(f'> You entered: {output_dir}\n\n')

if output_dir == 'Y':
    new_out_dir = input('Which is the new input directory?')
    out_dir = md.set_outputs_dir(new_out_dir)
    print('New output directory setted!')

else:
    out_dir = md.set_outputs_dir()
    print('Default output directory will be used.')


print(os.listdir(input_dir))

# set input dir and autcompletion
os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


print(os.listdir(out_dir))

input_file = input("Insert your itemset file:\n\n")
print(f'> You entered: {input_file}\n\n')

otu_table = input("Insert your taxa table file:\n\n")
print(f'> You entered: {otu_table}\n\n')

trans_file = input("Insert your transactional file:\n\n")
print(f'> You entered: {trans_file}\n\n')

# input_file = 'df_tutorial_DWTP_classic_itemsets.csv'
# trans_file = 'tutorial_DWTP_taxa_table_transactions'
# otu_table = 'tutorial_DWTP_taxa_table.csv'

df = pd.read_csv(os.path.join(out_dir, input_file), header=0, index_col=None)
print(df)
n_patterns = df.shape[0]

#
df_otu = pd.read_csv(os.path.join(input_dir, otu_table), header=0, index_col=None)

# convert to a list
list_of_string = df_otu['#ID'].tolist()
print(list_of_string)
for i in list_of_string:
    i = i.lower()

#print(list_of_string)


# calculate ids frequency and create a dict
#frequency = mim.calculate_ids_frequency(input_dir, trans_file)
#print(frequency)

# calculate occurrences for each id
frequency = mim.calculate_ids_occurrence(df_otu)
print(frequency)



#sys.exit()

# calculate len of trans_file
lines_in_file = open(os.path.join(input_dir, trans_file), 'r').readlines()
#print(lines_in_file)
number_of_lines = float(len(lines_in_file))

#print(number_of_lines)


###

data_allc_update = mim.all_confidence(df, frequency, number_of_lines)
#print(data_allc_update)

#sys.exit()

data_crosssupp_update = mim.cross_support(df, frequency, number_of_lines)
#print(data_crosssupp_update)

# write file
file_name = input('Insert your output file name (without extensions):\n')
print(f'> You entered: {file_name}\n\n')

#data_crosssupp_update.to_csv('df_tutorial_DWTP_closed_addm_itemsets.csv')
#data_crosssupp_update.to_csv(os.path.join(out_dir, 'df_tutorial_DWTP_classic_addm_itemsets.csv'))
data_crosssupp_update.to_csv(os.path.join(out_dir, file_name + '.csv'), index=False)
