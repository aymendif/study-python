#open technique,
names=[]
for _ in range(3):
     names.append(input("what is your name ")) #append =ajouter element dans la list "names"
for name in sorted(names):  #sorted = triee les element dans la list en ordre alphabitique
    print (f"hello , {name}")
#for i in range(len(names)):
 #    file =open("names.txt","a")
  #   file.write(f"{i}-{names[i]}\n")
#file.close()
#for better code and to close the file automaticly is better to use this code 
for i in range(len(names)):
    with open("names.txt","a") as file :  # a for append to the file 
         file.write(f"hello,{names[i]}\n")
         
# how to read a file 

   