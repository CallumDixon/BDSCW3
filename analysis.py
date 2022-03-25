from cgi import test
import os
import pandas as pd

my_dir = "./output"# enter the dir name

min = None
min_row = None
min_file= ""
min_dir=""

for fname in os.listdir(my_dir):
    if "energy" in fname:

        energy_dir = "./output/" + fname +"/global-cost.csv"

        gc = pd.read_csv(energy_dir)

        test_min = gc['Run-0'].min()

        if min is None or test_min < min:
            min = test_min
            min_row = gc['Run-0'].idxmin()
            min_file = energy_dir
            min_dir = "./output/" + fname

with open(min_dir+"/global-response.csv", "r+") as f:
    next
    for line in f:
        parsed = line.split(',')
        if str(parsed[1]) == str(min_row):
            vals = parsed[2:]
            total = 0
            for val in vals:
                total = total + float(val)
            
            print("Total Power Demand: " + str(total))

print("Minimum Variance: " + str(min))
print("Iteration: " + str(min_row))
print("Folder: " + str(min_dir))