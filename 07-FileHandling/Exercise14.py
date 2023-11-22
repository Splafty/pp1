# 14.	Write a program that allows you to add a name of next product you want to buy at the end of the shopping.txt file. 
# Enter the product name from the keyboard. 
# Numbers products on the list. 
# Tip: open the file in appending mode. 

file = open("shopping.txt",'a')
read_product = True
counter = 0
while read_product:
    product = input("Enter product name: ")
    if product != "":
        counter += 1
        file.write(f"{counter}. {product} \n")
    else:
        read_product = False
file.close()


