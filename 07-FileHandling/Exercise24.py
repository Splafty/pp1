# 24.	In any text editor, create a text file studentslist.txt containing the following data in the CSV format:
# first_name,last_name,age,gender,email
# Decca,Blackstone,52,Male,dblackstone0@time.com
# Elena,Rechert,27,Female,erechert1@ucoz.com
# Bibbye,Norree,26,Female,bnorree2@reddit.com
# Alasdair,McCoole,53,Male,amccoole3@foxnews.com
# Hogan,Hatrey,26,Male,hhatrey4@zimbio.com
# Then, create a program that reads data from the CSV file and displays the first name, last name and email address of students under 30. 
# Format the data as below. 
# Sample result:
# Elena   Rechert  erechert1@ucoz.com
# Bibbye  Norree   bnorree2@reddit.com
# Hogan   Hatrey   hhatrey4@zimbio.com
# Tip: import and use the CSV module. 

import csv


with open("studentslist.txt", 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        age = int(row['age'])
        if age < 30:
            print(f"{row['first_name']:<10}{row['last_name']:<10}{row['email']:<20}")
