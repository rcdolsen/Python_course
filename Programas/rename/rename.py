import os

for filename in os.listdir("."):
    if filename.endswith(".py") and not filename.islower():
        new_filename = filename[0].lower() + filename[1:]
        os.rename(filename, new_filename)