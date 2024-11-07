"Palindrome program"

import string
from unidecode import unidecode

#### Fonction secondaire


def ispalindrome(p):
    """
    Check if a string p is a palindrome
    """
    p = unidecode(p.replace(" ", "")).lower()
    p = p.translate(str.maketrans("", "", string.punctuation))

    return p == p[::-1]

#### Fonction principale


def main():

    """
    main function
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
