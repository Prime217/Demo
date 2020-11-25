lines_seen = set() # holds lines already seen
with open("CSC_217_attendance_ week1final.txt", "w") as output_file:
	for each_line in open("CSC_217_attendance_ week1raw.txt", "r"):
	    if each_line not in lines_seen: # check if line is not duplicate
	        output_file.write(each_line)
	        lines_seen.add(each_line)
