print("Welcome to ASCII Code-English text converter")
print("1.  ASCII Code to English Text")
print("2. English Text to ASCII Code")

try:
    userInput = int(input("What feature would you like to use:"))

    if userInput == 1:
        user_input = input("PLEASE ENTER TEXT/WORD:")
        replaced_string = user_input.replace(" ", "* *")

        string_array = replaced_string.split("*")

        for letters in string_array:
            for letter in letters:
                print(ord(letter), end=" ")



    elif userInput == 2:
        user_input2 = input("PLEASE ENTER ASCII CODE:")

        string_array2 = user_input2.split()

        for number in string_array2:
            print(chr(int(number)), end="")

except:
    print("Invalid input.Please follow the necessary information")
