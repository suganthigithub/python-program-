def remove_vowels(string):
    vowels="aeiouAEIOU"
    result =""

    for char in string:
        if char not in vowels:
            result += char
    return  result

print(remove_vowels("Guvi Geeks Network Private Limited"))   