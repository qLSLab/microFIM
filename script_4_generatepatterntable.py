import pandas as pd
import os
import sys

import functions.microfim as mf
import functions.microdir as md
import functions.microinterestmeasures as mim
import functions.microimport as mi

import readline

# set autcompletion
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

# set dirs
data_dir = input("Do you want to change input directory?\nType Y or N: ")
print(f'> You entered: {data_dir}\n\n')

if data_dir == 'Y':
    new_data_dir = input("Which is the new input directory?")
    input_dir = md.set_inputs_dir(new_data_dir)
    print('New input directory setted!')

else:
    input_dir = md.set_inputs_dir()
    print('Default input directory will be used.')


out_dir = input("Do you want to change output directory?\nType Y or N: ")
print(f'> You entered: {out_dir}\n\n')

if out_dir == 'Y':
    new_out_dir = input("Which is the new input directory?")
    out_dir = md.set_inputs_dir(new_out_dir)
    print('New output directory setted!')

else:
    out_dir = md.set_outputs_dir()
    print('Default input directory will be used.')


# imports data to creata taxa table
print(os.listdir(input_dir), '\n')
print(os.listdir(out_dir))
# itemset input 0

itemset_input = input("Insert your itemset file:\n\n")
print(f'> You entered: {itemset_input}\n\n')

# otu table input 1
trans_input = input("Insert your transactional file:\n\n")
print(f'> You entered: {trans_input}\n\n')

# metrics input 2
metadata_input = input("Insert your metadata file:\n\n")
print(f'> You entered: {metadata_input}\n\n')

# for metadata
sep = input('Declare the column separate of your metadata file:\n \
E.g. , for commas\n')
print(f'> You entered: {sep}\n\n')

# itemset_input = 'df_DWTP_aquifer_maximal.csv'
# trans_input = 'DWTP_genus_aquifer_transactions'
# metadata_input = 'DWTP_metadata_aquifer.csv'

# DWTP_genus_aquifer.csv
# DWTP_genus_aquifer_transactions
# df_DWTP_aquifer_maximal.csv

df = pd.read_csv(os.path.join(out_dir, itemset_input), header=0, index_col=None)
print(df, '\n')

#sys.exit()

col_patterns = mf.set_patterns_for_matching(df)
#print(col_patterns)

print('\n')

#sys.exit()

transactional_list = mf.set_transdata_for_matching(input_dir, trans_input)
#print(transactional_list)

#sys.exit()

pattern_table = mf.generate_pattern_occurrences(input_dir, col_patterns, transactional_list, metadata_input, sep)
#print(pattern_table)

df_pattern_table = mf.concat_tables(df, pattern_table)
print(df_pattern_table)

# only 0 and 1
df_pattern_table_clean = df_pattern_table.drop(['Samples', 'Support', 'Support(%)', 'Pattern length', 'All-confidence', 'Cross-support'], axis=1)

#sys.exit()

# save
output_file = input("Insert your output file name (without extensions):\n\n")
print(f'> You entered: {output_file}\n\n')

df_pattern_table.to_csv(os.path.join(out_dir, output_file + '_complete.csv'), index=False)
df_pattern_table_clean.to_csv(os.path.join(out_dir, output_file + '.csv'), index=False)
