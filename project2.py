HISTORY_File = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('history cleared')
    
def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()
    
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("invalid input. use format: number operator nu")
        return
        
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("you cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("invalid operator. User only + - * / ")
        return
        
    if int(result) == result:
        result = int(result)
    print("result:", result )
    save_to_history(user_input, result)
def main():
        print('---simple calculator (type history, clear or exit')
        while true:
            user_input = input("enter calculation (+-*/ pr command histpry,clear")
            if user_input == "exit":
                print('goodbye')
                break
            elif user_input == 'history':
                show_history()
            else:
                calculate(user_input)