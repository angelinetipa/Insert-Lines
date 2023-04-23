# create mylife.txt
with open("mylife.txt", "a") as file_mylife:
# while input is y, loop to first line
    more_line = ""
    while more_line != "n":
        # input for text line
        line = input("\nEnter line: ") 
        # write input to mylife.txt
        file_mylife.write(line)
        file_mylife.write("\n")
        # input if need more line
        more_line = input("Are there more lines y/n? ")

# print output
