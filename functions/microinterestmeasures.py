### INTEREST MEASURES ###

import os
import re
import string
import numpy as np
import pandas as pd
import functions.microimport as mi
import functions.microfim as mf


def calculate_ids_frequency(input_directory, trasactional_file):
    frequency_ids_dict = {}
    document_text = open(os.path.join(input_directory, trasactional_file), 'r')
    text_string = document_text.read().lower()
    print(text_string)

    #match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    # ^.
    match_pattern = re.findall('\b.\b', text_string)
    #print(match_pattern)

    for word in match_pattern:
        count = frequency_ids_dict.get(word,0)
        frequency_ids_dict[word] = count + 1

    frequency_list = frequency_ids_dict.keys()

    # for words in frequency_list:
    #     print(words, frequency_ids_dict[words])

    return frequency_ids_dict


def calculate_ids_occurrence(df_otu):
    df_otu2 = df_otu.iloc[:, 1:]
    df_otu2[df_otu2 > 0] = 1

    df_otu2['Occurrences'] = df_otu2.sum(axis=1)

    ids = df_otu['#ID'].str.lower().str.replace(' ','_')
    print(ids)
    occurrences = df_otu2['Occurrences']
    L = [ids,occurrences]
    new_df = pd.concat(L, axis=1)

    frequency = dict(zip(new_df['#ID'], new_df['Occurrences']))

    return frequency


def all_confidence(input_data, frequency, n_samples):
    """All-confidence interest measure calculation
    allC(X) = supp(X) / max_x_supp(X) - where max_x_supp(X) is the support of the item with the highest support in X.
    Range: [0,1]

    All-confidence means that all rules which can be generated from itemset X have
    at least a confidence of allC(X).
    All-confidence possesses the downward-closed closure property and thus can be effectively used inside
    mining algorithms. All-confidence is null-invariant.

    (Ref: https://michael.hahsler.net/research/association_rules/measures.html#all-confidence)
    """

    all_c_array = np.empty(input_data.shape[0], dtype=object)

    for index, row in input_data.iterrows():
        #print(index)
        p = row['Patterns']
        p = p.lower()
        pattern_supp = row['Support']
        #print(pattern_supp)
        c = mi.convert_pattern_to_list(p)
        #print(c)
        e_supports = []
        for e in c:
            #print('e:', e)
            s = frequency.get(e, 0)
            #print('s:', s)
            #print('n_samples: ', n_samples)
            e_s = round(float(s/n_samples), 2)
            #print('e_s:', e_s)
            if e_s == 0.0:
                all_c = 0
            else:
                e_supports.append(e_s)
                max_s = max(e_supports)
                #print(max_s)

                all_c = round(float(pattern_supp/max_s), 2)
                #print(pattern_supp)
                #print(max_s)
                #print(all_c)
        all_c_array[index] = all_c

    input_data['All-confidence'] = all_c_array.tolist()

    return input_data


def add_interest_measures(data_table, df, trans_file, data_dir):
    """
    """
    # calculate frequency
    frequency = calculate_ids_occurrence(data_table)
    print(frequency)

    # calculate len of trans_file
    number_of_lines = mf.len_trans_file(data_dir, trans_file)

    # calculate all-confidence
    data_allc_update = all_confidence(df, frequency, number_of_lines)

    return data_allc_update


def add_table_export(data_allc_update, data_dir, add_interest_file):
    """
    """
    data_allc_update.to_csv(os.path.join(data_dir, 'df_' + add_interest_file + '.csv'), index=False)

    return


def cross_support(input_data, frequency, n_samples):
    """# crossSupportRatio
    # Defined on itemsets as the ratio of the support of the least frequent
    # item to the support of the most frequent item, a ratio smaller than a set threshold.
    # Normally many found patterns are cross-support patterns which contain frequent
    # as well as rare items. Such patterns often tend to be spurious.

    # crossSupportRatio(X) = min_x_supp(X) / max_x_supp(X)
    """

    cross_support_array = np.empty(input_data.shape[0], dtype=object)

    for index, row in input_data.iterrows():
        #print(index)
        p = row['Patterns']
        p = p.lower()
        pattern_supp = row['Support']
        #print(pattern_supp)
        c = mi.convert_pattern_to_list(p)
        #print(c)
        e_supports = []
        for e in c:
            s = frequency.get(e, 0)
            #print('s:', s)
            e_s = round(float(s/n_samples), 2)
            #print('e_s:', e_s)
            e_supports.append(e_s)

            min_s = min(e_supports)

            max_s = max(e_supports)
            if max_s == 0.0:
                cross_supp = 0
            else:
                #print(max_s)

                cross_supp= round(float(min_s/max_s), 2)
                #print(pattern_supp)
                #print(min_s)
                #print(max_s)
                #print(cross_supp)
        cross_support_array[index] = cross_supp

    input_data['Cross-support'] = cross_support_array.tolist()

    return input_data
