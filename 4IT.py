searchfile = open("CSC_217_attendance_ week1final.txt", "r")
for line in searchfile:
    if "B141" in line: print (line)
searchfile.close()
