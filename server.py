import socket
import threading

host = '127.0.0.1'
port = 27272
text_to_person = []
clients = []
nicks = []


def chat(client):
    while True:
        try:
            message = client.recv(1024)
            text_to_person.append(message)
            for j in clients:
                j.send(message)
            file = open('log.txt', mode='a')
            file.write(str(message))
            file.write('\n')
            file.close()
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            nicks.remove(nickname)
            for i in clients:
                i.send(f'{nickname} left!'.encode())

            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

while True:
    client, address = server.accept()
    print(f"Connect with {str(address)}")
    client.send('write_name'.encode())
    nickname = client.recv(1024).decode()
    nicks.append(nickname)
    clients.append(client)
    print("Подлючен {}".format(nickname))
    for client in clients:
        client.send(f"{nickname} подключился".encode())
    client.send('Соединение было установлено'.encode())
    thread = threading.Thread(target=chat, args=(client,))
    thread.start()
