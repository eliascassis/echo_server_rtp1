#!/usr/bin/env python3

# Imports socket lib
import socket

# Echo client class definition
class EchoClient():
    """
        Implements the echo client side.
    """
    # Sets server information (host, port)
    def __init__(self, host, port) -> None:
        self._client_socket = socket.socket() # Initializes the client socket
        self._server_host = host # Sets server host
        self._server_port = port # Sets server port 

    # Waits for a connection
    def connect_to_server(self):
        print('Aguardando conexão...')
        # Tries connection
        try:
            self._client_socket.connect((self._server_host, self._server_port)) # connects with the server side
        # Caughts socket exception
        except socket.error as e:
            print(f"{str(e)}\nO servidor está fora do ar. :(")
        # Executes the program 
        else:
            # Gets welcome message from server
            response = self._client_socket.recv(1024).decode('utf-8')
            print(f"Conectado ao servidor de eco: {self._server_host} {self._server_port}")
            print(response)
            print("\nPara enviar mensagens utilize os comandos abaixo:")
            print('(1) echo -m "<MENSAGEM>" -> retorna exatamente a mensagem enviada.')
            print('(2) echo -e "<MENSAGEM>" -> retorna a mensagem enviada com eco.')
            print("\nPara encerrar a conexão digite:")
            print('quit\n')
            # Executes main loop
            try:
                while True:
                    _input = input('> ') # Gets client input
                    _input = _input.strip().lower() # Removes unnecessary whitespaces
                    if _input.strip().lower() == 'quit': # Leaves application
                        raise EOFError
                    self._client_socket.sendall(str.encode(_input)) # Sends message to the server
                    # Receives response from server
                    response = self._client_socket.recv(1024).decode('utf-8') 
                    print(response) # Prints response
            # Finalizes the connection by ctrl + d 
            except EOFError:
                print("\nEco finalizado!")
            # Finalizes the connection by ctrl + c
            except KeyboardInterrupt:
                print("\nEco interrompido!")
            # Some socket error
            except socket.error as e:
                print(str(e))
                print("Erro de conexão!")
            # Closes connection
            finally:
                self._client_socket.close() # Closes

if __name__ == "__main__":
    ec = EchoClient('127.0.0.1',5948) # Creates client
    ec.connect_to_server() # Connects client to the server 
