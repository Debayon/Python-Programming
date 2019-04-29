#input repetedly until string "EndOfInput" is encountered
flag = True
Grading = {'A':10,'AB':9,'B':8,'BC':7,'C':6,'CD':5,'D':4}
Courses = {}
Students = {}
Output = {}
Grades = {}
inner_flag = True
temp_list = []
#while(flag):
dataLine = input()
#if(dataLine == "EndOfInput"):
#    flag = False
if(dataLine == "Courses"):
    while(inner_flag):
        dataLine = input()
        if(dataLine == "Students"):
            inner_flag = False
        else:
            temp_list = dataLine.split("~")
            Courses[temp_list[0]] = temp_list[1:len(temp_list)]
if(dataLine == "Students"):
    inner_flag = True
    while (inner_flag):
        dataLine = input()
        if (dataLine == "Grades"):
            inner_flag = False
        else:
            temp_list = dataLine.split("~")
            Students[str(temp_list[0])] = [temp_list[1],{}]
if(dataLine == "Grades"):
    inner_flag = True
    while(inner_flag):
        dataLine = input()
        if(dataLine == "EndOfInput"):
            inner_flag = False
            flag = False
        else:
            temp_list = dataLine.split("~")
            var = str(temp_list[3])
            Students[var][1][temp_list[0]] = temp_list[4]

for i in Students:
    gpa = 0
    for j in Students[i][1]:
        gpa = gpa + Grading[Students[i][1][j]]  # check string - non-string consistency
    if(len(Students[i][1]) != 0):
        gpa = gpa / len(Students[i][1])
    gpa = round(gpa,2)
    #Students[i][1]['gpa'] = round(gpa,2)
    temp_list = [i,Students[i][0],str(gpa)]
    Output[i] = [Students[i][0],str(gpa)]
    #joiner = "~"
    #l = joiner.join(temp_list)
    #print(l)

for key in sorted(Output.keys()):
    joiner = "~"
    temp_list = [key, Output[key][0], Output[key][1]]       #Output[key][0] == Name, Output[key][1] == gpa
    l = joiner.join(temp_list)
    print(l)
