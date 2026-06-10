# ​🏹 CTF-Binary_Toolkit

This repository contains my personal collection of Python exploits and scripts developed to solve Software Security challenges during Capture The Flag (CTF) competitions.

The toolkit covers diverse offensive techniques, ranging from memory corruption and Return-Oriented Programming (ROP) to automated binary analysis and dynamic mitigation bypass.
> **🌟 Highlight:** Looking for something more advanced? Check out my standalone exploits: [https://github.com/Vashak/ChaCha20-Linear-Exploit]
[https://github.com/Vashak/Triwizard-Maze-Exploit]

## 🧰 The Arsenal

Below is an index of the exploits available in this toolkit. Files are organized into specific directories based on their cryptographic domain.
| Script | Category | Vulnerability | Description |
| :--- | :--- | :--- | :--- |
| **`basic_bof_shell.py`** | Buffer Overflow | Stack Buffer Overflow | Bypasses an initial input constraint to trigger an out-of-bounds read, injecting a cyclic pattern to hijack the instruction pointer and spawn a shell. |
| **`ret2libc_32bit.py`** | ROP Chains | Stack Buffer Overflow | Performs a 2-stage Return-to-Libc attack (32-bit). Leaks GOT to defeat ASLR, calculates libc base, and redirects execution to `system('/bin/sh')`. |
| **`canary_leak_64bit.py`** | Bypass Mitigations | Off-by-One / Overflow | Overwrites a Stack Canary's null terminator to force the server to leak the remaining 7 bytes, enabling subsequent overflow exploitation. |
| **`fmtstr_got_overwrite.py`** | Format String | Unsafe `printf` | Leverages a format string vulnerability to overwrite `strlen@got` with `system@plt`, hijacking execution flow to spawn a shell. |
| `binary_oracle_bruteforcer.py` | Reverse Engineering | Validation Oracle | Automates local binary execution via `subprocess` to perform a character-by-character brute-force attack, exploiting an early-termination string oracle. |

---

## ⚠️ Disclaimer

*All scripts were developed for educational purposes and authorized CTF competitions. Do not use them against real systems without explicit permission.*
