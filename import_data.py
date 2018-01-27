""" Reads in the dataFiles"""
import pandas as pd
import glob


def import_data(file_regex, index_col_val=None,
                format_str=None):
    """
        takes in a regular expression describing the filepath to
         the data files and returns a pandas dataFrame

         Usage1:      
         var_name = import_data.import_data("./hackathon_data/*20*.dat")
         
         Usage2:
         var_name = import_data.import_data("./hackathon_data/*20*.dat",
          "column of dates", "format of dates")

    """
    all_files = glob.glob(file_regex)
    all_files.sort()
    list_ = []
    for file_ in all_files:
        if index_col_val is not None:
            df = pd.read_csv(file_, index_col=index_col_val)
        else:
            df = pd.read_csv(file_)
        list_.append(df)
    ret = pd.concat(list_)
    if index_col_val is not None and format_str is not None:
        pd.to_datetime(ret.index, format=format_str,
                       errors='ignore')
        ret.sort_index(axis=0)
    return ret
