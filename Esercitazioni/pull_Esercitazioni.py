import subprocess

print "-----------------Pulling Repository------------------"
subprocess.call('cd Esercitazioni', shell=True)
subprocess.call('ls -l', shell=True)
subprocess.call('git pull https://github.com/davidemelchiorre/UnimiAssignment-Esercitazioni.git', shell=True)
print "-----------------------------------------------"