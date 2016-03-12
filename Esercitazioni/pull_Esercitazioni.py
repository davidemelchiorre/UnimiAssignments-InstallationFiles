import subprocess

subprocess.call('ls -l', shell=True)
subprocess.call('git pull https://github.com/davidemelchiorre/UnimiAssignment-Esercitazioni.git', shell=True)
subprocess.call('ls -l', shell=True)
print "pulled into Esercitazioni"
