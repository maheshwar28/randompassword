import random
import string

def generate_password(length=12, min_alphabets=6, min_symbols=1, min_numbers=1):
    if length < min_alphabets + min_symbols + min_numbers:
        raise ValueError("Password length is too short to meet the specified criteria.")

    # Ensure at least 6 alphabets
    alphabets = ''.join(random.choice(string.ascii_letters) for _ in range(min_alphabets))

    # Ensure at least 1 symbol
    symbols = ''.join(random.choice(string.punctuation) for _ in range(min_symbols))

    # Ensure at least 1 number
    numbers = ''.join(random.choice(string.digits) for _ in range(min_numbers))

    # Fill the rest of the password with a mix of alphabets, symbols, and numbers
    remaining_length = length - (min_alphabets + min_symbols + min_numbers)
    characters = alphabets + symbols + numbers + ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Shuffle the characters to randomize the password
    password = ''.join(random.sample(characters, length))
    return password

# You can customize the length of the password by providing a different value to the function.
# For example, to generate a password with a length of 16 characters:
# password = generate_password(16)

generated_password = generate_password()
print("Generated Password:", generated_password)
