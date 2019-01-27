import uuid
import time
print ("Starting in")
print ("3")
time.sleep(0.9)
print ("2")
time.sleep(0.9)
print ("1")
time.sleep(0.9)
file = open("emailaddresses.txt","w+")
file = open("emailaddresses.txt","a") 
while 2>1:
    rand = str(uuid.uuid4())
    link = 'fyii.de/trashmail/'
    email_address = '@fyii.de'
    email_link = link+rand[:8]+'.html'
    email = rand[:8]+email_address
    print(email+'\n'+email_link+'\n') 
    file.write(email+'\n'+email_link+'\n') 
    file.write('\n') 
