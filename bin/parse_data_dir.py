import os

class ParseDataDir(object):
    # data_dir, the grand-parents of the actual .fq.gz/.fq files, output a list of full paths for their sub directories
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.dir_list = []  # empty list

    # read information from data_dir, output a list of full paths for their sub-directories
    def dir_to_list(self):
        if (os.path.exists(self.data_dir)):  # check data_dir
            for d in os.listdir(self.data_dir):  # sub dirs
                full = os.path.join(self.data_dir, d)
                if (os.path.isdir(full)):   # select directories
                    self.dir_list.append(full)
        else:
            print "The input dir %s is not a directory" % (self.data_dir)

        return self.dir_list