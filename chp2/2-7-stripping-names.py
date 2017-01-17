# Exercise 2-7
# Stripping Names: Store a person’s name, and include some whitespace 
# characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.

name = "      \tChris \tCasio\n  "
print(name)
print("Left strip: " + name.lstrip())
print("Right strip: " + name.rstrip())
print("Dual strip: " + name.strip())
