
def find_acronym():
    look_up = input("Greetings! What software acronym would you like to have me look for?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print ('That file is not found')
        return

    if not found:
        print("Many Apologies, but I was not able to locate that acronym.")
    
def add_acronym():
    acronym = input('What acronym would you like to add?\n')
    definition = input('What is the definition?\n')
    with open('acronyms.txt', 'a') as file:
        file.write(acronym+ ' - ' + definition + '\n')

def main():
    # Ask the user wheter they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()