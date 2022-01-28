import requests
import time,os,sys

# clear 
os.system('clear')
# logo
print ('-------------------------------')
print ('[+] Creator : Agunmyyouz')
print ('[+] Youtube : AGUNMYYOUZ')
print ('-------------------------------')
print ('\n[+] nomor di awali 8xxxx cuy')

# Run nomor
nomor = input('[+] Nomor terget : ')
req=requests.get('https://ainxbot-sms.herokuapp.com/api/spamsms',params={'phone':nomor}).text
if 'terkirim' in req:
     print ('[√] Spam Terkirim')
else:
     print ('[!] Spam Gagal')
