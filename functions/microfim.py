# functions to run microFim

import pandas as pd
import numpy as np
import fim
import os
import csv
import functions.microimport as mi
import functions.microinterestmeasures as mim

""" Functions to run main microFIM functions. For simpilicty, to use this functions
into a Python script or Python Interpreter, import functions.microfim as mf """


### MANAGING AND CONVERTING FILES ###

def filter_data_table(metadata, data_table):
    """
    """
    samples = metadata['#SampleID'].to_list()
    id = data_table[['#ID']]
    samples_table = data_table[[*samples]]
    filter_table = pd.concat([id, samples_table], axis=1)
    no_zeros = (filter_table.iloc[:,1:] != 0).any(axis=1)
    filter_table = filter_table.loc[no_zeros]
    return filter_table


def write_transactions(n_columns, n_rows, dataset):
    """ per ogni colonna, se a quella riga x > 0 prendi il nome della riga e
    aggiungilo alla lista della colonna """
    transactions = []
    for c in np.arange(1, n_columns+1):
        print(c)
        list = []
        for r in np.arange(0, n_rows+1):
            print(r)
            print(dataset.iloc[r,c])
            if dataset.iloc[r,c] > 0:
                item = dataset.iloc[r,0]
                #print(item)
                list.append(item)
            else:
                pass

        transactions.append(list)
    return transactions


def convert_in_transaction_list(filter_table, data_table_name):
    """
    """
    # remove space from ID column
    filter_table['#ID'] = filter_table['#ID'].str.replace(' ','_')
    n_cols = filter_table.shape[1] - 1
    n_rows = filter_table.shape[0] - 1
    transaction_list = write_transactions(n_cols, n_rows, filter_table)
    return transaction_list


def save_transaction_list(data_dir, t_list, file_name):
    """
    """
    # save as transaction list
    with open(data_dir + '/' + 'transactions_' + file_name[0], 'w') as f:
        wr = csv.writer(f)
        wr.writerows(t_list)

    return

def import_fim_table():
    """ This function allow to import the itemset file in Python to perform other
    analysis (e.g. calculate and add new interest measures).

    Input: itemsets calculated (output of mf.calculate_fim)
    Output: Python object - input of interest measures functions (e.g. mf.cross_support)
    """
    return la


def read_transaction(t):
    a_file = open(t, "r")
    list_of_lists = []
    for line in a_file:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      list_of_lists.append(line_list)

    a_file.close()
    return list_of_lists


### ARM FUNCTIONS ###

def itemsets_algorithm_parameters(file_param):
    """ Import file with parameters for itemset and rules calculation.
    The file is available as a template into github repository, it has ten rows
    two columns. This funtion extract algorithm information.
    """
    cols = ['Parameter', 'Value']
    parsed = file_param.iloc[0, 1]

    return parsed


def fim_calculation(input, target, minsupp, zmin, zmax):
    """ Run fim scripts based on algorithm type (parsed by mf.itemsets_algorithm_parameters)
    and parameters imported (mi.itemsets_parameters).
    """
    itemsets = []
    report= '[asS'
    if target == 'i':
        itemsets = fim.eclat(input, target='s', supp=minsupp, zmin=zmin, report=report)
        #print(result)
    elif target == 'c':
        itemsets = fim.eclat(input, target='c', supp=minsupp, zmin=zmin, report=report)
        #print(result)
    elif target == 'm':
        itemsets = fim.eclat(input, target='m', supp=minsupp, zmin=zmin, report=report)
        #print(result)
    elif target == 'g':
        itemsets = fim.eclat(input, target='g', supp=minsupp, zmin=zmin, report=report)
        #print(result)

    return itemsets


def write_results(results, data_dir, output_file):
    """
    """
    # write results
    file = open(data_dir + '/' + output_file + '.csv', 'w+', newline ='')
    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(results)

    out_file = data_dir + '/' + output_file + '.csv'
    new_out_file = data_dir + '/df_' + output_file + '.csv'
    with open(out_file, 'r') as f, open(new_out_file, 'w') as fo:
        for line in f:
            fo.write(line.replace('"', '').replace("'", "").replace('),[', ')/[').replace(')', '').replace('(', '').replace('[', '').replace(']', ''))


    return file, out_file, new_out_file


def itemsets_dataframe(input_file):
    df = pd.read_csv(input_file, sep='/', header=None)
    df.columns =['Patterns', 'Points']

    data_patterns = df['Patterns']

    ## expand
    data_points = df.Points.str.split(",", expand=True,)

    # merge
    data = pd.concat([data_patterns, data_points], axis=1)
    data.columns = ['Patterns', 'Samples', 'Support', 'Support(%)']
    data = data.astype({"Samples": int, "Support": float, "Support(%)": float})
    data['Support'] = data['Support'].round(2)
    data['Support(%)'] = data['Support(%)'].round(2)
    data['Pattern length'] = data.Patterns.str.count(',')
    data['Pattern length'] += 1

    return data


def export_dataframe(df, outdir, output_file):
    """
    """
    output_file_name = 'df_' + output_file + '.csv'
    df.to_csv(os.path.join(outdir, output_file_name), index=False)

    return

