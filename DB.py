def sameReverse(word):
    c = len(word)
    lst = [None] * c
    for i in word:
        lst[c-1] = i
        c -= 1
    reve = "".join(lst)

    if word == reve:
        return True
    else:
        return False


def sameReverse2(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True


print(sameReverse("ala"))
print(sameReverse2("alas"))


