import re

# Prompt the user for the file name
fname = input('Enter file name: ')

def sum_integers_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        # Find all sequences of digits
        numbers = re.findall(r'[0-9]+', content)

        # Convert the extracted strings to integers
        integers = [int(num) for num in numbers]

        # Sum up the integers
        total_sum = sum(integers)

        return total_sum
    except FileNotFoundError:
        return "File not found. Please check the file name."
    except Exception as e:
        return f"An error occurred: {e}"

# Prompt the user for the file name
result = sum_integers_in_file(fname)
print(f"The sum of all integers in the file is: {result}")
