# text1_list = input("Input sentence: ").split()
# print(text1_list)

# words_list = ["Hello!", "I", "am", "a", "student"]

# print(" ".join(words_list)) # reverse of "split", joining elements of list to string
# print(",".join(words_list))

# # print("-".join([22, 10, 2026])) # TypeError (join works only with strings)

# print("-".join(map(str, [22, 10, 2026])))



"""cleaning messy spaces"""
messy = "   ADA     School      PYTHON course    "
print(" ".join(messy.split()))

"""reversing splitted text"""
sentence = "I love Python"
reversed_words = sentence.split()[::-1]
print(" ".join(reversed_words))

"""listing of string"""
print(list("ADA"))