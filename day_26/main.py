import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


should_continue = True
while should_continue:
    try:
        word = list(input("Enter the word: ").upper())
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please use only letters")
    else:
        print(nato_list)
        should_continue = False
        