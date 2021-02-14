from interface_2 import *
import glob
import os

path = file_path
savepath = new_path


infile = open(path, "r")
base = os.path.basename(path) # fetching a file name only
outfile = open(savepath + f"\{base[:-4]}_record_found.txt", "w")

i = 0

for line in infile:
    if value in line:
        i += 1
        outfile.write(line)

infile.close()
outfile.close()

if i == 0:
    os.remove(savepath + f"\{base[:-4]}_record_found.txt") # deleting a .txt file if it is empty