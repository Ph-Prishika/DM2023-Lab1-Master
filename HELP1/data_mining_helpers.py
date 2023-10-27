import nltk

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(df, text_column_name):
    """ format the text field and strip special characters """
    D = []
    for row in df[text_column_name]:
        temp_d = " ".join(row.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, df, text_column_name ):
    """ format the labels """
    return  df[text_column_name].target_names[target]


def check_missing_values(df):
    """ Function that checks and verifies if there are missing values in a DataFrame """
    missing_values = df.isnull().sum()
    return missing_values

def check_missing_values(df):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in df:
        if element == True:
            counter+=1
    return ("The amount of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            tokens.append(word)
    return tokens
