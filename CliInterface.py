import subprocess
import threading
import socket
comando="Hello World"

host=''
port = 9696
buflen=1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

def server_function():
    global comando
    while 1:
        client, buf = server.accept()
        #-------------------------
        buf = client.recv(buflen)
        if not buf:break
        comando=buf.decode('utf-8')
        print ">",comando
        client.send(bytes(0))
        if comando=="quit":
            client.close()
            
def input_function():
    global comando
    while 1:
        comando = raw_input(">")

server_thread=threading.Thread(name='server_thread', target=server_function)
input_thread=threading.Thread(name='input_thread', target=input_function)

server_thread.start()
input_thread.start()

print ""
print "Starting Cli Interface..."
print "Press CTRL+C to terminate"
print ""
print "-------------------------Cli Interface-------------------------"
print ""
while 1:
    if comando=="start":
        print ""
        print "-----------------Start routine-----------------"
        try:
            if proc is None:
                print("Info>> Starting program...")
                proc=subprocess.Popen(["jupyter","notebook"])
            else:
                print("Info>> Program is already running")
        except NameError:
            print("Info>> Starting program...")
            proc=subprocess.Popen(["jupyter","notebook"])
        print "-----------------------------------------------"
        print ""
  
    if comando=="stop":
        print ""
        print "-----------------Stop routine------------------"
        try:
            if proc is not None:
                print(proc)
                print("Info>> Stopping program...")
                proc.kill()
                proc=None
            else:
                print("Info>> Program is not running")
        except NameError:
            print("Info>> Program is not running")
        print "-----------------------------------------------"
        print ""
        
    if comando=="get":
        print ""
        print "--------------Getting Notebooks----------------"
        print "Cloning into Esercitazioni..."
        subprocess.call('rm -r Esercitazioni', shell=True)
        subprocess.call('git clone https://github.com/davidemelchiorre/UnimiAssignment-Esercitazioni.git Esercitazioni', shell=True)
        subprocess.call('ls -l', shell=True)
        print "cloned into Esercitazioni"
        print "-----------------------------------------------"
        print ""
    
    if comando=="quit":
        server.close()
        
    comando="Hello World"
