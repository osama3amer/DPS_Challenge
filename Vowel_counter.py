def vowel_counter (word):
    vowels = "aeiouAEIOU"
    counter = 0
    for i in word:
        if i in vowels:
            counter+=1
    return counter


word = input("Enter your desired word:")

print(vowel_counter(word))
