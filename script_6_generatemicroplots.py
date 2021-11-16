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


""" This script produce plotly figures to represent pattern distribution and
general statistics (TO DO) - removing '#' from .show() command you can directly
interacts with the plots """


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


# create distance matrix
dis_matrix = mp.calculate_distance_matrix(df_pattern, metadata)

mp.plot_heatmap(dis_matrix, metadata, data_dir, plot_name, output_format)
print('Heatmap saved in ' + output_format + ' as ' plot_name + '_heatmap in ' + data_dir + '\n\n')

sys.exit()

# set columns for plotting
col_to_group = ['Pattern length', 'Support', 'All-confidence']



# set names
set_col = mp.set_col_name(plot_name)


# PLOTTING HIST
## create plot
hist1 = mp.hist_plot(df_pattern, col_to_group1)

## save as SVG and HTML
mp.save_hist_plot(outputdir, plot, plot_name, format, set_col)


# plot scatter1, scatter2 & scatter 3


# plot heatmap

sys.exit()





# figure 2 = scatter2d
data_2dscatter_1 = df_pattern.groupby(['Support', 'Pattern length']).size().reset_index(name='Counts')

data_2dscatter_2 = df_pattern.groupby(['All-confidence', 'Pattern length']).size().reset_index(name='Counts')

#data_2dscatter_3 = df_pattern.groupby(['Cross-support', 'Pattern length']).size().reset_index(name='Counts')

scatter_2d_1 = px.scatter(data_2dscatter_1, x="Pattern length", y="Counts", color="Support")
scatter_2d_1.update_traces(marker=dict(size=data_2dscatter_1['Pattern length']*5))
#scatter_2d_1.show()

scatter_2d_2 = px.scatter(data_2dscatter_2, x="Pattern length", y="Counts", color="All-confidence")
scatter_2d_2.update_traces(marker=dict(size=data_2dscatter_2['Pattern length']*5))
#scatter_2d_2.show()

# scatter_2d_3 = px.scatter(data_2dscatter_3, x="Pattern length", y="Counts", color="Cross-support")
# scatter_2d_3.update_traces(marker=dict(size=data_2dscatter_3['Pattern length']*5))
#scatter_2d_3.show()





# figure 3 = scatter3d
data_3dscatter_1 = df_pattern.groupby(['Support', 'Pattern length','All-confidence']).size().reset_index(name='Counts')
print(data_3dscatter_1.head())
# data_3dscatter_2 = df_pattern.groupby(['Support', 'Pattern length','Cross-support']).size().reset_index(name='Counts')
# print(data_3dscatter_2.head())

scatter3d_1 = px.scatter_3d(data_3dscatter_1, x='Counts', y='Support', z='All-confidence',
              color='Pattern length')
# scatter3d_2 = px.scatter_3d(data_3dscatter_2, x='Counts', y='Support', z='Cross-support',
#               color='Pattern length')

#scatter3d_1.show()
#scatter3d_1.write_image(os.path.join(input_dir, 'scatter3d_prova.svg'))
#scatter3d_1.write_html(os.path.join(input_dir, 'scatter3d_prova.html'))

#scatter3d_2.show()
