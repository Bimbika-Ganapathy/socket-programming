import socket

host='127.0.0.0'
port=8500

lk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

lk.bind(port,host)

if TRUE:
    lk.listen()
    client,address=lk.accept()
    response=client.recv(1024)




    print("The text is"+response.decode())
    print("the text in uppercase is"+ (response.decode()).upper())

    client.close()
