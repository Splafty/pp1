# 47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign). 
# Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

import separationofletters

text = "University"
separated_text = separationofletters.f(text)
print(f"f(\"{text}\") returns \"{separated_text}\"")

text = "UE"
separated_text = separationofletters.f(text)
print(f"f(\"{text}\") returns \"{separated_text}\"")

text = "x"
separated_text = separationofletters.f(text)
print(f"f(\"{text}\") returns \"{separated_text}\"")

text = ""
separated_text = separationofletters.f(text)
print(f"f(\"{text}\") returns \"{separated_text}\"")