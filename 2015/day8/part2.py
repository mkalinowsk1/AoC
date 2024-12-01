with open("input.in") as fin:
    file = fin.read().splitlines()

total_original_len = 0
total_encoded_len = 0

for line in file:
    # Length of the original string (code representation)
    original_len = len(line)
    
    # Encoding the string
    encoded_string = '"'  # Starting with the new opening quote
    for char in line:
        if char == '"':
            encoded_string += r'\"'  # Escape quote
        elif char == '\\':
            encoded_string += r'\\'  # Escape backslash
        else:
            encoded_string += char
    encoded_string += '"'  # Closing quote

    # Length of the encoded string
    encoded_len = len(encoded_string)
    
    # Update total lengths
    total_original_len += original_len
    total_encoded_len += encoded_len

# Compute the difference
print(total_encoded_len - total_original_len)
