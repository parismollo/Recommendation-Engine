import sys
import os

dir_name = sys.argv[1]

try:
    os.mkdir(dir_name)
except FileExistsError:
    import glob
    chunk_name_list = glob.glob(dir_name + "/chunk-*.txt")
    for chunk_name in chunk_name_list:
        try:
            os.remove(chunk_name)
        except SystemError:
            print("Something went wrong...")

chunk_nb = 1
line_nb = 0

for line in sys.stdin:
    if line_nb == 0:
        out = open(dir_name + "/chunk-" + str(chunk_nb) + ".txt", "w")
    line_nb += 1
    out.write(line)
    if line_nb == 250000:
        chunk_nb += 1
        line_nb = 0
