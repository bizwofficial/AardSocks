# Thanks for using AardSocks!
This is a light software based on UDP protocol helping you chat on LAN.

## Compile  
Before using, you need to compile AardSocks first. __Python 3.6 or later needed.__ Open shell in the root directory and type:  
```  
  cd lib  
  python -O -m py_compile AardSocks_Launcher.py  \n
  python -O -m py_compile Aard_send.py  \n
  python -O -m py_compile Aard_receive.py  \n
```
Then move the three file in folder "pycache" to the lib folder, and rename them to:  
```
  AardSocks_Launcher.pyc  
  Aard_send.pyc  
  Aard_receive.pyc  
 ```
After doing this, you need to use your G++ to compile the AardSocks.cpp in the root directory.

## Config  
You need to add the ip address of computers you want to connect with to "servers.conf" in lib folder like this:  
```
  127.0.0.1  
  192.168.0.1  
  180.76.76.76  
```

## Run  
To run AardSocks, simply double-click "AardSocks.exe".  
  
## Reconnect  
If you want to reconnect to the servers, please type this:  
```
  UDP_Reco<  
```

## Easy-to-Use  
For a built version, [click here](https://codeload.github.com/bizwofficial/AardSocks/zip/Latest).__Python 3.6 needed.__  

## Why My AardSocks Crash?  
- Check if your Python is added to PATH.  
- Check if the source code are compiled.  

