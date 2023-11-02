import random
import string

def generate_password(length=10):
    """Generate a random password with the specified length."""
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation.replace("'", "")  # Remove apostrophe from punctuation
    password_chars = f"{letters}{numbers}{symbols}"
    password = "".join(random.choice(password_chars) for _ in range(length))
    return password

def check_password_strength(password):
    """Check the strength of the specified password."""
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = ('That\'s a very bad password.'
            ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
            ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
            ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!!'
            ' Hackers don\'t have a chance guessing that password!')

    print('\nYour password has: ')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{special_count} special characters')
    print(f'\nPassword Score: {strength / 5}')
    print(f'Remarks: {remarks}')
    print("\n")

while True:
    print("="*60)
    print("\tPassword Generator and Strength Checker")
    print("="*60)
    print("\nChoose an option:\n[1] Generate a random password | [2] Check the strength of a password | [3] Quit")
    choice = input("\nSelect an option: ")
    if choice == '1':
        length = int(input("\nEnter the number of characters you want for your password: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
        check_password_strength(password)
    elif choice == '2':
        password = input('Enter the password: ')
        check_password_strength(password)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
