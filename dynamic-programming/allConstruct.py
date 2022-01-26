def allConstruct(target, wordBank):
    if target == "": return [[]]

    result = []

    for word in wordBank:
        if target.index(word) == 0:
            suffix = target[len(word):] 
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = map(lambda x: [word] + x[:], suffixWays)
            result.append(targetWays[:])

    return result

#print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
word = "potato"
print(word.index("l"))