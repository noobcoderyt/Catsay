import sys
import colorama
from colorama import Fore

colorama.init()

try:
    text = sys.argv[1]

    print(Fore.GREEN + f"""

    _._     _,-'""`-._
    (,-.`._,'(       |\`-/|
        `-.-' \ )-`( , o o)
            `-    \`_`"'-

    {text.capitalize()}

    """)

except:
    print("Usage : python3 catsay.py <text>")