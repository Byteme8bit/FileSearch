import os

__author__ = "byteme8bit"


# Program's main function
def main():
    print_header()  # Prints app header
    folder = get_folder_from_user()  # Grabs input from user
    if not folder:  # Test for no input from user
        print("Try again")
        return

    text = get_search_text_from_user()  # Grabs input from user
    if not text:  # Test for no input from user
        print("Try again")
        return

    search_folders(folder, text)


# Prints program's header in terminal
def print_header():
    print('=====================================')
    print('              File Search            ')
    print('=====================================')
    print()


# Function defines grabbing input from user to be used as location to be searched. Absolute path required!
def get_folder_from_user():
    folder = input("What folder do you want to search? ")  # Grabs input from user (Absolute path to location)
    if not folder or not folder.strip():  # This test will trigger the main test for empty input from user
        return None

    if not os.path.isdir(folder):  # Tests for file or directory
        return None

    return os.path.abspath(folder)


# Function defines grabbing input from user to be used as search terms
def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]")    # Grabs input from user
    return text


# Defines the algorithm to recursively search through directories
def search_folders(folder, text):
    print("Would search {} for {}".format(folder, text))


# Defines the algorithm to recursively search files for the text
def search_file():
    pass


# Allows file to be imported without running in host environment
if __name__ == '__main__':
    main()
