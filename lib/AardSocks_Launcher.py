import os,time

ppt='python'
print('AardSocks v1.0.19a')
print('\n')
print('*'*20)
print('Launching AardSocks ...')
time.sleep(3)

os.system(f'@start {ppt} Aard_receive.pyc')
os.system(f'@start {ppt} Aard_send.pyc')
