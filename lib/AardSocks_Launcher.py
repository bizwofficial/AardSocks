import os,time

ppt='python'

os.system('@color f0')
print('AardSocks v1.3.19b')
print('\n')
print('*'*20)
print('Launching AardSocks ...')
time.sleep(3)

os.system(f'@start {ppt} Aard_receive.pyc')
os.system(f'@start {ppt} Aard_send.pyc')
