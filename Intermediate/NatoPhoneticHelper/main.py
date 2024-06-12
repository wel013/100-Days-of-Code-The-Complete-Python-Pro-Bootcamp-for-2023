import pandas

# create a dictionary for the format {A:Alpha}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# create a list from the user input
def enter_name():
    name_str = input("Enter a word: ")
    try:
        new_list = [data_dict[letter.upper()] for letter in name_str]
    except KeyError:
        print("Sorry, please only enter the letters in the alphabet!")
        enter_name()
    else:
        print(new_list)

enter_name()