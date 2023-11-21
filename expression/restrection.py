import re
email = input ("entrer votre mail")
if re.search (r"^A+.*@?.+\.edu$",email):
    print ("valide ")
else : 
    print ("invalide")
    