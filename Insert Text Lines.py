# Create mylife.txt
with open("mylife.txt", "a") as file_mylife:
    # while input is y, loop to first line
    more_line = ""
    while more_line != "n":
        line = input("\nEnter line: ") 
        file_mylife.write(line)
        more_line = input("Are there more lines y/n? ")