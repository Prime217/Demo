data = data2 = "" 
  
with open('CSC_217_attendance_ week1_30.txt') as fp: 
    data = fp.read() 
  
with open('CSC_217_attendance_ week1_end.txt') as fp: 
    data2 = fp.read() 

data += "\n"
data += data2 
  
with open ('CSC_217_attendance_ week1raw.txt', 'w') as fp: 
    fp.write(data) 
