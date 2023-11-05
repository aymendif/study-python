noms =[]
with open("names.txt","r") as filereader : #r for read
     lines=filereader.readlines()

for line in lines:
    print (line.rstrip()) #rstrip orgnize the output
 #for line in filereader  other methode to do the ligne 5
    #print (line.rstrip())
with open("names.txt") as nfile:
     for line in sorted(nfile) :
         noms.append(line.rstrip())
print (noms )
with open("students.csv","r") as Sfile:  #use of csv file
     for line in Sfile.readlines():
          #row=line.rstrip().split(",") is not good way to store two values in list insted we use the next ligne
          nom,prenom=line.rstrip().split(",")
          print (f"{nom} {prenom}")