# first import socket library
import socket

#now create a socket object
s=socket.socket()
print("socket successfully created")

#reserve a port in your computer it can be anything
port=12345

#NExt bind to the port
#we have not bind anything in the ip field,instead we have inputed an empty string
#this would make server listen to the request coming from other computers on the network
print("socket binded to %s"%(port))

#now put the port in listening mode
s.listen(5)
print("socket is listening")

#a infinite loop unless we interrupt or an error occurs
while True:

    #establish a connection with client
    c, addr = s.accept()
    print("Got connection from ",addr)

    #send a thanku msg to the client,encoding to send bytes
    c.send("Thank u for connecting".encode())

    #close the connection with the client
    c.close()

    #breaking once the connection is closed
    break


