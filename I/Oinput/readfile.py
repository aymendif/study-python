noms =[]
with open("names.txt","r") as filereader : #r for read
     lines=filereader.readlines()


with open("names.txt") as nfile:
     for line in sorted(nfile) :
         noms.append(line.rstrip())
print (noms )
