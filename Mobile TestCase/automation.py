import os
import re
#file_one = open("AndroidManifest.xml", "r")
#file_one.write('android:allowBackup="true"')
#file_one.close()

# patrn = 'android:allowBackup="true"
patrn = 'hello'
path = input("")
file_one = open(path, "r")
lines = file_one.readlines()
for line in lines:
    if patrn in line:
        print(line)
