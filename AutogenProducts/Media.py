import requests
import base64
import os
import json




def Media(Url,ProductName):
    #add username that in admin board
    user="User_Name_admin_poard"
    pswd="Pass_admin_board"
    url="https://url/wp-json/wp/v2/media/"

    auth = user + ":"+pswd

    token = base64.b64encode(auth.encode("utf-8"))
    

    header = {"Authorization":"basic "+ token.decode()}
    files = {"file" : open(Url,'rb')}
    data= {"title":ProductName,
        "alt_text" : ProductName}

    r = requests.post(url,headers=header,files=files,data=data)
    ID =  r.json()['id']

    return ID 
