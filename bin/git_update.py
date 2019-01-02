import os
import sys
import argparse

# main
if __name__ == '__main__':
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--desc", help="Message for git commit -m, RECOMMENDED!")
    parser.add_argument("-d", "--dry_run", action= "store_true", help="Only print commands, but not run them")  # how to use boolean option?
    parser.add_argument("files", nargs='+', help="File names for git add")
    args = parser.parse_args()

    # get command infor for git adding
    if args.desc:
        file_list = ' '.join(args.files)
        git_command = "git add %s;  git commit -m \"%s\";  git push origin master" % (file_list, args.desc)
    else:
        print "Please input options:-m"

    # run or print
    print git_command
    if not args.dry_run:
        os.system(git_command)