import os
import argparse
import check_fastq_files
from parse_data_dir import ParseDataDir


def write_script(tool, outdir):
    # prepare outdir
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    # enumerate sub directories
    for data_dir in dir_list:
        sub_name = os.path.basename(data_dir)
        out_dir_prefix = outdir + "/" + sub_name
        # print "Sub name: %s, out prefix, %s" % (sub_name, out_dir_prefix)

        # output cmd files for each tool
        if tool == 'bwa-sambamba':
            write_bwa_sambamba(data_dir, outdir, sub_name)
        else:
            print "The program %s has not be specified" % (tool)


def write_bwa_sambamba(indir, outdir, subname):
    (fq1, fq2) = check_fastq_files.check_fq(indir, args.suffix)
    if fq1 and fq2:
        outfile = os.path.join(outdir, subname + '.sorted.bam')
        logfile = os.path.join(args.logdir, "bwa_" + subname + ".log" )
        bwa_script = "bwa mem -t %s %s %s %s" % (args.cpus, args.genome_file, fq1, fq2)
        view_script = "sambamba view -t %s -S -f bam -o /dev/stdout /dev/stdin" % (args.cpus)
        sort_script = "sambamba sort -t %s -o %s /dev/stdin &>%s" % (args.cpus, outfile, logfile)
        print "time %s |%s |%s &" % (bwa_script, view_script, sort_script)

        # print "%s \\\n|%s \\\n|%s" % (bwa_script, view_script, sort_script)   # multiple lines
        # example:
        # bwa mem ../genome/hg19.genome.fa N1_blood.test_1.fq.gz N1_blood.test_2.fq.gz >N1_blood.test.sam
        # bwa mem -t 3 ../genome/hg19.genome.fa N1_blood.test_1.fq.gz N1_blood.test_2.fq.gz |sambamba view -t 3 -S -f bam -o /dev/stdout /dev/stdin |sambamba sort -t 3 -o test.bam /dev/stdin
    else:
        print "Two files in $s, _1.fq.gz and _2.fq.gz is not prepared" % (indir)


# main
if __name__ == '__main__':
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_dir", help="Directory name including the data files, absolute path required")
    parser.add_argument("-g", "--genome_file", help="File name of genome sequence, absolute path required")
    parser.add_argument("-s", "--suffix", help="suffix for fastq files, .fq.gz or .fq")
    parser.add_argument("-t", "--tool", help="output script for [bwa-sambamba]")
    parser.add_argument("-o", "--outdir", help="directory for output files")
    parser.add_argument("-l", "--logdir", help="directory for recording log information")
    parser.add_argument("-c", "--cpus", help="cpu number for running")
    args = parser.parse_args()

    # read data and dir information
    if args.data_dir and args.genome_file and args.suffix and args.tool and args.outdir and args.logdir and args.cpus:
        my_dir = ParseDataDir(args.data_dir)
        dir_list = my_dir.dir_to_list()  # my_data.dir_list
        # print 'dir_list: ' + str(dir_list)

        if dir_list:
            # print comments and scripts
            print "### script for running %s" % (args.tool)
            write_script(args.tool, args.outdir)
    else:
        print "Seven options should be specified: -d, -g, -s, -t, -o, -l and -c"