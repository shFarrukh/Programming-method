import os, shutil,logging
import sys
import threading
import time

def decrypt(text,s):
    result = ""
    for i in range(len(text)-1):
        char=text[i]
        if (char.isupper()):
            result += chr((ord(char)-65+26-s) % 26+65)
        elif (ord(char) >= 48 and ord(char) <= 58):
            result += chr((ord(char)-48+10-s) % 10+48)
        else:
            result += chr((ord(char)-97 + 26 - s) % 26 + 97)
    return result

def protector(password_checker):
	logging.basicConfig(level=logging.DEBUG)
	logging.debug('the program is running ')

	f = open('C:/Users/Farrukh99/Desktop/subjects/coding/TIMP Lab1/template.tbl', 'r')
	psw = f.readline()

	y = list()
	n = list()
	for line in f:
		a = str(line.strip())
		if os.path.isfile(a):
			y.append(a)
		else:
			n.append(a)
	if  os.path.isdir('tmp'):
		shutil.rmtree('tmp', ignore_errors = True)
	os.mkdir('tmp')


	for f in y:
		shutil.copy(f, 'tmp')
	logging.debug('Copies of the files created ')


	to = os.listdir(path=".")

	e = True
	while password_checker.is_alive(): # e==True:
		for f in n:
			if os.path.isfile(f):
				os.remove(f)
				logging.debug(f' {f} Deleted')
		t = os.listdir(path=".")
		if len(t)!=len(to):
			for f in y:
				if f not in t:
					shutil.copy(f'tmp/{f}', f)
					logging.debug(f'{f} restored ')
		else:
			for f in t:
				if f not in to:
					new = f
			for f in y:
				if f not in t:
					os.remove(new)
					shutil.copy(f'tmp/{f}', f)
					#logging.debug(f'Файл {f} переименован обратно из фай {new}')
		c = True
		for f in n:
			if os.path.isfile(f):
				c = False
		for f in y:
			if f not in t:
				c = False
		if c and t!= to:
			to = t
			#logging.debug('Change in other files, commit the change in the file list ')

def protector_killer():
	password = "Hello"
	f = open('template.tbl', 'r')
	psw = f.readline()
	password=decrypt(psw,13)
	while input("Enter password:") != password:
		print("Incorrect password!")
	print("Correct password was entered. File guard is shutting down!")
	print("Bye")
	sys.exit()

password_checker = threading.Thread(target=protector_killer, args=())
password_checker.start()
protector(password_checker)







