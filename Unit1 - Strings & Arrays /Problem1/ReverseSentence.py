def reverse_sentence1(sentence):
    reversed_sentence = sentence[::-1]
    return reversed_sentence

def reverse_sentence2(sentence):
    chars = list(sentence) 
    L = 0
    R = len(chars) - 1        
    while L < R:
        chars[L], chars[R] = chars[R], chars[L]
        L += 1
        R -= 1
    return "".join(chars)
def reverse_sentence3(sentence):
    chars = list(sentence)
    reversed_string = ""
    for i in range(len(chars)):
        reversed_string+=chars.pop()
    return reversed_string
        
print("slicing method:")
print(reverse_sentence1("Naman"))
print(reverse_sentence1("in reverse"))
print(reverse_sentence1("Sentence in reverse"))
print("Left and Right pointer method")
print(reverse_sentence2("Naman"))
print(reverse_sentence2("in reverse"))
print(reverse_sentence2("Sentence in reverse"))
print("Stack method")
print(reverse_sentence3("Naman"))
print(reverse_sentence3("in reverse"))
print(reverse_sentence3("Sentence in reverse"))