'''
Created on Aug 5, 2018

@author: Zeyad Abuamer
'''
import requests

user_data = {} #Example: {'user':'admin','password':'admin'}
reboot_data = {} #Example: {'reboot':'true'}
headers = {} #Example: {'Content-Type': 'application/x-www-form-urlencoded'} 
login_url = '' #Example: http://192.168.1.1/api/user/login
reboot_url = '' #Example: http://192.168.1.1/api/user/reboot

def reboot_router():
    print("~Loading~")
    '''
    Open a session and login then do the reboot request
    If an exception happens user will be prompted to retry or exit
    '''
    with requests.Session() as s:
        try:
            s.post(login_url , data = user_data, headers = headers)
            s.post(reboot_url, data = reboot_data , headers = headers)
            print("Success!")
        except Exception:
            print("An exception was caught, do you want to retry again? Answer Y or N")
            answer = input()
            if answer.lower() == 'y':
                reboot_router()
            else:
                print("Sorry for the error!")    
    
    
reboot_router()    
    
    