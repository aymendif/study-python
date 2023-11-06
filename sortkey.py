students=[]
with open ("students.csv") as file :
    for line in file :
        name,prenom = line.rstrip().split(",")
        student = {"nom":name,"prenom":prenom}
        students.append(student)
def get_name (student):
    return student["nom"]
for student in sorted(students, key=get_name): # the key is a reference for order the values
    print (student)
    print(f"nom est {student['nom']} et le prenom est {student['prenom']}")
