
sentance = "This a common interview Question"

char_frequency = {}

for char in sentance:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True
)
print(char_frequency_sorted[0])
