nbr_notes = input("Combien de notes avez-vous eu ?")
note = 0
notes = 0
while note < int(nbr_notes):
    notes = notes + int(input("Donnez moi l'une de vos notes. >"))
    note = note + 1

moyenne = notes / int(nbr_notes)
print(moyenne)