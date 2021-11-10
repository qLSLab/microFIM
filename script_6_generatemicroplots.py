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

from sklearn.metrics import pairwise_distances #jaccard diss.
from sklearn import manifold


""" This script produce plotly figures inspired by common microbiome data
visualization representations """

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
out_dir = '/Users/j/Documents/PHD/MICROFIM/microFim_dev/ecam_inputs/'

os.chdir(input_dir)
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

print(os.listdir(input_dir), '\n')

# pattern input
pattern_input = 'pattern_table_test_complete.csv'
# pattern_input = input("Insert your pattern file:\n\n")
# print(f'> You entered: {pattern_input}\n\n')

# metadata file
meta_input = 'list_id0_vaginal_date0.csv'
# meta_input = input("Insert your metadata file:\n\n")
# print(f'> You entered: {meta_input}\n\n')


# df import
df_pattern = pd.read_csv(os.path.join(input_dir, pattern_input), header=0, index_col=None)

df_pattern = df_pattern.drop(['Support(%)'], axis=1)

print(df_pattern)
print(df_pattern.columns)



## fix path
df_metadata = pd.read_csv(os.path.join(out_dir, meta_input), header=0, index_col=None)
print(df_metadata)
print(df_metadata.columns)

pattern_table = df_pattern.drop(['Samples','Support','Pattern length','All-confidence','Cross-support'], axis=1)


# filter samples from metadata
samples = df_metadata.iloc[:,0].to_list()
print(samples)

# filter samples from pattern table
df_filt_pattern = pattern_table[samples]
print(df_filt_pattern)
data = df_filt_pattern.to_numpy()
print(data)
print(data.shape)


#jaccard distance matrix
data_t = np.transpose(data)
dis_matrix = pairwise_distances(data_t, metric = 'jaccard')

np.savetxt(os.path.join(input_dir, 'jaccard_dist_matrix.csv'), dis_matrix, delimiter=',', fmt='%1.2f')

print(dis_matrix.shape)

## 0 = identici

dis_heatmap = px.imshow(dis_matrix,
                x=samples,
                y=samples)
dis_heatmap.update_layout(coloraxis_colorbar=dict(
    title="Jaccard index",
    tickvals=[0,1],
    ticktext=["0","1"],
    lenmode="pixels", len=100,
))

#dis_heatmap.write_html(os.path.join(input_dir, 'dis_heatmap_prova.html'))
#fig.show()


# heatmap originale
patterns = pattern_table['Patterns'].to_list()

pattern_heatmap = px.imshow(data,
                x=samples, y=patterns)
# pattern_heatmap.update_layout(coloraxis_colorbar=dict(
#     title="Presence/absence pattern heatmap",
#     tickvals=[0,1],
#     ticktext=["0","1"],
#     lenmode="pixels", len=100,
# ))
pattern_heatmap.show()




sys.exit()


#hover_name="country", hover_data=["continent", "pop"]
# barplot percentuale e non
# barchart
# filter samples and patterns from pattern table
df_filt_pattern = pattern_table[samples]

patterns = pattern_table['Pattern length']
df_barchart = pd.concat([patterns, df_filt_pattern], axis=1)
print(df_barchart)

df_barchart_group = df_barchart.groupby(['Pattern length', samples]).size().reset_index(name='Counts')
barchart = px.bar(df_barchart_group, x=samples, y="Counts", color='Pattern length')
barchart.show()

# heatmap originale e filtrata

# per la dashboard, posso pensare di evitare grandi plot come la heatmap
# e lasciare solo i plot di andamento
