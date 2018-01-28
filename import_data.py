""" Reads in the dataFiles"""
import pandas as pd
import glob


def parse_date(given_date, date_format):
    try:
        return pd.datetime.strptime(given_date, date_format)
    except ValueError:
        return pd.NaT


def import_data(file_regex, index_col_val=None, parse_dates=None,
                date_format=None):
    """
        takes in a regular expression describing the filepath to
         the data files and returns a pandas dataFrame

         Usage1:      
         var_name = import_data.import_data("./hackathon_data/*20*.dat")
         
         Usage2:
         var_name = import_data.import_data("./hackathon_data/*20*.dat",
          "column to index with", "column of dates", "format of dates")

    """
    all_files = glob.glob(file_regex)
    all_files.sort()
    list_ = []
    for file_ in all_files:
        if index_col_val is not None and parse_dates is not None and \
                        date_format is not None:
            df = pd.read_csv(file_, parse_dates=[parse_dates],
                             index_col=index_col_val,
                             date_parser=lambda x:
                             parse_date(x, date_format))
        elif index_col_val is not None:
            df = pd.read_csv(file_, index_col=index_col_val)
        elif parse_dates is not None and date_format is not None:
            df = pd.read_csv(file_, parse_dates=[parse_dates],
                             date_parser=lambda x:
                             parse_date(x, date_format))
        else:
            df = pd.read_csv(file_)
        list_.append(df)
    ret = pd.concat(list_)
    ret = ret[ret.index.notnull()]
    ret.on_promotion.replace(('Y', 'N'), (1, 0), inplace=True)
    
    return ret

if __name__ == '__main__':
    data = import_data(file_regex="./hackathon_data/*20*.dat",
                        parse_dates="date_", date_format="%Y%m%d")
    data.to_csv('./hackathon_data/test_data.csv')
    print(data.head())