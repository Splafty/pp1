facebook = True
twitter = False
instagram = True
number_of_social_media_accounts = 0

if facebook == True:
    number_of_social_media_accounts += 1
if twitter == True:
    number_of_social_media_accounts += 1
if instagram == True:
    number_of_social_media_accounts += 1

if number_of_social_media_accounts >= 2:
    print("A person can be a good influencer!")
else:
    print("A person can't be a good influencer!")
