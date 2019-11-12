import os
from socket import *

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
        else:
            if sv[0] in trusted_servers:
                print(f'{name[sv[0]]}: {c}')
            else:
                pass
    except KeyboardInterrupt:
        print('*'*20)
        print('Disconnecting ...')
        s.close()
        break
