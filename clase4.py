name = 'TIGER'
last_name = 'corona'
print(name * 5)
print(name + ' ' + last_name)
print(len(last_name))
print(name.lower())


#print(name[1])
#print(name[2])
#print(name[-1])
# Capitalize the first letter.

text = "hello world"
print(text.capitalize())  # "Hello world"

# title()
# Capitalize the first letter of each word.
text = "hello world"
print(text.title())  # "Hello World"

# strip()
# Remove leading and trailing whitespace.
text = "  hello  "
print(text.strip())  # "hello"

# replace(old, new)
# Replace parts of the string.
text = "hello world"
print(text.replace("world", "Python"))  # "hello Python"

# split(sep)
# Split the string into a list based on the separator.
text = "hello,world,Python"
print(text.split(","))  # ['hello', 'world', 'Python']

# join(iterable)
# Join elements of an iterable into a single string.
lst = ["hello", "world"]
print(" ".join(lst))  # "hello world"

# find(sub)
# Find a substring and return the index of its first occurrence.
text = "hello world"
print(text.find("world"))  # 6

# startswith(prefix) and endswith(suffix)
# Check if the string starts or ends with a substring.
text = "hello world"
print(text.startswith("hello"))  # True
print(text.endswith("world"))  # True

# Complete Example:
phrase = "  Welcome to Python!  "
phrase = phrase.strip().replace("Python", "the world of Python").upper()
print(phrase)  # "WELCOME TO THE WORLD OF PYTHON!"


