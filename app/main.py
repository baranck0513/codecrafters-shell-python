import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            exit()

        if command.startswith("echo "):
            print(command[5:])
            continue
        if command == "echo":
            print("")
            continue

        print(f"{command}: command not found")

    
        # pass


if __name__ == "__main__":
    main()
