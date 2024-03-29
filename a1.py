# Nicole Kwan
# nkwan3@uci.edu
# 76647093

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

# PART 2

def create_file(args):
    try:
        new_file = args[-1] + ".dsu"
        path = Path(args[0]) / new_file
        path.touch(exist_ok=True)
        return str(path)
    except Exception:
        print(f"ERROR")
        return None

def delete_file(args):
    path = Path(args[0])

    try:
        if path.exists():
            path.unlink()
            return print(f"{path} DELETED")
        else:
            print("ERROR")
    except Exception as e:
        return "ERROR"

def read_file(args):
    path = Path(args[0])

    if (path.stat().st_size == 0) is True:
        print("EMPTY")
    else:
        try:
            with open(path, "r") as file:
                content = file.read()
                print(content.strip())
        except Exception:
            print(f"ERROR")

def main():
    try:
        while True:
            user_input = input("")
            command, *args = user_input.split()
            if command.lower() == 'q':
                break
            elif command.lower() == 'l': 
                if ("-f" in args) or ("-s" in args) or ("-e" in args):
                    output_directory(args)
                elif (args[-1] == "-r") or (len(args) == 1):
                    print_directory(args)
                else:
                    print("ERROR: Please enter a valid option.")
            elif command.lower() == "c":
                try:
                    print(create_file(args))
                except:
                    print("ERROR")
            elif command.lower() == "d":
                if Path(args[0]).suffix.lower() != ".dsu":
                    print("ERROR")
                else:
                    delete_file(args)
            elif command.lower() == "r":
                if Path(args[0]).suffix.lower() != ".dsu":
                    print("ERROR")
                elif len(args) < 0:
                    print("ERROR")
                else:
                    read_file(args)
            else:
                print("Error: Please enter a valid command and path")
                continue
    except Exception:
        print(f"ERROR")

if __name__ == '__main__':
    main()
