import os
import pandas as pd

class ParseDataInfor(object):
    # data_infoF, tab delimited files , with two column names in the header line as origin_name and new_name, output an dict with origin_name as key and new_name as value
    # data_dir, the grand-parents of the actual .fq.gz files, output a list of full paths for their sub directories
    def __init__(self, data_infoF, data_dir, origin_name, new_name):
        self.data_infoF = data_infoF
        self.data_dir = data_dir
        self.origin_name = origin_name
        self.new_name = new_name
        self.file_dict = {}  # empty dict
        self.dir_list = []  # empty list

    # read information from data_infoF, output a dict with origin_name as key and new_name as value
    def file_to_dict(self):
        df = pd.read_csv(self.data_infoF, sep="\t")
        self.file_dict = df.set_index(self.origin_name)[self.new_name].to_dict()

    # read information from data_dir, output a list of full paths for their sub-directories
    def dir_to_list(self):
        if (os.path.exists(self.data_dir)):
            for d in os.listdir(self.data_dir):
                full = self.data_dir + '/' + d
                if (os.path.isdir(full)):   # select directories
                    self.dir_list.append(full)
        else:
            print "The input dir %s is not a directory" % (self.data_dir)
