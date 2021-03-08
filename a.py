import subprocess
import random
import sys
import time
import os

done = False

subprocess.run("python2 b.py",shell=True,check=True)
subprocess.run("python c.py",shell=True,check=True)

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

print(" ")
print(" ")
mengetik('Terimakasih Telah,Memakai\nScript Arimengen\nDan\nJangan Lupa Subscribe')

time.sleep(0.9)
import os
os.system("clear")

time.sleep(0.9)
os.system("php rhawk.php")



