class1 = ['mahesh' , 'suresh' , 'sangeetha' , 'sushil']
class2 = ['ram' , 'sham' , 'mahesh' , 'boresh']

counter = 0
common_names = []
for name in class1:
    for name2 in class2:
        if name == name2 and name not in common_names:
            common_names.append(name)
            counter  += 1


print("Common students:", common_names)
print("Number of common students: " , counter)
    

    