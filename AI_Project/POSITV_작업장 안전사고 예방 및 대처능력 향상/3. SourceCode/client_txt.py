#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python3

import socket

HOST = '141.223.140.38'
PORT = 9990

# 소켓 객체를 생성합니다. 
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 
# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다. 
client_socket.connect((HOST, PORT))
 
# 메시지를 전송합니다. 
 
 
# 메시지를 수신합니다.
 
copy ='0'
 
while True:
 
    data = client_socket.recv(1024)
 
    if copy == data:
        continue
    else:
        print('서버로 부터 받은 메모장의 내용', repr(data.decode()))
        
        copy = data
 
        f = open('detect.txt', 'w')
        f.write(data.decode())
        f.close()
    
 
# 소켓을 닫습니다.
client_socket.close()

