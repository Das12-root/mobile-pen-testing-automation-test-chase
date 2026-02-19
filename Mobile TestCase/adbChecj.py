import subprocess
command = 'adb devices'
p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
print('standard output: %s \n error output: %s \n',(stdout,stderr))