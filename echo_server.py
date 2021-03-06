#!/usr/bin/env python3

### Imports 
import socket
from _thread import *
from re import sub, search
from sys import argv

# Echo server class definition
class EchoServer():
    """
        Implements the echo server side.
    """
    def __init__(self, number_of_threads) -> None:
        self._HOST = '127.0.0.1' # server ip
        self._PORT = 5948 # server port
        self._num_threads = 0 # number of threads alocated
        self._server_socket = socket.socket() # Initializes the server socket
        self._max_threads = int(number_of_threads) # supported number of threads 

    # Binds socket to server
    def bind_socket_to_server(self):
        try:
            self._server_socket.bind((self._HOST, self._PORT)) # Binds
        except socket.error as e:
            print(str(e))

    # Sets the maximum number of the queue of pending connections and listens
    def set_max_threads(self):
        try:
            self._server_socket.listen(int(self._max_threads*.1)) # Listens (backlog queue size)
        except socket.error as e:
            print(str(e))

    # Echoing the message according to the position of word 
    # Words in the final of the string echoes more
    def echoing_message(self, data):
        data = data.split()
        for i in range(-1,-len(data)//2-1,-1):
            data[i] += ' '
            data[i] *= (i+4)*(1 if i+4 > 0 else -1)
        data = sub(r' +',' ',' '.join(data))
        return data

    # Sets threads for a client 
    def threaded_client(self, connection):
        try:
            # Sends welcome message or closes connection by thread limit
            if self._num_threads <= self._max_threads:
                connection.send(str.encode('Seja bem-vindo! Digite uma mensagem e a veja ecoar.'))
            else:
                connection.send(str.encode('%'))
                raise ValueError(f"Servidor cheio!\nConexão encerrada com {connection.getpeername()}")
            while True:
                data = connection.recv(1024).decode('utf-8').lower() # Receives message from client 
                # Closes connection if no data was send in the message or the client quits
                if not data or data == 'quit':
                    raise ValueError(f"Conexão encerrada com {connection.getpeername()}")
                else:
                    # Searches for correct pattern in command
                    data = search(r'^(echo) (-[m|e]) \"([^\"]*)\"$',data)
                    if data is not None:
                        data = data.groups()
                        command = data[0]
                        parameter = data[1]
                        message = data[2]
                    else:
                        command = parameter = message = ''
                    if not message or not parameter or not command:
                        alert = 'Por favor, informe o comando corretamente:\necho -m "<mensagem>"\necho -e "<mensagem>"\nquit\n'
                        connection.sendall(str.encode(alert)) # Sends alert to client
                        continue
                    data = message
                    result = data if parameter == "-m" else self.echoing_message(data)
                response = 'Servidor: ' + result # Echoes the message
                connection.sendall(str.encode(response)) # Sends reponse to client
        except socket.error as e:
            print(str(e))
        except ValueError as e:
            print(str(e))
        finally:
            self._num_threads -= 1
            connection.close() # Closes the connection

    # Runs echo server 
    def run_server(self):
        print("Servidor aguardando...")
        # Executes main loop
        try:
            while True:
                client, address = self._server_socket.accept() # Accepts connection from client
                print(f"Conectado a: {address[0]}:{address[1]}") # Prints client information
                self._num_threads += 1 # Increments the number of threads
                thread = start_new_thread(self.threaded_client, (client,)) # Starts new thread
                print(f"Thread id: {thread}") # Prints thread id
                print(f"Número de threads: {self._num_threads}")
        # Finalizes the connection by ctrl + d 
        except EOFError:
            print("\nEco finalizado!")
        # Finalizes the connection by ctrl + c
        except KeyboardInterrupt:
            print("\nEco interrompido!")
        # Closes connection
        finally:
            self._server_socket.close() # Closes 

if __name__ == "__main__":
    if len(argv) != 2:
        print("Por favor, informe somente o número máximo de threads desejado:")
        print("Comando: ./echo_server.py <número de threads>")
    else:
        es = EchoServer(argv[1]) # Creates server 
        es.bind_socket_to_server() # Binds server's host and port
        es.set_max_threads() # Sets max number of threads
        es.run_server() # Runs the server 
