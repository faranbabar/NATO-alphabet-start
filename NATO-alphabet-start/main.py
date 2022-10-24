
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
retry = True
while retry:
    word = input("What is the word?").upper()
    output = [phonetic_dict[letter] for letter in word]
    print(output)
    play_again= input("Would you like to again Type y to continue").lower()
    if play_again == 'y':
        retry = True
    else:
        retry = False

