# 20.	Using any text editor, create the following two text files:
# MeatAndFish.txt
# Skinless white meat
# Tuna fish
# Luncheon meat
# Lean cuts of red meat
# GrainsAndBread.txt
# Bread
# Rice
# All purpose flour
# Breakfast cereal
# Pasta 
# Then, write a program that creates the allproducts.txt file, in which save the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

with open("MeatAndFish.txt", "r") as f1:
    with open("GrainsAndBread.txt", "r") as f2:
        with open("allproducts.txt", "w") as f3:
            f1_content = f1.read()
            f2_content = f2.read()
            f3.write(f"{f1_content}\n{f2_content}")