def calculate_ids_frequency(input_directory, trasactional_file):
    frequency_ids_dict = {}
    document_text = open(os.path.join(input_directory, trasactional_file), 'r')
    text_string = document_text.read().lower()
    print(text_string)

    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    print(match_pattern)

    for word in match_pattern:
        count = frequency_ids_dict.get(word,0)
        frequency_ids_dict[word] = count + 1

    frequency_list = frequency_ids_dict.keys()

    # for words in frequency_list:
    #     print(words, frequency_ids_dict[words])

    return frequency_ids_dict


def len_trans_file(data_dir, trans_file):
    """
    """
    lines_in_file = open(os.path.join(data_dir, trans_file), 'r').readlines()
    lines = float(len(lines_in_file))

    return lines


def export_add_patterns():
    """
    """
    return


def set_patterns_for_matching(pattern_dataframe):
    col_patterns = pattern_dataframe['Patterns'].tolist()

    # create list of patterns and re-order them alphabetically (lower condition - apply also to transactional data)
    for p in range(len(col_patterns)):
        col_patterns[p] = col_patterns[p].replace(',', '')
        col_patterns[p] = col_patterns[p].lower()
        col_patterns[p] = col_patterns[p].split()
        col_patterns[p] = sorted(col_patterns[p])
        col_patterns[p] = ' '.join(map(str, col_patterns[p]))

    return col_patterns


def set_transdata_for_matching(input_dir, trans_file):
    transactional_list = []
    with open(os.path.join(input_dir, trans_file)) as f:
        transactional_list = []
        lines = [line.rstrip() for line in f]
        for line in lines:
            transactional_list.append(line)

    for l in range(len(transactional_list)):
        transactional_list[l] = transactional_list[l].lower()
        transactional_list[l] = transactional_list[l].split()
        transactional_list[l] = sorted(transactional_list[l])
        transactional_list[l] = ' '.join(map(str, transactional_list[l]))

    return transactional_list


def generate_pattern_occurrences(input_dir, col_patterns, transactional_list, meta_file, sep):
    pattern_table = []

    for a in col_patterns:
        pattern_line = []
        #print('pattern:', a)
        for b in transactional_list:
            #print('sample transactional:', b)
            result = all(elem in b for elem in a)
            if result:
                pattern_line.append(1)
            else:
                pattern_line.append(0)
        pattern_table.append(pattern_line)

    print('pattern_table:', pattern_table)
    df_meta = pd.read_csv(os.path.join(input_dir, meta_file), sep=sep, header=0, index_col=None)
    print(df_meta, '\n')
    # print(df_meta.columns)

    meta_cols = df_meta.columns
    print(meta_cols)
    #list_of_names = student_df['Name'].to_list()
    #sample_cols = meta_cols[1:]
    sample_cols = df_meta['#SampleID'].to_list()
    print(sample_cols)

    pattern_table = pd.DataFrame.from_records(pattern_table, columns=sample_cols)
    # print(pattern_table)

    return pattern_table


def generate_pattern_occurrences_rev(input_dir, col_patterns, transactional_list, meta_file, sep):
    pattern_table = []

    for a in col_patterns:
        pattern_line = []
        #print('pattern:', a)
        for b in transactional_list:
            #print('sample transactional:', b)
            result = all(elem in b for elem in a)
            if result:
                pattern_line.append(1)
            else:
                pattern_line.append(0)
        pattern_table.append(pattern_line)

    print('pattern_table:', pattern_table)
    #df_meta = pd.read_csv(os.path.join(input_dir, meta_file), sep=sep, header=0, index_col=None)
    #print(df_meta, '\n')
    # print(df_meta.columns)

    meta_cols = meta_file.columns
    print(meta_cols)
    #list_of_names = student_df['Name'].to_list()
    #sample_cols = meta_cols[1:]
    sample_cols = meta_file['#SampleID'].to_list()
    print(sample_cols)
    pattern_table = pd.DataFrame.from_records(pattern_table, columns=sample_cols)
    # print(pattern_table)

    return pattern_table


def generate_pattern_table(data_allc_update, df, data_dir, trans_file, metadata, meta_sep):
    """
    """
    col_patterns = set_patterns_for_matching(data_allc_update)
    transactional_list = set_transdata_for_matching(data_dir, trans_file)
    pattern_table = generate_pattern_occurrences_rev(data_dir, col_patterns, transactional_list, metadata, meta_sep)
    pattern_table_complete = concat_tables(df, pattern_table)

    return pattern_table_complete


def export_pattern_tables(pattern_table, data_dir, out_file_name):
    """
    """
    #df_pattern_table_clean = pattern_table.drop(['Samples', 'Support', 'Support(%)', 'Pattern length', 'All-confidence'], axis=1)
    # export standard
    pattern_table.to_csv(os.path.join(data_dir, out_file_name + '_complete.csv'), index=False)

    # export cleaned
    #df_pattern_table_clean.to_csv(os.path.join(data_dir, out_file_name + '.csv'), index=False)

    return

def concat_tables(df, pattern_table):
    df_pattern_table = pd.concat([df, pattern_table], axis=1)
    return df_pattern_table
