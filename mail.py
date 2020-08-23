import email
import re

file=open("FREE.eml","rb")
file_read=file.read()
maile=email.message_from_bytes(file_read)

#print(maile._headers)
for item in  maile._headers:
    print(item)

print("_______________________________________")
#print(maile["Authentication-Results"])
str_split=maile["Authentication-Results"].split(" ")
#print(str_split["spf"]+"\n"+str_split["dkim"])
for item in str_split:
    if(re.search("dkim\w*", item)!=None) | (re.search("spf\w*", item)!=None) | (re.search("smtp.mailfrom\w*", item)!=None) :
        print(item)
print("HeaderFrom :"+ maile["From"])
print("TO :"+ maile["To"])
print("Subject :"+ maile["Subject"])
print("Message-ID :"+ maile["Message-ID"])
print("Date :"+ maile["Date"])
print("X-Sender :" + str(maile["X-Sender"]))
#print(maile["Received"])
print("PATH taken by MAIL")
Received_List=[]
RL=0
for item in maile.items():
    if(item[0]=="Received"):
        Received_List.append(item[1])
        RL=RL+1

for item in Received_List:
    print(item)







file.close()
