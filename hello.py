#Ask user for their name
name = input("what's your name?")

#remove white space from str
Name = name.strip()

#split user's name into first and last
first, last = name.split(" ")

#capitalize User's name - Sentence case
name = name.capitalize()

#capitalize User's name - Initial Caps
name = name.title

#Say hello to use
print(f"hello, {name}")
