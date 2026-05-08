class1 =  ['suresh' , 'mahesh' , 'sangeetha' , 'sushil' , 'boresh']
class2 = ['ram' , 'sham' , 'mahesh' , 'boresh']

counter = 0
common_names = []
for name in class1:
    for name2 in class2:
        if name == name2 :
            common_names.append(name2)
            counter  += 1


print("Common students:", common_names)
print("Number of common students:" , counter)
    

    