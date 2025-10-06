def check_character(char):
    # Check karna agar character uppercase hai ya nahi
    if char.isupper():
        return "Uppercase"
    # Check karna agar character lowercase hai ya nahi
    elif char.islower():
        return "Lowercase"
    # Check karna agar character ek digit hai ya nahi
    elif char.isdigit():
        return "Digit"
    # Agar none of the above conditions are true, to character symbol hai
    else:
        return "Symbol"

# Input character lena
character = input("Enter a character: ")

# Character ka type check karna
character_type = check_character(character)

# Result print karna
print(f"The character entered is a {character_type}.")
