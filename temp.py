acronym = input('What acronym would you like to add?\n')
definition = input('What is the definition?\n')
with open('acronyms.txt', 'a') as file:
    file.write(acronym+ ' - ' + definition + '\n')
#Then ask the user for the definition 
#open the file