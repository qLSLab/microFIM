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
import functions.microplots as mp

import plotly.graph_objects as go
from plotly.subplots import make_subplots


""" This script produce plotly heatmap based on Jaccard distance matrix.
Inputs:
- pattern table
- metadata
- plot_name
- output_format
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



# IMPORT pattern table
pattern_input = input("Insert your pattern table file:\n\n")
print(f'> You entered: {pattern_input}\n\n')

df_pattern = mi.import_pattern_dataframe_plot(data_dir, pattern_input)
print(df_pattern)

# metadata file
meta_input = input("Insert your metadata file:\n\n")
print(f'> You entered: {meta_input}\n\n')
meta_sep = input('Declare the column separate of your metadata file:\n \
E.g. , for commas\n')
print(f'> You entered: {meta_sep}\n\n')


metadata = mi.import_metadata(meta_input, data_dir, meta_sep)
print(metadata)

# output name
plot_name = input("Insert the name of your output file (will be used for all the plots):\n\n")
print(f'> You entered: {plot_name}\n\n')

## save format
output_format = input('Declare the format for your plots:\n \
E.g. SVG or HTML\n')
print(f'> You entered: {output_format}\n\n')


#create distance matrix
dis_matrix = mp.calculate_distance_matrix(df_pattern, metadata)

mp.plot_heatmap(dis_matrix, metadata, data_dir, plot_name, output_format)
print('Heatmap saved in ' + output_format + ' as ' plot_name + '_heatmap in ' + data_dir + '\n\n')



sys.exit()

set_col = mp.set_col_name(plot_name)

# set columns for plotting
cols = ['Pattern length', 'Support', 'All-confidence']

# PLOTTING SCATTER 2D
col_to_group = 'Support'
col_to_group1 = 'Support'
col_to_group2 = 'Pattern length'

# PLOTTING HIST
hist = mp.hist_plot(df_pattern, col_to_group)
# # save as SVG and HTML
mp.save_hist_plot(outputdir, plot, plot_name, format, set_col)


# PLOTTING SCATTER 2D
scatter_2d = mp.scatter_plot_2d(df_pattern, col_to_group1, col_to_group2)
mp.save_scatter_2d_plot(data_dir, plot, plot_name, format)


# PLOTTING SCATTER 3D
col_to_group1 = 'Support'
col_to_group2 = 'Pattern length'
col_to_group3 = 'All-confidence'
scatter_3d = mp.scatter_plot_3d(df_pattern, col_to_group1, col_to_group2, col_to_group3)
mp.save_scatter_2d_plot(data_dir, plot, plot_name, format)
