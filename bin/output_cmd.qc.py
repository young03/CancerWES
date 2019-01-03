import os
import argparse
import check_fastq_files
from parse_data_dir import ParseDataDir
from parse_data_infor import ParseDataInfor


def write_script(tool, outdir):
    # enumerate sub directories
    for data_dir in dir_list:
        #  replace to sub_newname
        sub_newname = file_dict[os.path.basename(data_dir)]
        out_dir_prefix = outdir + "/" + sub_newname
        if not os.path.isdir(out_dir_prefix):
            os.makedirs(out_dir_prefix)
        # print "Sub name: %s, out prefix, %s" % (sub_newname, out_dir_prefix)

        # output cmd files for each tool
        if tool == 'rename':
            out_file_prefix = out_dir_prefix + "/" + sub_newname
            write_rename(data_dir, out_file_prefix)
        else:
            print "The program %s has not be specified" % (tool)


def write_rename(indir, outprefix):
    (file1, file2) = check_fastq_files.check_fq(indir, args.suffix)
    if file1 and file2:
        print "ln -s %s %s_1.fq.gz" % (file1, outprefix)
        print "ln -s %s %s_2.fq.gz" % (file2, outprefix)
    else:
        print "Two files in $s, _1.fq.gz and _2.fq.gz is not prepared" % (indir)


# def write_fastqc(indir, outprefix):
#     print "fastqc %s/*.fq.gz -o %s &"  % (indir, outprefix)


# main
if __name__ == '__main__':
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--info_file", help="File including the data information, tab delimited, absolute path required")
    parser.add_argument("-d", "--data_dir", help="Directory name including the data files, absolute path required")
    parser.add_argument("-s", "--suffix", help="suffix for fastq files, .fq.gz or .fq")
    parser.add_argument("-t", "--tool", help="output script for [rename]")
    parser.add_argument("-o", "--outdir", help="directory for output files")
    args = parser.parse_args()

    # read data and dir information
    if args.info_file and args.data_dir and args.suffix and args.tool and args.outdir:
        my_dir = ParseDataDir(args.data_dir)
        my_infor = ParseDataInfor(args.info_file, 'Sample', 'Prefix')
        dir_list = my_dir.dir_to_list()
        file_dict = my_infor.file_to_dict()
        # print 'dir_list: ' + str(dir_list)
        # print 'file_dict: ' + str(file_dict)

        if dir_list and file_dict:
            # print comments and scripts
            print "### script for running %s" % (args.tool)
            write_script(args.tool, args.outdir)
    else:
        print "Five options should be specified: -f, -d, -s, -t and -o"
