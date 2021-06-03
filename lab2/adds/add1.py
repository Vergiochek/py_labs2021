def word_counter(string):
    string = string.lower()
    for symbol in string:
        if not str.isalpha(symbol) and symbol != " ":
            string = string.replace(symbol, "")

    words = string.split()
    total = dict()

    for word in words:
        total[word] = words.count(word)

    print(f"Words amount in text: {total}")
    return total

def average_amount(string):
    sentences = string.split(". ")
    words = string.split()
    print(f"Average words amount in sentences: {len(words) / len(sentences)}")

def median_amount(string):
    num_list = list()
    text = string.split(". ")

    for sentence in text:
        num_list.append(len(sentence.split()))

    num_list.sort()
    middle = int(len(num_list) / 2) - 1
    print(f"Median words amount: {num_list[middle]}")

def find_ngrams(words, k = 10, n = 4):
    ngrams = dict()
    for word in words:
        slices = [word[i: n + i] for i in range(len(word) - n + 1)]
        for slice in slices:
            if ngrams.get(slice):
                ngrams[slice] += words[word]
            else:
                ngrams.update({slice: words[word]})

    res = sorted([(ngram, ngrams[ngram]) for ngram in ngrams], key = lambda l: -l[1])

    print(f"Top{k} {n}-grams: {res[0: k]}")

text = input("Enter text: ")
words = word_counter(text)
average_amount(text)
median_amount(text)
find_ngrams(words, 5, 2)