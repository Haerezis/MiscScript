import argparse
import os
import shutil

def endwith(string, suffix_array) :
    for suffix in suffix_array :
        if string.endswith(suffix) : return True
    return False

def main() :
    parser = argparse.ArgumentParser(description = 'Script to splitting/copying files matching some file extensions inside a directory \
    tree to a destination directory, keeping the tree structure (intermediate directories)')

    parser.add_argument("-i", "--input", help="The input/source directory from where will be search the files", required=True)
    parser.add_argument("-o", "--output", help="The output/destination directory to where will be stored the matched files", required=True)
    parser.add_argument('file_extension', nargs='+',  help='The file extensions to use to match the files in the input source tree')

    args = parser.parse_args()
    
    if os.path.isdir(args.input) is False :
        print("The input path '{0}' doesn't exist or is not a directory".format(args.input))
        exit()
    if os.path.isdir(args.output) is False :
        print("The output path '{0}' doesn't exist or is not a directory".format(args.output))
        exit()
    
    inputPath = os.path.abspath(args.input)
    outputPath = os.path.abspath(args.output)
    directoriesToSearch = [inputPath];
    
    while len(directoriesToSearch) > 0 :
        path = directoriesToSearch.pop()
        directories = [path + "\\" + f for f in os.listdir(path) if os.path.isdir(path + "\\" + f)]
        directoriesToSearch += directories
        
        files = [path + "\\" + f for f in os.listdir(path) if os.path.isfile(path + "\\" + f) and endwith(f, args.file_extension)]
        for file in files :
            outputFile = outputPath + file[len(inputPath):]
            try :
                os.makedirs(os.path.dirname(outputFile), True)
            except :
                pass
            shutil.copy(file, outputFile) 

if __name__ =="__main__":
    main()
