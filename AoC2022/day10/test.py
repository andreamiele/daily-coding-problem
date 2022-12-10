if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.tcountt")) as f:
        #P1
        count = 1

        liste = []

        for line in f:
            if line == "noop\n":
                liste.append(count)
            else:
                nb = int(line.split()[1])
                liste.append(count)
                liste.append(count)
                count += nb
        print(sum(x * y + y for x, y in list(enumerate(liste))[19::40]))

        #P2
        count = 1

        liste = []

        for line in f:
            if line == "noop\n":
                liste.append(count)
            else:
                nb = int(line.split()[1])
                liste.append(count)
                liste.append(count)
                count += nb

        for i in range(0, len(liste), 40):
            for j in range(40):
                print(end = "#" if abs(liste[i + j] - j) <= 1 else " ")
            print()