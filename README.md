# 🗡️ CTF-Binary_Toolkit

This repository contains my personal collection of Python exploits and scripts developed to solve Cryptography and Hardware challenges during Capture The Flag (CTF) competitions.

The toolkit covers a variety of attack vectors, from breaking classic algorithms (RSA, AES) to exploiting hardware vulnerabilities (LFSR) and side-channel data.

> **🌟 Highlight:** Looking for something more advanced? Check out my standalone exploits: [https://github.com/Vashak/ChaCha20-Linear-Exploit]
[https://github.com/Vashak/Triwizard-Maze-Exploit]

## 🧰 The Arsenal

Below is an index of the exploits available in this toolkit. Files are organized into specific directories based on their cryptographic domain.
| Script | Category | Vulnerability | Description |
| :--- | :--- | :--- | :--- |
| `basic_bof_shell.py` | Buffer Overflow | Stack Buffer Overflow | Bypasses an initial input constraint to trigger an out-of-bounds read, injecting a cyclic pattern to hijack the instruction pointer and spawn a shell. |

---

## ⚠️ Disclaimer

*All scripts were developed for educational purposes and authorized CTF competitions. Do not use them against real systems without explicit permission.*
