import socket
import threading

ServerHost = input('IP of server, default(rowisabeast.com): ') or 'rowisabeast.com'
ServerPort = 55555

nickname = input("Choose a nickname: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ServerHost, ServerPort))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print("An error has occurred!")
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