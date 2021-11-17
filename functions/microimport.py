# functions to import files to run microFim

import pandas as pd
import os


""" Functions to set import files to run microFIM. For simpilicty, to use this functions
into a Python script or Python Interpreter, import functions.microimport as mi

"""


def import_metadata(metadata, data_dir, sep):
    """ Import metadata file as pandas dataframe.
    Arguments:
    - metadata: metadata file name;
    - data_dir: metadata file name directory;
    - sep: type of separator within metadata file (e.g. \t)
    """
    meta_file = pd.read_csv(os.path.join(data_dir, metadata), sep=sep, header=0, index_col=None)
    return meta_file


def import_data_table(data_table, data_dir, sep):
    """ Import data table file (intended as OTU, ESV or taxa table) as pandas dataframe.
    Arguments:
    - data_table: data file name;
    - data_dir: data file name directory;
    - sep: type of separator within metadata file (e.g. \t)
    """
    data_table = pd.read_csv(os.path.join(data_dir, data_table), sep=sep, header=0, index_col=None, engine='python')
    return data_table


def itemsets_parameters(input_dir, file_param):
    """ Import file with parameters for itemset and rules calculation.
    The file is available as a template into github repository, it has ten rows
    two columns. Save parameters indipendently.
    """
    p = pd.read_csv(os.path.join(input_dir, file_param),  header=0, index_col=None)

    minsupp = int(p.iloc[0]['Value'])
    zmin = int(p.iloc[1]['Value'])
    zmax = int(p.iloc[2]['Value'])

    return minsupp, zmin, zmax


def output_file_name(data_table_name):
    """
    """
    file_name = data_table_name.split('.')
    return file_name


def import_pattern_dataframe(data_dir, output_file):
    """
    """
    output_file_name = 'df_' + output_file + '.csv'
    dataframe = pd.read_csv(os.path.join(data_dir, output_file_name), header=0, index_col=None)
    return dataframe


def import_pattern_dataframe_rev(data_dir, output_file):
    """
    """
    dataframe = pd.read_csv(os.path.join(data_dir, output_file), header=0, index_col=None)
    return dataframe


def import_pattern_dataframe_plot(data_dir, output_file):
    """
    """
    dataframe = pd.read_csv(os.path.join(data_dir, output_file), header=0, index_col=None)
    dataframe = dataframe.drop(['Support(%)'], axis=1)

    return dataframe


def convert_pattern_to_list(string):
    li = list(string.split(", "))
    return li
