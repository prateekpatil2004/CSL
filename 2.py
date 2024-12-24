import regex as re
# Sample text to work with
text = "  Hello, World! Welcome to Python programming.  "

# 1. Strip leading and trailing spaces
clean_text = text.strip()
print(f"Original Text: '{text}'")
print(f"Text after stripping spaces: '{clean_text}'")

# 2. Convert the text to uppercase
upper_text = clean_text.upper()
print(f"\nText in uppercase: '{upper_text}'")

# 3. Convert the text to lowercase
lower_text = clean_text.lower()
print(f"\nText in lowercase: '{lower_text}'")

# 4. Count occurrences of a substring (e.g., "o")
count_o = clean_text.count("o")
print(f"\nNumber of occurrences of 'o': {count_o}")

# 5. Replace a word in the string
replaced_text = clean_text.replace("Python", "Data Science")
print(f"\nText after replacing 'Python' with 'Data Science': '{replaced_text}'")

# 6. Find the position of a word in the string
position_world = clean_text.find("World")
print(f"\nPosition of 'World' in the text: {position_world}")

# 7. Split the text into words (by default on spaces)
words = clean_text.split()
print(f"\nList of words in the text: {words}")

# 8. Join the words back into a single string
joined_text = " ".join(words)
print(f"\nText after joining words: '{joined_text}'")

# 9. Check if the text starts with "Hello"
starts_with_hello = clean_text.startswith("Hello")
print(f"\nDoes the text start with 'Hello'? {starts_with_hello}")

# 10. Check if the text ends with a specific word (e.g., "programming.")
ends_with_programming = clean_text.endswith("programming.")
print(f"\nDoes the text end with 'programming.'? {ends_with_programming}")

text = """
John's email is [email protected]. He said, "Python is awesome!!"    It's a     great   language.
Another email: [email protected]. 
"""

# 1. Remove special characters except for spaces and email-related characters.
# Using regex to remove non-alphabetic characters and non-email symbols
clean_text = re.sub(r"[^a-zA-Z0-9@\.\s]", "", text)
print("Text after removing special characters:")
print(clean_text)

# 2. Convert the text to lowercase
clean_text = clean_text.lower()
print("\nText after converting to lowercase:")
print(clean_text)

# 3. Replace multiple spaces with a single space
clean_text = re.sub(r"\s+", " ", clean_text)
print("\nText after replacing multiple spaces:")
print(clean_text)

# 4. Extract all words starting with a vowel (a, e, i, o, u)
vowel_words = re.findall(r"\b[aeiouAEIOU]\w+", clean_text)
print("\nWords starting with a vowel:")
print(vowel_words)

# 5. Replace email addresses with '[email protected]'
masked_text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[email protected]", clean_text)
print("\nText after replacing emails:")
print(masked_text)
