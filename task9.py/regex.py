# regex to validate  email address#

import re
pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-z]{2,4}$'

emailId="theju@gmail.com"

if re.match(pattern,emailId):
    print(f"{emailId} is valid.")
else:
    print (f"{emailId} is invalid.")    


    #To validate the mobile no of bangladesh#

    import re
    def bangladesh_number(mobile_number):
    
    pattern = r'^\+880 1\d{2}  \d{6}$'

    if re.match (pattern,mobile_number):
        return true
    else:
        return false

    check="+880 122 987655"  

    if bangladesh_number (check):
        print("valid mobile number")
    else:
         print("not valid mobile number")   


   #   To validate the usa phone number

      import re
    def match_usa_phone_number(phone_number):
    
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

    if re.match (pattern,phone_number):
        return true
    else:
        return false
    check_number="(123) 456 7890"        
    if match_usa_phone _number (check_number):
        print("valid phone number")
    else:
         print("phone number is not valid")   


      #  to validate password
     import re

     def validate_password(password):
     pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#4%^&*()-_=+{};:|'""

     if re.match(pattern, password):
         return true
     else:
         return false

    check_password="sugu19@"  
    
    if validate_password(check_password):
        print("password is valid") 
    else:
        print("password is invalid")               
  
         