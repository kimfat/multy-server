import socket
import threading


def checker():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'write_name':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("Доступ отсутстует")
            client.close()
            break


def name():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode())


nickname = input("Введите ваше имя: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 27272))
get_server = threading.Thread(target=checker())
get_server.start()
give_to_server = threading.Thread(target=name())
give_to_server.start()
