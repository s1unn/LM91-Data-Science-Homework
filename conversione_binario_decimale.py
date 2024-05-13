try:
    binary_number = input("Inserisci un numero binario: ")
    decimale = 0
    lunghezza = len(binary_number)
    if not all(char in '01' for char in binary_number):
        raise ValueError("Il numero inserito non è binario.")
    for i in range(lunghezza):
        decimale += int(binary_number[i]) * (2 **(lunghezza - 1 - i))
    print(decimale)  
except ValueError as e:
    print(e)