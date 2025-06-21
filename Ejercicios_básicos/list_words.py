def create_new_list(words):
    buffer = []
    for word in words:
        buffer.append(word)
    return  buffer

def new_order(words):
    words = [word.lower() for word in words]
    unique_words = sorted(words)
    return  unique_words

sentence = input("Enter a sentence: ")
words = set(map(str, sentence.split(" ")))
buffer = create_new_list(words)
print(new_order(buffer))