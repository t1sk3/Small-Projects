import socket
import threading

nickname = input("Choose a nickname: ")

#host = '192.168.68.117'
host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                if not message.startswith(nickname):
                    print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
