import pandas as pd
import plotly.express as px
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import readline

import functions.microfim as mf
import functions.microdir as md
import functions.microinterestmeasures as mim
import functions.microimport as mi

import plotly.graph_objects as go
from plotly.subplots import make_subplots


""" This script produce plotly figures to represent pattern distribution and
general statistics (TO DO) - removing '#' from .show() command you can directly
interacts with the plots """


##### COMMENTS FOR DEF VALUES #####

# # set autcompletion
# readline.set_completer_delims(' \t\n=')
# readline.parse_and_bind("tab: complete")
#
# # set dirs
# data_dir = input("Do you want to change input directory?\nType Y or N: ")
# print(f'> You entered: {data_dir}\n\n')
#
# if data_dir == 'Y':
#     new_data_dir = input("Which is the new input directory?")
#     input_dir = md.set_inputs_dir(new_data_dir)
#     print('New input directory setted!')
#
# else:
#     input_dir = md.set_inputs_dir()
#     print('Default input directory will be used.')
#
#
# out_dir = input("Do you want to change output directory?\nType Y or N: ")
# print(f'> You entered: {out_dir}\n\n')
#
# if out_dir == 'Y':
#     new_out_dir = input("Which is the new input directory?")
#     out_dir = md.set_inputs_dir(new_out_dir)
#     print('New output directory setted!')
#
# else:
#     out_dir = md.set_outputs_dir()
#     print('Default input directory will be used.')
#
#
# # imports data to creata taxa table
# print(os.listdir(input_dir), '\n')


##### FINO A QUI #####

input_dir = '/Users/j/Documents/PHD/MICROFIM/microFim_dev/ecam_outputs/'
#out_dir = '/Users/j/Documents/PHD/MICROFIM/microFim_dev/test2/'

os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

print(os.listdir(input_dir), '\n')

# pattern input
pattern_input = 'pattern_table_test_complete.csv'
# pattern_input = input("Insert your pattern file:\n\n")
# print(f'> You entered: {pattern_input}\n\n')

# metadata file
#meta_input = 'metadata_test2.csv'
# meta_input = input("Insert your metadata file:\n\n")
# print(f'> You entered: {meta_input}\n\n')


# df import
df_pattern = pd.read_csv(os.path.join(input_dir, pattern_input), header=0, index_col=None)

df_pattern = df_pattern.drop(['Support(%)'], axis=1)

print(df_pattern)
print(df_pattern.columns)

# df_metadata = pd.read_csv(os.path.join(input_dir, meta_input), header=0, index_col=None)
# print(df_metadata)
# print(df_metadata.columns)


# figure 1 = hist_counts
#hist = make_subplots(rows=1, cols=2)
data_hist1 = df_pattern.groupby(['Pattern length']).size().reset_index(name='Counts')
print(data_hist1.head())
data_hist2 = df_pattern.groupby(['Support']).size().reset_index(name='Counts')
print(data_hist2.head())


hist1 = px.bar(data_hist1, x='Pattern length', y='Counts', height=400, width=800,
              color='Pattern length', title='Pattern length distribution')
hist2 = px.bar(data_hist2, x='Support', y='Counts', height=400, width=800, color='Support',
              title='Pattern support distribution')

#hist1.show()
#hist2.show()

#sys.exit()


# figure 2 = scatter2d
data_2dscatter_1 = df_pattern.groupby(['Support', 'Pattern length']).size().reset_index(name='Counts')

data_2dscatter_2 = df_pattern.groupby(['All-confidence', 'Pattern length']).size().reset_index(name='Counts')

data_2dscatter_3 = df_pattern.groupby(['Cross-support', 'Pattern length']).size().reset_index(name='Counts')

scatter_2d_1 = px.scatter(data_2dscatter_1, x="Pattern length", y="Counts", color="Support")
scatter_2d_1.update_traces(marker=dict(size=data_2dscatter_1['Pattern length']*5))
#scatter_2d_1.show()

scatter_2d_2 = px.scatter(data_2dscatter_2, x="Pattern length", y="Counts", color="All-confidence")
scatter_2d_2.update_traces(marker=dict(size=data_2dscatter_2['Pattern length']*5))
#scatter_2d_2.show()

scatter_2d_3 = px.scatter(data_2dscatter_3, x="Pattern length", y="Counts", color="Cross-support")
scatter_2d_3.update_traces(marker=dict(size=data_2dscatter_3['Pattern length']*5))
#scatter_2d_3.show()





# figure 3 = scatter3d
data_3dscatter_1 = df_pattern.groupby(['Support', 'Pattern length','All-confidence']).size().reset_index(name='Counts')
print(data_3dscatter_1.head())
data_3dscatter_2 = df_pattern.groupby(['Support', 'Pattern length','Cross-support']).size().reset_index(name='Counts')
print(data_3dscatter_2.head())

scatter3d_1 = px.scatter_3d(data_3dscatter_1, x='Counts', y='Support', z='All-confidence',
              color='Pattern length')
scatter3d_2 = px.scatter_3d(data_3dscatter_2, x='Counts', y='Support', z='Cross-support',
              color='Pattern length')

#scatter3d_1.show()
#scatter3d_1.write_image(os.path.join(input_dir, 'scatter3d_prova.svg'))
#scatter3d_1.write_html(os.path.join(input_dir, 'scatter3d_prova.html'))

#scatter3d_2.show()



# figure 4
# number per samples


sys.exit()
