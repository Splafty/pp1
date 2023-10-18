article_number = input("EAN-13 article number: ")
if len(article_number) != 13:
    print("Article number is not correct")
else:
    print("Article number is correct")
    if article_number[0] + article_number[1] + article_number[2] == "590":
        print("Article manufactured in Poland")
    else:
        print("Article not manufactured in Poland")