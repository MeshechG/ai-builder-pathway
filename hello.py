#Ask user for their name
name = input("what's your name?")

#remove white space from str
name = name.strip()

#capitalize User's name - Initial Caps
name = name.title()

#Say hello to use
print(f"hello, {name}")
