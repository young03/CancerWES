import os
import argparse
from parse_data_infor import ParseDataInfor


def write_script(tool, outdir):
    # enumerate sub directories
    for data_dir in my_data.dir_list:
        #  prepare outdir or outprefix
        sub_newname = my_data.file_dict[os.path.basename(data_dir)]
        out_dir_prefix = outdir + "/" + sub_newname
        if not os.path.isdir(out_dir_prefix):
            os.makedirs(out_dir_prefix)
        # print "New name: %s, out prefix, %s" % (sub_newname, out_dir_prefix)

        # output cmd files for each tool
        if tool == 'rename':
            out_file_prefix = out_dir_prefix + "/" + sub_newname
            write_rename(data_dir, out_file_prefix)
        elif tool == 'fastqc':
            write_fastqc(data_dir, out_dir_prefix)
        else:
            print "The program %s has not be specified" % (tool)


def write_rename(indir, outprefix):
    file1, file2 = check_fq_gz(indir)
    if file1 and file2:
        print "ln -s %s %s_1.fq.gz" % (file1, outprefix)
        print "ln -s %s %s_2.fq.gz" % (file2, outprefix)
    else:
        print "Two files in $s, _1.fq.gz and _2.fq.gz is not prepared" % (indir)


def write_fastqc(indir, outprefix):
    print "fastqc %s/*.fq.gz -o %s &"  % (indir, outprefix)


def check_fq_gz(indir):
    file1 = indir + '/*_1.fq.gz'
    file2 = indir + "/*_2.fq.gz"
    return file1, file2


# main
if __name__ == '__main__':
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--info_file", help="File including the data information, tab delimited, absolute path required")
    parser.add_argument("-d", "--data_dir", help="Directory name including the data files, absolute path required")
    parser.add_argument("-t", "--tool", help="output script for [rename|fastqc|multiqc|bcbio_nextgen]")
    parser.add_argument("-o", "--outdir", help="directory for output files")
    args = parser.parse_args()

    # read data and dir information
    if args.info_file and args.data_dir and args.tool and args.outdir:
        my_data = ParseDataInfor(args.info_file, args.data_dir, 'Sample', 'Prefix')
        my_data.file_to_dict()  # my_data.file_dict
        my_data.dir_to_list()  # my_data.dir_list
        # print 'file_dict: ' + str(my_data.file_dict)
        # print 'dir_list: ' + str(my_data.dir_list)

        if my_data.file_dict and my_data.dir_list:
            # print comments and scripts
            print "### script for running %s" % (args.tool)
            write_script(args.tool, args.outdir)
    else:
        print "Four options should be specified: -f, -d, -t and -o"
