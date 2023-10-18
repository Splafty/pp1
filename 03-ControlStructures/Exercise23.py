dogs_age_in_human_years = int(input("Enter the dog's age in human years: "))
i = 1
dogs_age_in_dog_years = 0
while i <= dogs_age_in_human_years:
    if i <= 2:
        dogs_age_in_dog_years += 10.5
        i += 1
    else:
        dogs_age_in_dog_years += 4
        i += 1
print(f"The dog's age in dog's years is {dogs_age_in_dog_years} years.")
