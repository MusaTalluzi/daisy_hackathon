""" Reads in the dataFiles"""
import pandas as pd
import glob

'''
    takes in a regular expression describing the filepath to
     the data files and returns a pandas dataFrame
     
     Usage:      
     var_name = import_data.import_data("./hackathon_data/*20*.dat")
'''
def import_data(file_regex):
    all_files = glob.glob(file_regex)
    list_ = []
    for file_ in all_files:
        df = pd.read_csv(file_)
        list_.append(df)
    ret = pd.concat(list_)
    return ret
