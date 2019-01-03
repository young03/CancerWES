import os

## data_dir, subdir containing .fq.gz/.fq files
## suffix, .fq.gz or .fq
## return the absolute path of two .fq.gz/.fq files (_1 and _2)
def check_fq(data_dir, suffix):
    r1_list = []
    r2_list = []
    if (os.path.exists(data_dir)):  # check data_dir
        for f in os.listdir(data_dir):
            suffix1 = '_1' + suffix
            suffix2 = '_2' + suffix
            if len(f.split(suffix1)) == 2:
                r1_list.append(os.path.join(data_dir, f))
            if len(f.split(suffix2)) == 2:
                r2_list.append(os.path.join(data_dir, f))
    else:
        print "The input dir %s is not a directory" % (data_dir)

    if len(r1_list) == 1 and len(r2_list) == 1:
        return(r1_list[0], r2_list[0])
