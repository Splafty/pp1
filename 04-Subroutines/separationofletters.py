# 47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign). 
# Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text):
    i = 0
    separated_text = ""
    if len(text) < 2:
        return text
    else:
        while i < len(text):
            separated_text += text[i]
            if i < len(text) -1:
                separated_text += "-"
            i += 1
    
    return separated_text
    
# def separate_characters(text):
#     # Use the join() method to join characters with "-"
#     separated_text = '-'.join(text)
#     return separated_text

if __name__ == "__main__":
    text = "University"
    separated_text = f(text)
    print(f"f(\"{text}\") returns \"{separated_text}\"")

    text = "UE"
    separated_text = f(text)
    print(f"f(\"{text}\") returns \"{separated_text}\"")

    text = "x"
    separated_text = f(text)
    print(f"f(\"{text}\") returns \"{separated_text}\"")

    text = ""
    separated_text = f(text)
    print(f"f(\"{text}\") returns \"{separated_text}\"")