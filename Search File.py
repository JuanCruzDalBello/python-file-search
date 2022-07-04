import os
import time

def findFile(starting_dir, wanted_file):
    # If the specified file is in the starting directory,
    # return its path, else return None
    for root, dirs, files in os.walk(starting_dir):
        if wanted_file in files:
            return os.path.join(root, wanted_file)      
    return None


print("Enter the name of the file you want to find and the directory where to start the search.")
print("To exit the program don't write anything for 'File name' and press Enter.")

while(True):
    # User input
    print("\n--------------- Search File ---------------")
    wanted_file = input("\nFile name: ")
    if wanted_file == "":
        print("Thank you for using the program.")
        print("Shutting down 'Search File ...")
        time.sleep(2)
        break
    starting_dir = input("Starting directory: ")    
    
    if not os.path.isdir(starting_dir):
        print(f"{starting_dir} is not a valid directory.")
    else:
        # Shows the file's path to the user, unless None
        path = findFile(starting_dir, wanted_file)
        if path != None:
            print(f"Path: '{path}'")
        else:
            print(f"'{wanted_file}' is not in the selected directory.")
