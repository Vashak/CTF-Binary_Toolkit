"""
===========================================================================
🎯 Objective: Extract Hidden Flag via Automated Side-Channel Brute-Force
💣 Vulnerability: Linear Character-by-Character Validation Oracle
⚔️ Method:
  1. Iterates through a targeted alphabet of alphanumeric characters and symbols.
  2. Executes the local binary dynamically via the subprocess module for each guess.
  3. Captures and inspects stdout to detect the absence of the failure string ("Learn to move properly").
  4. Progressively appends correct characters until the flag terminator ("}") is reached.
===========================================================================
"""

import subprocess
import string
import sys

def main():
    target = "./cha-cha" 
    flag = "CCIT{" 
    alphabet = string.ascii_letters + string.digits + "{}_!"

    print(f"[*] Automation started. Target binary: {target}")
    print(f"[*] Initializing brute-force from base: {flag}")

    while True:
        found_in_iteration = False
        
        for character in alphabet:
            guess = flag + character
            
            # Execute the binary and merge stdout/stderr to simplify parsing
            process = subprocess.run(
                [target, guess],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            
            # If the error signature is missing, the character is correct
            if "Learn to move properly" not in process.stdout:
                flag = guess
                print(f"[+] Character confirmed. Current string: {flag}")
                found_in_iteration = True
                break 

        # Exit condition: successfully extracted the closing brace
        if flag.endswith("}"):
            print("\n" + "="*50)
            print(f"[+] SUCCESS: Flag extracted: {flag}")
            print("="*50 + "\n")
            break
            
        # Error handling: execution failed to resolve the next index
        if not found_in_iteration:
            print("\n[-] Error: Next character not found. Review alphabet constraints.")
            sys.exit(1)

if __name__ == "__main__":
    main()
