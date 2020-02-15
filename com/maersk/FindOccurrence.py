#******************************************************************************************
#Write a program to find number of occurrences of each vowel present in the given string?
#******************************************************************************************

d = {}
word = input("Please provide the input: ")
vowels ={"a", "e", "i", "o", "u"}

for x in word:
    if x in vowels:
        d[x] = d.get(x, 0)+1

for k, v in sorted(d.items()):
    print(k, "occurred", v, "times")
