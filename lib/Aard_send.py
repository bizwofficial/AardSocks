import os
from socket import *

PORT=5418

os.system('@title AardSocks Outbox')
servers=[each.rstrip() for each in open('servers.conf').readlines()]
print('Establishing UDP socket ...')
s=socket(AF_INET,SOCK_DGRAM)
socks=[]
for each in servers:
    sig=False
    print(f'{each}: Handshaking with remote socket ...')
    try:
        s.sendto(f'UDP_Hello<{each}'.encode('ascii'),(each,PORT))
    except:
        pass
    else:
        sig=True
    if sig==True:
        print(f'{each}: Connected to port {PORT}.')
        socks.append(each)
    else:
        print(f'{each}: Connection failed.')

print(f'\n{len(socks)} of {len(servers)} connected.')
print('*'*20)

while True:
    try:
        c=input('localhost: ')
        if c=='UDP_Reco<':
            s.close()
            os.system('@start python Aard_send.pyc')
            break
        else:
            for each in socks:
                s.sendto(c.encode('ascii'),(each,PORT))
    except KeyboardInterrupt:
        for each in socks:
            s.sendto('UDP_Logout<'.encode('ascii'),(each,PORT))
        print('*'*20)
        print('Disconnecting ...')
        s.close()
        break
