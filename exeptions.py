while True :
 try : 
    x=int(input("entrer le valeur de x "))
    
 except ValueError:
    print ("x is not an integer")
 else :
    print (f"x is {x}")
    break

while True :
 try : 
    x=int(input("entrer le valeur de x "))
    
 except ValueError:
    pass
 else :
    print (f"x is {x}")
    break