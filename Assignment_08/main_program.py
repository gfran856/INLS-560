import sys

while True: # we use a while look to keep the menu up
# This if called file_variable because it takes the users input as a variable, and sets it equal to the file
    file_variable = input('''
What file would you like to search for?:
    a) Popular Music
    b) Popular Movies
    x) exit file search
                          
    Enter your choice here:                       ''')
    # [TEST] file_variable = file_variable.lower() <---- doesnt seem to work :(
    if file_variable == 'x':
        sys.exit() # this is required to exit sys module
    elif file_variable == 'a':
        file_variable = 'gpt_music.csv'
    elif file_variable == 'b':
        file_variable = 'gpt_movies.csv'
    else:
        print("Invaled option, please try again. Select a, b, or x.")
        continue # Returns to start of the loop

# Enter a search term (this is considered a global variable)
    search_variable = input(f" Enter a search term for {file_variable} file: ")
    search_variable = search_variable.title()

# Define the search function
    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file: # <-------- what does the 'r' do?
            content = file.read()
# Check to see if users search variable is in the file variable 
        if search_variable in content:
            print(f'Your search term {search_variable} exsists in the {file_variable} file!')
            see_entries = input('Would you like to see the entries? (Yes = y, No = n): ').lower()
# Run if statements, and display searches
            if see_entries == 'y':
                print(f'Here are all the entries with the term {search_variable}:')
                with open(file_variable, 'r') as file:
                    for line in file:
                        if search_variable in line:
                            print(line.strip())
            elif see_entries == 'n':
                print("Returing you to the file explorer-->")
            else:
                print(f"{search_variable} does not exsist in {file_variable}, returing you to the file explorer -->")
        else:
            print(f'Your search term "{search_variable}" was not found in the "{file_variable}" file.')
# Call the function
    find(file_variable, search_variable)