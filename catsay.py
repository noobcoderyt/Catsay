import sys
import colorama
from colorama import Fore

colorama.init()

try:
    text = " ".join(sys.argv[1:])  # Join all command line arguments to form the complete text

    print(Fore.GREEN + f"""
                            ___________________
                           <{text.capitalize()}>
                            -------------------
    _._     _,-'""`-._          /
    (,-.`._,'(       |\`-/|   / 
        `-.-' \ )-`( , o o) /
            `-    \`_`"'-

    """)

except:
    print("Usage: python3 catsay.py <text>")
