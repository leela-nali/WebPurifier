# importing the required modules
import os
import argparse

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."


def validate_file(file_name):


def valid_filetype(file_name):
    # validate file type
    return file_name.endswith('.txt')

def valid_path(path):
    # validate file path
    return os.path.exists(path)

def add(args):


def delete(args):


def whitelist(args):

def blacklist(args):


def main():
    parser = argparse.ArgumentParser(description = "A filterlist CLI tool!")
    parser.add_argument("-a", "--add", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Adds filter list")
    parser.add_argument("-d", "--delete", type = str, nargs = 1,
                        metavar = "path", default = None,
                        help = "Deletes filter list")
    parser.add_argument("-w", "--whitelist", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Whitelists filter list")
    parser.add_argument("-b", "--blacklist", type = str, nargs = 2,
                        metavar = ('file1','file2'), help = "Blacklists filterlist")
    args = parser.parse_args()
    if args.add != None:
        read(args)
    elif args.delete != None:
        show(args)
    elif args.whitelist !=None:
        delete(args)
    elif args.blacklist != None:
        copy(args)

if __name__ == "__main__":
    # calling the main function
    main()