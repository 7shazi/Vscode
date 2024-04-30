import itertools

# Define the character set for password generation
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Define the minimum and maximum length of passwords to generate
min_length = 6  # Minimum password length
max_length = 8  # Maximum password length

# Generate all possible combinations of characters within the specified length range
passwords = []
for length in range(min_length, max_length + 1):
    for combination in itertools.product(characters, repeat=length):
        password = ''.join(combination)
        passwords.append(password)

# Write generated passwords to a file
output_file = 'custom_passwords.txt'
with open(output_file, 'w') as file:
    for password in passwords:
        file.write(password + '\n')

# Calculate the total number of passwords generated
total_passwords = len(passwords)
print(f"Password file '{output_file}' generated successfully with {total_passwords} unique passwords.")
