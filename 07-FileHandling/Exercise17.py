# 17.	Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
# Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
# The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

with open("Peter_Pan.txt") as file:
    counter = 0
    for line in file:
        if counter <= 5:
            counter += 1
            print(line)
        else:
            input("Press Enter to continue...")
            counter -= 5
