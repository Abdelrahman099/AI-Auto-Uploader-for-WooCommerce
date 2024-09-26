import requests
import base64
import os
import json




def Media(Url,ProductName):
    user="abdelrahman"
    pswd="T9RW G2tS QHx2 VTLa mAtL 1OrH"
    url="https://tossonlibrary.com/wp-json/wp/v2/media/"

    auth = user + ":"+pswd

    token = base64.b64encode(auth.encode("utf-8"))
    

    header = {"Authorization":"basic "+ token.decode()}
    files = {"file" : open(Url,'rb')}
    data= {"title":ProductName,
        "alt_text" : ProductName}

    r = requests.post(url,headers=header,files=files,data=data)
    ID =  r.json()['id']

    return ID 
