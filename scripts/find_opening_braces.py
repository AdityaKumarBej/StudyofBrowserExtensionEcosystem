def find_closing_bracket(file_path, opening_line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    stack = []

    for index, line in enumerate(lines):
        for char in line:
            if char == '[':
                stack.append(index + 1)
            elif char == ']':
                if stack and stack[-1] == opening_line_number:
                    return index + 1
                stack.pop()

    raise ValueError(f"No matching closing bracket found for opening bracket at line {opening_line_number}.")

if __name__ == "__main__":
    file_path = "../datasets/firefox/myjsonfile_1_100.json"
    opening_line_number = int(input("Enter the line number containing the opening bracket: "))

    try:
        closing_line_number = find_closing_bracket(file_path, opening_line_number)
        print(f"The closing bracket for the opening bracket at line {opening_line_number} is at line {closing_line_number}.")
    except Exception as e:
        print(f"An error occurred: {e}")
