import os
from socket import socket,AF_INET,SOCK_DGRAM

PORT=5418

os.system('@color 70')
os.system('@title AardSocks Outbox')
filea=[each.rstrip() for each in open('servers.conf').readlines()]
alias=filea[0]
servers=filea[1:]
print('Establishing UDP socket ...')
s=socket(AF_INET,SOCK_DGRAM)
socks=[]
for each in servers:
    sig=False
    print(f'{each}: Handshaking with remote socket ...')
    try:
        s.sendto(f'UDP_Hello<{alias}'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
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
        elif c=='cls':
            s.sendto('UDP_CLS<'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),('127.0.0.1',PORT))
        elif c.startswith('file<'):
            fil=[each.rstrip() for each in open(c[5:]).readlines()]
            nm=c.split('\\')[-1]
            print(f'Sending file {nm} ...')
            for each in socks:
                s.sendto(f'UDP_Filetrans<{nm}'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
            for line in fil:
                for each in socks:
                    s.sendto(line.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
            for each in socks:
                s.sendto(f'UDP_EOF'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
        else:
            for each in socks:
                s.sendto(c.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
    except KeyboardInterrupt:
        for each in socks:
            s.sendto('UDP_LocalLogout<'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
            s.sendto('UDP_Logout<'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),(each,PORT))
        print('*'*20)
        print('Disconnecting ...')
        s.close()
        break
