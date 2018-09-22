#### socket.error: [Errno 48] Address already in use
#### https://stackoverflow.com/questions/19071512/socket-error-errno-48-address-already-in-use
### EXCERPT
You already have a process bound to the default port (8000). If you already ran the same module before, it is most likely that process still bound to the port. Try and locate the other process first:

$ ps -fA | grep python
  501 81651 12648   0  9:53PM ttys000    0:00.16 python -m SimpleHTTPServer
The command arguments are included, so you can spot the one running SimpleHTTPServer if more than one python process is active. You may want to test if http://localhost:8000/ still shows a directory listing for local files.

The second number is the process number; stop the server by sending it a signal:

kill 81651
