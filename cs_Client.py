import threading
import socket

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4444))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
             print("Error occured syempre ano aasahan mo?")
             client.close()
             break
             
def write():
    while True:
        message = f'{nickname}: {input(" ")}'
        client.send(message.encode('ascii'))
receive_threads = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()