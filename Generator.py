import uuid
import time
import os
print ("Starting in")
print ("3")
time.sleep(0.9)
print ("2")
time.sleep(0.9)
print ("1")
time.sleep(0.9)
exists = os.path.isfile('emailaddresses.txt')
if exists:
    file = open("emailaddresses.txt","a")
else:
    file = open("emailaddresses.txt","w+") 


while 2>1:
    rand = str(uuid.uuid4())
    link = 'fyii.de/trashmail/'
    email_address = '@fyii.de'
    email_link = link+rand[:8]+'.html'
    email = rand[:8]+email_address
    print(email+'\n'+email_link+'\n') 
    file.write(email+'\n'+email_link+'\n') 
    file.write('\n') 

