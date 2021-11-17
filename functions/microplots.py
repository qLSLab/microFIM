import pandas as pd
import plotly.express as px
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import readline

import functions.microfim as mf
import functions.microdir as md
import functions.microinterestmeasures as mim
import functions.microimport as mi

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from sklearn.metrics import pairwise_distances
from sklearn import manifold


"""
"""


def calculate_distance_matrix(df_pattern, metadata):
    """
    """
    # filter samples from metadata
    samples = metadata.iloc[:,0].to_list()
    print(samples)
    # filter pattern table
    pattern_table_filt = df_pattern[samples]

    data = pattern_table_filt.to_numpy()

    #jaccard distance matrix
    data_t = np.transpose(data)
    dis_matrix = pairwise_distances(data_t, metric = 'jaccard')

    return dis_matrix


def plot_heatmap(dis_matrix, metadata, outputdir, output_name, format):
    """
    """
    samples = metadata.iloc[:,0].to_list()
    dis_heatmap = px.imshow(dis_matrix,
                    x=samples,
                    y=samples)

    dis_heatmap.update_layout(coloraxis_colorbar=dict(
        title="Jaccard index",
        tickvals=[0,1],
        ticktext=["0","1"],
        lenmode="pixels", len=100,
    ))

    if format == 'SVG':
        save_name = output_name + '_heatmap.svg'
        dis_heatmap.write_image(os.path.join(outputdir, save_name))

    elif format == 'HTML':
        save_name = output_name + '_heatmap.html'
        dis_heatmap.write_html(os.path.join(outputdir, save_name))

    return


def heatmap_function():
    """
    """
    return

def hist_plot(df_pattern, col_to_group):
    """
    """
    title = col_to_group + ' distribution'
    hist_df = df_pattern.groupby([col_to_group]).size().reset_index(name='Counts')
    hist = px.bar(hist_df, x=col_to_group, y='Counts', height=400, width=800,
                  color=col_to_group, title='Pattern length distribution')

    return hist


def save_hist_plot(outputdir, plot, plot_name, format, set_col):
    """
    """

    if format == 'SVG':
        save_name = plot_name + '_' + set_col + '_hist.svg'
        plot.write_image(os.path.join(outputdir, save_name))

    elif format == 'HTML':
        save_name = plot_name + '_' + set_col + '_hist.html'
        plot.write_image(os.path.join(outputdir, save_name))

    return


def scatter_plot_2d(df_pattern, col_to_group1, col_to_group2):
    """
    """
    title = col_to_group1 + ' and ' + col_to_group2 + ' distribution'
    scatter_df = df_pattern.groupby([col_to_group1, col_to_group2]).size().reset_index(name='Counts')
    scatter_2d = px.scatter(scatter_df, x=col_to_group1, y="Counts", color=col_to_group2)

    return scatter_2d


def save_scatter_2d_plot(outputdir, plot, plot_name, format):
    """
    """

    if format == 'SVG':
        save_name = plot_name + '_hist.svg'
        plot.write_image(os.path.join(outputdir, save_name))

    elif format == 'HTML':
        save_name = plot_name + '_hist.html'
        plot.write_image(os.path.join(outputdir, save_name))

    return


def scatter_plot_3d(df_pattern, col_to_group1, col_to_group2, col_to_group3):
    """
    """
    title = col_to_group1 + ' and ' + col_to_group2 + ' and ' + col_to_group3 + ' distribution'
    scatter_df = df_pattern.groupby([col_to_group1, col_to_group2, col_to_group3]).size().reset_index(name='Counts')
    scatter3d = px.scatter_3d(scatter_df, x='Counts', y=col_to_group1, z=col_to_group3, color=col_to_group2)

    return scatter_3d


def save_scatter_3d_plot(outputdir, plot, plot_name, format):
    """
    """

    if format == 'SVG':
        save_name = plot_name + '_hist.svg'
        plot.write_image(os.path.join(outputdir, save_name))

    elif format == 'HTML':
        save_name = plot_name + '_hist.html'
        plot.write_image(os.path.join(outputdir, save_name))

    return


def set_col_name(plot_name):
    """
    """
    col_name = [each_string.lower() for each_string in plot_name]
    name = col_name[0][:3]
    return name
