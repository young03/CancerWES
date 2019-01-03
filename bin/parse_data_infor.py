import pandas as pd

class ParseDataInfor(object):
    # data_infoF, tab delimited files , with two column names in the header line as origin_name and new_name
    # output an dict with origin_name(sub dirs in data_dir) as key and new_name as value
    def __init__(self, data_infoF, origin_name, new_name):
        self.data_infoF = data_infoF
        self.origin_name = origin_name
        self.new_name = new_name
        self.file_dict = {}  # empty dict

    # read information from data_infoF, output a dict with origin_name as key and new_name as value
    def file_to_dict(self):
        df = pd.read_csv(self.data_infoF, sep="\t")
        self.file_dict = df.set_index(self.origin_name)[self.new_name].to_dict()
        return self.file_dict
