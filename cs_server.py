import threading
import socket

host = '127.0.0.1'
#local host to ahhh

port = 5555
#eto port mo syempre
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()



client = []
nickname = []

def broadcast(message):
    for client in clients:
        client.send(message)
        

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            #yung 1024 bytes po sya okie??
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nickname[index]
            broadcast(f'{nickname} left the chat' .encode('ascii'))
            nickname.remove(nickname)
            break
 
 
def receive():
    while True:
        client, address = server.accept()
        print("connected with {str(address)}") 
        
        client.send('NICK' .encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the server!' .ecode('ascii'))
        
        thread = threading.Thread(target= handle, args=(client,))
        thread.start()
        
print("Nakikinis sayo ang server")
receive()import threading
import socket

host = '127.0.0.1'
#local host to ahhh

port = 44444
#eto port mo syempre
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()



client = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
        

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            #yung 1024 bytes po sya okie??
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nicknames = nickname[index]
            broadcast(f'{nickname} left the chat' .encode('ascii'))
            nicknames.remove(nickname)
            break
 
 
def receive():
    while True:
        client, address = server.accept()
        print("connected with {str(address)}") 
        
        client.send('NICK' .encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append()
        
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the server!' .ecode('ascii'))
        
        thread = threading.Thread(target= handle, args=(client,))
        thread.start()
        
print("Nakikinis sayo ang server")
receive()
