<h1>PLEASE USE IT AS A WISE PERSON</h1>
Was just playing around with python and decided to make this file encryptor.
It can be used wisely to encrypt your files and decrypt when needed. 
Or.
To randomly encrypt a PC.[Files will not be recovered if you do it randomly]

It encrypts all files given in a directory
you can decrypt it with d-dec.py [with your key in play.py]

or you can make play.py encrypt files with random keys
NB: Files cannot be decrypted in this way 

you can modify the script to encrypt all files on the pc
you can read from the comments at the top of the play.py file or use this

at the top (Just to make code neat)
from os.path import expanduser
then:
home = expanduser("~")

so print(home) will be something like
on linux:
	"/root"
on windows:
	"/Users/MyUsername"

then look for this in play.py
for x in os.walk("/YOUR/DIRECTORY/witha / at the end"):

replace this part of the code
("/YOUR/DIRECTORY/witha / at the end")
replace with
(home)
so it should be 
for x in os.walk(home + "/"):

and you are done :)
