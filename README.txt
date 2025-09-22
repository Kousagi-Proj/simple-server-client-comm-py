HOW TO RUN:
Simply run the Server file first, and then the Client side. Simple as that.

The messaging starts after the server and client file are ran. The Server 
file opens up the port to listen to, and the Client file opens up to the 
same port. Both are communicating through it, listening to each other from
opposite sides until they hear something. On the Server side, if it hears 
something from the CLient, it grabs what it hears and sends it back. If the
client hears anything from the server side, it displays it for the user to 
read. The connection is only cut if the Client side sends the message 
"quit", to which both the server and the client cut conection from the 
socket. 