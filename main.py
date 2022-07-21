dict_letra_para_score = {
                            'E':1,
                            'A':1,
                            'O':1,
                            'R':1,
                            'T':1,
                            'L':1,
                            'S':1,
                            'D':2,
                            'G':2,
                            'B':3,
                            'C':3,
                            'M':3,
                            'P':3,
                            'U':3,
                            'F':4,
                            'H':4,
                            'V':4,
                            'W':4,
                            'Y':4,
                            'I':5,
                            'K':5,
                            'N':5,
                            'J':8,
                            'X':8,
                            'Q':10,
                            'Z':10
                        }

palavra = input("Digite a palavra: ")
score    = 0
for char in palavra:
    score += dict_letra_para_score[char.upper()]

print("Seu score é: {}".format(score))