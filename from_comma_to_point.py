from interface_1 import *
import glob
import os

path = old_path
savepath = new_path

for files in glob.glob(path + "\*.txt"): # iterating through all files .txt in a selected folder
    base = os.path.basename(files) # fetching a file name only
    infile = open(files, "r")
    outfile = open(savepath + f"\{base[:-4]}_new.txt", "w")
    for line in infile:
        outfile.write(line.replace(",", "."))

infile.close()
outfile.close()