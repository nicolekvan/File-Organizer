# Nicole Kwan
# nkwan3@uci.edu
# 76647093

# file_path = Path("/Users/nicolekwan/Workspace/Test")

from pathlib import Path

def print_directory(args):
    path = Path(args[0])

    if path.exists() and path.is_dir():
        files = [file for file in path.iterdir() if file.is_file()]
        directories = [directory for directory in path.iterdir() if directory.is_dir()]

        for file in files:
            print(file)
        for directory in directories:
            print(directory)
            if "-r" in args:
                print_directory([str(directory)])

def output_directory(args):
    path = Path(args[0])

    if path.exists() and path.is_dir(): 
        files = [file for file in path.iterdir() if file.is_file()]
        directories = [directory for directory in path.iterdir() if directory.is_dir()]
        
        if "-f" in args:
            for file in files:
                print(file)
            if "-r" in args:
                for directory in directories:
                    output_directory([str(directory)] + args)

        if "-s" in args:
            search = args[-1]
            for file in files:
                if str(search) in str(file):
                    print(file)
            for directory in directories:
                if "-r" in args:
                    output_directory([str(directory)] + args)
        
        if "-e" in args:
            extension = args[-1]
            for file in files:
                if extension in str(file):
                    print(file)
            if "-r" in args:
                for directory in directories:
                    output_directory([str(directory)] + args)

def create_file():
    pass

def delete_file():
    pass

def read_file():
    pass

def main():
    try:
        while True:
            user_input = input("Enter Command: ")
            command, *args = user_input.split()
            if command.lower() == 'q':
                break
            elif command.lower() == 'l': 
                if ("-f" in args) or ("-s" in args) or ("-e" in args):
                    output_directory(args)
                elif (args[-1] == "-r") or (len(args) == 1):
                    print_directory(args)
                else:
                    print("Error: Please enter a valid option.")
            elif command.lower() == "c":
                pass
            elif command.lower() == "d":
                pass
            elif command.lower() == "r":
                pass
            else:
                print("Error: Please enter a valid command and path")
                continue
    except:
        print("Something went wrong. Please try again.")

if __name__ == '__main__':
    main()
