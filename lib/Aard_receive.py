import os
from socket import socket,AF_INET,SOCK_DGRAM
import time

def gettime():
    a=time.localtime()
    return (a.tm_year,a.tm_mon,a.tm_mday,a.tm_hour,a.tm_min)

PORT=5418
os.system('@color f0')
os.system('@title AardSocks Inbox')

filea=[each.rstrip() for each in open('servers.conf').readlines()]
alias=filea[0]
servers=filea[1:]
trusted_servers=[]
print('Establishing UDP socket ...')
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',PORT))
print(f'\nPort {PORT}, ready to receive.')
print('*'*20)
name={'127.0.0.1':'Me'}
lctm=gettime()

while True:
    try:
        ct,sv=s.recvfrom(140)
        c=ct.decode('ascii').encode(encoding='utf-8').decode('unicode_escape')
        if 'UDP_Logout<' in c:
            print(f'>>{sv[0]} Logged out.')
        elif 'UDP_Hello<' in c:
            print(f'>>Handshaking with {sv[0]}:{sv[1]} ...')
            name[sv[0]]=c[10:]
            try:
                s.sendto(f'UDP_Hello<{alias}'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),sv)
            except:
                print(f'>>Failed in handshaking with {sv[0]}:{sv[1]}.')
            else:
                trusted_servers.append(sv[0])
                print(f'>>Finished handshaking with {sv[0]}:{sv[1]}.')
        elif c.startswith('UDP_Filetrans<'):
            nm=c[14:]
            fil=open(f'..\\Inbox\\{nm}','w')
            sig=True
            while sig:
                ct1,sv1=s.recvfrom(140)
                if sv1==sv:
                    c1=ct1.decode('ascii').encode(encoding='utf-8').decode('unicode_escape')
                    if c1=='UDP_EOF':
                        fil.close()
                        sig=False
                    else:
                        print(c1,file=fil)
            print(f'>>1 file received: {nm}')

        else:
            if sv[0] in trusted_servers:
                if gettime()!=lctm:
                    lctm=gettime()
                    print('*'*15,f'{lctm[3]}:{lctm[4]}','*'*15,sep='')
                print(f'{name[sv[0]]}: {c}')
            else:
                pass
    except KeyboardInterrupt:
        print('*'*20)
        print('Disconnecting ...')
        s.close()
        break
