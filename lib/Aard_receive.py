import os
from socket import *

PORT=5418
os.system('@title AardSocks Inbox')

servers=[each.rstrip() for each in open('servers.conf').readlines()]
trusted_servers=[]
print('Establishing UDP socket ...')
s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',PORT))
print(f'\nPort {PORT}, ready to receive.')
print('*'*20)

while True:
    try:
        ct,sv=s.recvfrom(140)
        c=ct.decode('ascii').encode(encoding='utf-8').decode('unicode_escape')
        if 'UDP_Logout<' in c:
            print(f'>>{sv[0]} Logged out.')
        elif 'UDP_Hello<' in c:
            print(f'>>Handshaking with {sv[0]}:{sv[1]} ...')
            try:
                s.sendto(f'UDP_Hello<{sv[0]}'.encode('unicode_escape').decode(encoding='utf-8').encode('ascii'),sv)
            except:
                print(f'>>Failed in handshaking with {sv[0]}:{sv[1]}.')
            else:
                trusted_servers.append(sv[0])
                print(f'>>Finished handshaking with {sv[0]}:{sv[1]}.')
        else:
            if sv[0] in trusted_servers:
                print(f'{sv[0]}: {c}')
            else:
                pass
    except KeyboardInterrupt:
        print('*'*20)
        print('Disconnecting ...')
        s.close()
        break
