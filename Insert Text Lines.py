# open mylife.txt[append]
with open("mylife.txt", "a") as file_mylife:
    # while input is yes, loop to first line
    more_line = ""
    while more_line != "no":
        # input for text line
        line = input("\n\033[1m\033[3mEnter line:  \033[0m") 
        # write input to mylife.txt
        file_mylife.write(line + "\n")
        # input if need more line
        more_line = input("\033[1m\033[3mAre there more lines yes/no?  \033[0m")
    
# print output
with open("mylife.txt", "r") as file_mylife1:
    print("\n\n\033[1m\033[3mLines from file mylife.txt:\033[0m\n")
    for line in file_mylife1:
        print(line.strip())
    print("\n")