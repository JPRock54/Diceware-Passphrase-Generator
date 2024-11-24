import random

WORD_FILE = "words.txt"
SPECIAL_CHARACTER_FILE = "special_characters.txt"

# Idiot proofing integer inputs
def integer_input(phrase):
    while True:
        integer = input(phrase)
        try:
            integer = int(integer)
        except ValueError:
            print("That is not an integer!\n")
            continue
        else:
            break
    return integer


# Iterate through the lines and returns it when found
def store_line(file_path, line_number):
    with open(file_path, 'r') as file:
        for current_line_number, line in enumerate(file, start=1):
            if current_line_number == line_number:
                return line
    

# Returns passphrase of a (word_count) as a string
def generate_diceware_passphrase(word_count):
    passphrase = []

    # Simulate dice rolls and pick words from the wordlist
    for _ in range(word_count):
        dice_roll = ''.join(str(random.randint(0, 5)) for _ in range(5)) # Rolls five dice (each number if one lower)
        line_number = int(dice_roll, 6) + 2 # Find the line number of the associated dice_roll
        line = store_line(WORD_FILE, int(line_number)) # Stores the whole string of the diceroll
        parts = line.split() # Splits the word into its dicerole and word
        passphrase.append(parts[1]) # Appends the word to the list
    
    # Returns the passphrase as a string
    return ' '.join(passphrase)


# Returns a list of special characters of (special_character_amount)
def generate_special_characters(special_charcter_amount):
    special_characters = []

    # Simulate dice rolls and pick special characters from the specialcharacterslist
    for _ in range(special_charcter_amount):
        dice_roll = ''.join(str(random.randint(0, 5)) for _ in range(2)) # Rolls two dice (each number if one lower)
        line_number = int(dice_roll, 6) + 2 # Find the line number of the associated dice_roll
        line = store_line(SPECIAL_CHARACTER_FILE, int(line_number)) # Stores the whole string of the diceroll
        parts = line.split() # Splits the word into its dicerole and character
        special_characters.append(parts[1]) # Appends the character to the list

    # Returns the list of speical characters
    return special_characters


def add_special_characters(passphrase, special_characters):
    n = 0
    word_list = passphrase.split()
    while n < len(special_characters):
        dice_roll = ''.join(str(random.randint(0, 5)) for _ in range(2))
        # Checks if character can be placed within word passes if it can't be
        if int(dice_roll[0]) > len(passphrase) or int(dice_roll[1]) > len(passphrase[0]) + 1:
            pass

        # Appends character within the word
        word_list[int(dice_roll[0])] = word_list[int(dice_roll[0])][:int(dice_roll[1])] + special_characters[n] + word_list[int(dice_roll[0])][int(dice_roll[1]):]
        n += 1
    return ' '.join(word_list)


def main():
    # User inputs
    word_count = integer_input("Input the amount of words you want to generate: ")
    special_character_count = integer_input("Input the amount of special characters you want: ")

    passphrase = generate_diceware_passphrase(word_count=word_count) # Generates a diceware passphrase of chosen length
    special_characters = generate_special_characters(special_charcter_amount=special_character_count) # Generates special characers in a list
    passphrase = add_special_characters(passphrase, special_characters) # Appends the special characters to 
    print(f"Your passphrase is: {passphrase}.") # Displays passphrase


# Main
if __name__ == "__main__":
    main()