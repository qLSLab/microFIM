# functions to import files to run microFim

import pandas as pd
import os

def import_table():
    return table

def import_sample_list():
    return sample_list


def itemsets_parameters(input_dir, file_param):
    """ Import file with parameters for itemset and rules calculation.
    The file is available as a template into github repository, it has ten rows
    two columns. Save parameters indipendently.
    """
    p = pd.read_csv(os.path.join(input_dir, file_param),  header=0, index_col=None)

    #target = p.iloc[0]['Value']
    minsupp = int(p.iloc[0]['Value'])
    zmin = int(p.iloc[1]['Value'])
    zmax = int(p.iloc[2]['Value'])
    #report = p.iloc[3]['Value']
    # è possibile che il report sia identico per tutte
    # le funzioni e quindi potrei tenerlo anche nell'uso della libreria

    return minsupp, zmin, zmax


def convert_pattern_to_list(string):
    li = list(string.split(", "))
    return li


def import_diversity_parameters():
    return diversity_parameters

def import_plot_file():
    return plots
