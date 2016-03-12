import subprocess

print ""
print "Starting Cli Interface..."
print "Press CTRL+C to terminate"
print ""
print "-------------------------Cli Interface-------------------------"
print ""
while 1:
    comando = raw_input(">")
    
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
        subprocess.call('rm -r mydir', shell=True)
        subprocess.call('git clone https://github.com/davidemelchiorre/UnimiAssignment-Esercitazioni.git Esercitazioni', shell=True)
        subprocess.call('ls -l', shell=True)
        print "cloned into Esercitazioni"
        print "-----------------------------------------------"
        print ""
