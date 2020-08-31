import email
import re
import tkinter
import base64
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from bs4 import BeautifulSoup


"""splits urls from the msg"""
def souper(html_content):
    return_string=""
    soup=BeautifulSoup(str(html_content), "html.parser")
    pretty=soup.prettify()
    link_list=soup.find_all(href=re.compile("\S*"))
    url_list=[]
    return_string="<h3>urls</h3><ol>"
    for item in link_list:
        url_list.append(item.get("href"))
        return_string=return_string+"<li>"+str(item.get("href"))+"</li>"
    print(url_list)
    return_string=return_string+"</ol>"
    return return_string


"""Splits content of msg"""
def split_content(content):
    return_string=""
    if(content.get_content_type()=="multipart/alternative"):
        walker= content.walk()
        for its in walker:
            #print(its.get_payload())
            return_string=souper(its.get_payload())

        souper(its)
    elif((content.get_content_type()=="text/html") | (content.get_content_type()=="text/plain")):
        walker= content.walk()
        for its in walker:
            #print(its.get_payload())
            return_string=souper(its.get_payload())
    return return_string



"""Prints Mail details from Mail Header"""

def mail_details(maile):
    html_string="<ul>"
    str_split=str(maile["Authentication-Results"]).split(" ")
    #print(str_split["spf"]+"\n"+str_split["dkim"])
    for item in str_split:
        if(re.search("dkim\w*", item)!=None) | (re.search("spf\w*", item)!=None) | (re.search("smtp.mailfrom\w*", item)!=None) :
            out_split=item.split("=")
            print(out_split[0].upper()+" :" + out_split[1])
            html_string=html_string+"<li>"+ out_split[0].upper() + ":" + out_split[1] + "</li>"
    Header_from=str(maile["From"])
    To=str(maile["To"])
    Subject= str(maile["Subject"])
    Message_ID =str(maile["Message-ID"])
    Date= str(maile["Date"])
    X_Sender=str(maile["X-Sender"])
    X_Mailer= str(maile["X-Mailer"])
    Delivered_To = str(maile["Delivered-To"])
    Forwarded= str(maile["Auto-Submitted"])
    dict_1={"Header_from": Header_from, "To": To,"Message_ID": Message_ID, "Date" : Date,"X_Sender" : X_Sender, "X_Mailer": X_Mailer, "Delivered_To": Delivered_To,"Forwarded": Forwarded}

    for item in dict_1:
        html_string=html_string+"<li>"+ item + ":" + dict_1[item] + "</li>"

    html_string=html_string+"</ul>"

    #print(maile["Received"])
    print("PATH taken by MAIL")
    Received_List=[]
    RL=0
    for item in maile.items():
        if(item[0]=="Received"):
            Received_List.append(item[1])
            RL=RL+1
    LL=0
    for item in Received_List:
        print("PATH_Value : "+ str(len(Received_List)-LL)+ "\n")
        IP=re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",item)
        if(IP!=None):
            print(IP[0])
        print(dir(IP))
        print("______________________________________")
        print(item + "\n")
        LL=LL+1

    return html_string


def reader(maile):
    html_string=mail_details(maile)
    return_string=""
    all_items=maile.get_payload()
    print(all_items)
    for item in all_items:
        return_string=split_content(item)
        print("__________________________________________________________________________________________")

    content_type=maile.get_content_type()
    return html_string+return_string






    file.close()

#filename="SC.eml"
#reader(filename)
