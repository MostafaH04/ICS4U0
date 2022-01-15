# This is used to clear the csv files used to store the collected data

import os

for file in os.listdir(path = "."):
    if file.endswith(".csv"):
        with open(file, "w") as currFile:
            currFile.write("# of Objects, Time Spent\n")
