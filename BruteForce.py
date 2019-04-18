import sys
import time

def BruteForceNormal():
    tempsDepart = time.time()
    lettre1 = chr(96)
    lettre2 = chr(96)
    lettre3 = chr(96)
    lettre4 = chr(96)
    lettre5 = chr(96)
    password = sys.argv[2]
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    while i < 26:
        lettre1 = chr(ord(lettre1) + 1)
        i += 1

        while j < 26:
            lettre2 = chr(ord(lettre2) + 1)
            j += 1

            while k < 26:
                lettre3 = chr(ord(lettre3) + 1)
                k += 1

                while l < 26:
                    lettre4 = chr(ord(lettre4) + 1)
                    l += 1

                    while m < 26:
                        lettre5 = chr(ord(lettre5) + 1)
                        if password == str(lettre1 + lettre2 + lettre3 + lettre4 + lettre5):
                            print(lettre1 + lettre2 + lettre3 + lettre4 + lettre5)
                            print(time.time() - tempsDepart)
                            quit()
                        m += 1
                    m = 0
                    lettre5 = chr(96)
                l = 0
                lettre4 = chr(96)
            k = 0
            lettre3 = chr(96)
        j = 0
        lettre2 = chr(96)
    i = 0


def BruteForceComplex():
    tempsDepart = time.time()
    passwordComplex = sys.argv[2]
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    lettre1 = chr(96)
    lettre2 = chr(96)
    lettre3 = chr(96)
    lettre4 = chr(96)
    lettre5 = chr(96)
    while i < 52:
        if (i != 26):
            lettre1 = chr(ord(lettre1) + 1)
        elif (i == 26):
            lettre1 = chr(65)
        i += 1

        while j < 52:
            if (j != 26):
                lettre2 = chr(ord(lettre2) + 1)
            elif (j == 26):
                lettre2 = chr(65)
            j += 1

            while k < 52:
                if (k != 26):
                    lettre3 = chr(ord(lettre3) + 1)
                elif (k == 26):
                    lettre3 = chr(65)
                k += 1

                while l < 52:
                    if (l != 26):
                        lettre4 = chr(ord(lettre4) + 1)
                    elif (l == 26):
                        lettre4 = chr(65)
                    l += 1

                    while m < 52:
                        if (m != 26):
                            lettre5 = chr(ord(lettre5) + 1)
                        elif (m == 26):
                            lettre5 = chr(65)

                        if passwordComplex == str(lettre1 + lettre2 + lettre3 + lettre4 + lettre5):
                            print(lettre1 + lettre2 + lettre3 + lettre4 + lettre5)
                            print(time.time() - tempsDepart)
                            quit()
                        m += 1
                    m = 0
                    lettre5 = chr(96)
                l = 0
                lettre4 = chr(96)
            k = 0
            lettre3 = chr(96)
        j = 0
        lettre2 = chr(96)
    i = 0

def BruteForceComplexDeLaMortQuiTue():
    tempsDepart = time.time()
    passwordComplexDeLaMortQuiTue = sys.argv[2]
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    lettre1 = chr(96)
    lettre2 = chr(96)
    lettre3 = chr(96)
    lettre4 = chr(96)
    lettre5 = chr(96)
    while i < 62:
        if (i != 26 and i != 52):
            lettre1 = chr(ord(lettre1) + 1)
        elif (i == 26):
            lettre1 = chr(65)
        else:
            lettre1 = chr(48)
        i += 1

        while j < 62:
            if (j != 26 and j != 52):
                lettre2 = chr(ord(lettre2) + 1)
            elif (j == 26):
                lettre2 = chr(65)
            else:
                lettre2 = chr(48)
            j += 1

            while k < 62:
                if (k != 26 and k != 52):
                    lettre3 = chr(ord(lettre3) + 1)
                elif (k == 26):
                    lettre3 = chr(65)
                else:
                    lettre3 = chr(48)
                k += 1

                while l < 62:
                    if (l != 26 and l != 52):
                        lettre4 = chr(ord(lettre4) + 1)
                    elif (l == 26):
                        lettre4 = chr(65)
                    else:
                        lettre4 = chr(48)
                    l += 1

                    while m < 62:
                        if (m != 26 and m != 52):
                            lettre5 = chr(ord(lettre5) + 1)
                        elif (m == 26):
                            lettre5 = chr(65)
                        else:
                            lettre5 = chr(48)
                        if passwordComplexDeLaMortQuiTue == str(lettre1 + lettre2 + lettre3 + lettre4 + lettre5):
                            print(lettre1 + lettre2 + lettre3 + lettre4 + lettre5)
                            print(time.time() - tempsDepart)
                            quit()
                        m += 1
                    m = 0
                    lettre5 = chr(96)
                l = 0
                lettre4 = chr(96)
            k = 0
            lettre3 = chr(96)
        j = 0
        lettre2 = chr(96)
    i = 0



if (sys.argv[1] == "BruteForceFaible()") :
    BruteForceNormal()
elif (sys.argv[1] == "BruteForceMoyen()"):
    BruteForceComplex()
elif (sys.argv[1] == "BruteForceFort()"):
    BruteForceComplexDeLaMortQuiTue()


