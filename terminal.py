import os
import subprocess
from transform_command import transform_command

def main():
    # check for cached API key, stored in a file named data.txt
    if not os.path.exists('data.txt'):
        print("Please enter your OpenAI API key:")
        api_key = input('> ')
        with open('data.txt', 'w') as f:
            f.write(api_key)
    else:
        with open('data.txt', 'r') as f:
            api_key = f.read().strip()

    while True:
        user_input = input('> ')
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            transformed_command = transform_command(user_input, api_key)
            # Confirm with the user before executing
            confirm = input(f"Execute '{transformed_command}'? (y/n): ")
            if confirm.lower() == 'y':
                subprocess.run(transformed_command, shell=True)
            else:
                print("Command execution canceled.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
