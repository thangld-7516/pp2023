print("-----------------------------------------------------")
print("option 1: enter number of student")
print("option 2: enter student info")
print("option 3: enter number of course")
print("option 4: enter course info")
print("option 5: display student list")
print("option 6: display course list")
print("option 7: enter mark of student in the course")
print("option 8: display the mark of student in the course")
print("option 9: exit")
print("-----------------------------------------------------")
 
studentinfo = []
courseinfo = []
markinput = []

while 0 == 0:
	opt = input("enter your option") 
	match opt:
		case "1":
            		
			numofstudent = input("Enter number of student in a class:")
			print("number of student in a class:" + numofstudent)
		case "2":
			IDstudent = input("Enter ID student:")
			studentinfo.append(IDstudent) 
			namestudent = input("Enter name of student:")
			studentinfo.append(namestudent)
			DOB = input("Enter DOB of student:")
			studentinfo.append(DOB)
			numarr1 = len(studentinfo);
		case "3":
			numofcourse = input("Enter number of course:")
			print(numofcourse)
		case "4":
			IDcourse = input("Enter ID course:")
			studentinfo.append(IDcourse) 
			namecourse = input("Enter name of course:")
			studentinfo.append(namecourse)
			numarr2 = len(courseinfo);
		case "5":
			for x in range(0,numarr1,3):
				print("IDstudent:"+studentinfo[x] ,"namestudent:"+studentinfo[x+1], "DOB:"+studentinfo[x+2])
		case "6":
			for x in range(0,numarr2,2):
				print("IDcourse:"+courseinfo[x] ,"namecourse:"+courseinfo[x+1])
		case "7":
			mark = input("enter the mark")
			markinput.append(mark)
			numarr3 = len(markinput);
		case "8":
			for x in range(0,numarr3):
				for y in range(0,numarr1,3):
					print("ID:"+studentinfo[y],"name:"+studentinfo[y+1],"mark:"+markinput[x])
		case "9":
			exit()
