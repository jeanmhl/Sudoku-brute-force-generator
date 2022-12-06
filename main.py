
import random
import sys

tentative = 0
sys.setrecursionlimit(10000)

def sudoku_generator():
    global tentative

    try:
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        line5 = []
        line6 = []
        line7 = []
        line8 = []
        line9 = []

        sudoku = [line1,line2,line3,line4,line5,line6,line7,line8,line9]
        tentative +=1
        o = -1 # o is the line index

        #for each lines
        for x in sudoku:
            o += 1
            b = -1 # b is the column index

            #for each columns
            for _ in range(0, 9):

                test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                b += 1

                y = random.choice(test)

                # check lines
                while y in x:
                    print(f" {y} est déjà dans la ligne {o}: {x}")
                    test.remove(y)
                    y = random.choice(test)

                # check columns
                challenge = []
                for a in sudoku:  # for each lines in the sudoku, get the numbers already in the same column

                    try:
                        challenge.append(a[b])  # b is the column index / == every numbers already generated in the b column

                    except IndexError:
                        print(f"Pas encore de chiffres dans l'index colonne {b} de la ligne {o}")
                        print(f"column : {challenge}")

                while y in challenge:
                    test.remove(y)
                    print(f'{y} déjà dans la colonne {b}')
                    y = random.choice(test)

                #check square

                square1 = line1[0:3] + line2[0:3] + line3[0:3]
                square2 = line1[3:6] + line2[3:6] + line3[3:6]
                square3 = line1[6:] + line2[6:] + line3[6:]

                square4 = line4[0:3] + line5[0:3] + line6[0:3]
                square5 = line4[3:6] + line5[3:6] + line6[3:6]
                square6 = line4[6:] + line5[6:] + line6[6:]

                square7 = line7[0:3] + line8[0:3] + line9[0:3]
                square8 = line7[3:6] + line8[3:6] + line9[3:6]
                square9 = line7[6:] + line8[6:] + line9[6:]

                if o < 3 and b < 3: #square1

                    while y in square1:
                        test.remove(y)
                        print(test)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 1")

                elif o < 3 and b < 6:  # square2

                    while y in square2:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 2")

                elif o < 3 and b < 9:  # square3

                    while y in square3:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 3")

                elif o < 6 and b < 3:  # square4

                    while y in square4:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 4")

                elif o < 6 and b < 6:  # square5
                    while y in square5:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 5")

                elif o < 6 and b < 9:  # square6
                    while y in square6:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 6")

                elif o < 9 and b < 3:  # square7
                    while y in square7:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 7")

                elif o < 9 and b < 6:  # square8
                    while y in square8:
                        test.remove(y)
                        y = random.choice(test)
                        print(f"{y} est déjà dans le carré 8")


                elif o < 9 and b < 9:
                    while y in square9:
                        test.remove(y)
                        print(f"{y} est déjà dans le carré 9")
                        y = random.choice(test)

                # check lines
                while y in x:
                    print(f" {y} est déjà dans la ligne {o}: {x}")
                    test.remove(y)
                    y = random.choice(test)

                # check columns
                challenge = []
                for a in sudoku:  # for each lines in the sudoku, get the numbers already in the same column

                    try:
                        challenge.append(
                            a[b])  # b is the column index / == every numbers already generated in the b column

                    except IndexError:
                        print(f"Pas encore de chiffres dans l'index colonne {b} de la ligne {o}")
                        print(f"column : {challenge}")

                while y in challenge:
                    test.remove(y)
                    print(f'{y} déjà dans la colonne {b}')
                    y = random.choice(test)

                # écriture de l'élément choisi au hasard et ayant passé avec succès les 3 tests.
                x.append(y)

        print("")
        print("Sudoku:")
        for x in sudoku:
            print(x)

        ### Création de cases vides dans le sudoku
        hiddensudoku = []
        listligne = []
        for x in sudoku:
            test_number = [1,2,3,4,5,6,7,8,9]
            listX = []

            randomness = [4,5,6]
            w = random.choice(randomness)
            for _ in range(0, w):
                b = random.choice(test_number)
                test_number.remove(b)
                listX.append(b)

            listligne.append([0 if s in listX else s for s in x])
            hiddensudoku.append(listligne)

        print("\nThe Sudoku is ready to play mannnn")
        for x in listligne:
            print(x)

    ### Nouvelle tentative de génération de sudoku si erreur dans la tentative précédente
    except IndexError:
        print("échec, impossible de continuer, nouvelle tentative de génération du sudoku")
        sudoku_generator()

    except RecursionError:
        sudoku_generator()


    else:
        print("\nsuccès de la génération du sudoku !")
        print(f"tentative : {tentative}ème")

sudoku_generator()

