import subprocess

username = 'root'
password = 'root'
database = 'backup'

with open('file.sql','w') as output:
    c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database],stdout=output, shell=True)