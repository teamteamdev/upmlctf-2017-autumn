#!/usr/local/bin/python3

import sys
sys.setrecursionlimit(100000)

def fast_power(a, b, mod):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return (fast_power(a, b // 2, mod) ** 2) % mod
    else:
        return (fast_power(a, b - 1, mod) * a) % mod

        
def rsa_decrypt(n, d, ciphertext):
    return fast_power(ciphertext, d, n)

n = 0xd105d12ea49ce8243bf5e8eb6dea31bbb30e413a042bed82f9007ddd89180c1e656e9b02eeae168e4917be2d8b56071d1a9d50b56dd2359f33c839aef0ed49746447b8712ac8a245d27aaeeb4452a87a3abca186e3d8e22a96ba744cedd700cc69028b28fe4144d8d5146b3ebc4123b98f9cf7939a5b2af08897d045f5b3b54cb2636f2cba863ab08de6f043f2af37d7ea7da54e87133d441cecf03cbce06581cba397e326be00e19031d96c6d81c83c855d3586950540a06f8b672ec00b79edc7e0c6a70129a9c7263ec41362a8273f43875ca93547245c6c6d6d4d4ed32b192e6fa7a6b8b01c53cfc9dc8bbab0d3ed51ee82c25a753945d49903607ac1ed31
e = 0x10001

restricted = int(open("/app/restricted.txt").read(), 16)

print('''RSA Decrypt-as-a-Service

Do you think that online crypto is a dream? No! It's just in front of you!
Just try to enter some hex and I'll decipher it for you.
''')

while True:
    print("HEX [in format 0x123abc]: ", end='', flush=True)
    hex = input()
    
    # check 0x
    if not hex.startswith("0x"):
        print("Your input must be in format 0x123abc", flush=True)
        continue
    hex = hex[2:]
    
    # try to parse hex
    try:
        data = int(hex, 16)
    except:
        print("Your input must be in format 0x123abc", flush=True)
        continue
        
    if data == restricted:
        print("I have some secrets and won't tell them to you", flush=True)
        continue
        
    break

d = int(open("/app/d.txt", "r").read(), 16)
decrypted = rsa_decrypt(n, d, data)
print("0x{:x}".format(decrypted))

