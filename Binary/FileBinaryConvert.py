def text_to_binary(file_path):
    # Open the file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Convert each character to its 8-bit binary equivalent
    binary_string = ''.join(format(ord(char), '08b') for char in text)

    return binary_string

def save_binary_to_file(binary_string, output_file):
    # Save the binary string to an output file
    with open(output_file, 'w') as file:
        file.write(binary_string)

# Example usage
input_file = input('InFile: ')
output_file = input('OutFile: ')

binary_string = text_to_binary(input_file)
save_binary_to_file(binary_string, output_file)

print(f"Binary data has been saved to {output_file}")
