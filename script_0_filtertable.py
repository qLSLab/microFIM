import os
import pandas as pd
import readline
import functions.microdir as md


""" This script can be used to filter your otu/taxa table based on a list of samples.
Files required and mandatory instructions:
* otu/esv/taxa table - the column name of OTU or TAXA must be '#ID'
* sample list  - the first row of your sample list must be '#SampleID'

The script will ask you to set the input directory and the two files mentioned -
otu/esv/taxa table and sample list. The format of the file does not matter at this stage,
the script will ask you the type of separator.

The output file will be a filtered CSV file saved into the input directory
(in order to allow subsequent analysis).

"""

# set autcompletion
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


# set dirs
data_dir = input('Do you want to change input directory?\nType Y or N: ')
print(f'> You entered: {data_dir}\n\n')

if data_dir == 'Y':
    new_data_dir = input('Which is the new input directory? ')
    input_dir = md.set_inputs_dir(new_data_dir)
    print('New input directory setted!')

else:
    input_dir = md.set_inputs_dir()
    print('Default input directory will be used.')



# list files of inputs dir
files = os.listdir(input_dir)
print('Here is the list of files in the input directory: \n\n')
print(files, '\n\n')


# set input dir and autcompletion
os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")


# filtering options

# import sample list
sample_list = input('Insert list of samples to filter your table:\n')
print(f'> You entered: {sample_list}\n\n')

# import taxa/otu_table
data_table = input('Insert your data table:\n')
print(f'> You entered: {data_table}\n\n')

# sep
sep = input('Declare the column separate of your otu/taxa table:\n \
E.g. , for commas\n')
print(f'> You entered: {sep}\n\n')


# filter oty/taxa table based on sample list
df1 = pd.read_csv(os.path.join(input_dir, sample_list), header=0, index_col=None)
df2 = pd.read_csv(os.path.join(input_dir, data_table), sep=sep, header=0, index_col=None, engine='python')


# convert sample_list into a list
samples = df1['#SampleID'].to_list()

# extract '#ID' column (otu/taxa) - see Docoumentation for details
id = df2[['#ID']]
samples_table = df2[[*samples]]

# concat datasets
new_data = pd.concat([id, samples_table], axis=1)
#print(new_data.info())


# remove rows with zeros
no_zeros = (new_data.iloc[:,1:] != 0).any(axis=1)
new_data = new_data.loc[no_zeros]
#print(new_data.info())


# write file
file_name = input('Insert your output file name (without extensions):\n')
print(f'> You entered: {file_name}\n\n')

new_data.to_csv(os.path.join(input_dir, file_name + '.csv'), index=False)

print('File filtered and saved as ' + file_name + '.csv' + ' in inputs dir!\n\n')
