import argparse

def parserfun():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='The path needed for the export file')
    parser.add_argument('--format', default='json',choices=['json','csv'], type=str.lower) #to make the option taken in upper or lower case
    return parser

def main():
    import sys
    from cmdtool import export, users
    from cmdtool import users as usi #importing python files from the package

    args = parserfun().parse_args() #calling the parser function and parsing the arguments so we can use the --path and --format options
    users = usi.read_user() #fetching the user info 
    if args.path:
        file = open(args.path, 'w',newline='') #when the a pth option is chosen open that file and writhe stdout to it
    else:
        file = sys.stdout
    if args.format=='json': #json here is the default option unless csv is specified
        export.toJson(file, users)
    else:
        export.toCSV(file, users)

