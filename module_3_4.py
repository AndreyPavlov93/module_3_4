def single_root_words(root_word, *other_word):

    same_word = []
    lowercase_list =[i.lower() for i in other_word]
    lowercase_root_word = root_word.lower()

    for j in lowercase_list:
        if j in lowercase_root_word or lowercase_root_word in j:
            same_word.append(j)

    return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('DisAblement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
