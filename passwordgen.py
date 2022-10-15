import random
import string


characters =list(string.ascii_letters + string.digits + "@#$%^&*()" ) 

def password_generator():
  
  password_length = int(input("How long would you like your password to be? "))
  
  random.shuffle(characters)
  
  password = []
  
  
  for _ in range(password_length):
 
    # password.( random.choice(characters))
    new_pas = random.choice(characters)
    
    random.shuffle(new_pas)
    
    password =(new_pas)
    
    print(password, end="")
    
    
    
option = input("do you want to generate passsword? (yes or no): ")
    
if option =="yes":
 password_generator()
      
elif option == "no":
     
     quit()
else:
      print("invalid input please input yes or no")
      quit()
   
    
  

    