"""
Vowel harmony is a phenomenon in some languages.
It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")"

Your goal is to create a function instrumental() which returns the valid form of a valid Hungarian word w in instrumental case 
i. e. append the correct suffix -vel or -val to the word w based on vowel harmony rules.

Vowel Harmony Rules (simplified)
Front vowels: e, é, i, í, ö, ő, ü, ű

Back vowels: a, á, o, ó, u, ú

Vowel pairs (short -> long): a -> á, e -> é, i -> í, o -> ó, u -> ú, ö -> ő, ü -> ű

Digraphs: sz, zs, cs

Word ends with a vowel
Change the ending vowel from short to long form.
Append the suffix:
vel if the ending vowel is a front vowel
val if the ending vowel is a back vowel
Word ends with a consonant
Step one
Default case: Double the ending consonant and continue with step two.
Special case: If the word ends with a digraph then double the first letter (e. g. sz -> ssz)
Step two
Append the suffix:

el if the last vowel is a front vowel
al if the last vowel is a back vowel

All strings are unicode strings.
The tests don't contain:
exceptional cases like kávé -> kávéval
words ending with doubled consonants (e. g. tett)
words ending with y
words ending with u, i
"""
def instrumental(word: str) -> str:
    front = {'e': 'é', 'i': 'í', 'ö': 'ő', 'ü': 'ű'}
    back = {'a': 'á', 'o': 'ó', 'u': 'ú'}
    
    suffix = {'front': 'vel', 'back': 'val'}
    digraphs = {'sz': 'ssz', 'zs': 'zzs', 'cs': 'ccs'}

    l_front = []
    l_back = []

    if word[-1] in front:  # ≡ if word.endswith(tuple(front.keys()))
        # word = word.replace() # replaces changes all instances
        word = word[:-1] + front[word[-1]]
        word += suffix['front']
    elif word[-1] in front.values():
        word += suffix['front']
    elif word[-1] in back:
        word = word[:-1] + back[word[-1]]
        word += suffix['back']
    elif word[-1] in back.values():
        word += suffix['back']
    else:
        if word[-2:] in digraphs:
            word = word.replace(word[-2:], digraphs[word[-2:]])
        else:
            word += word[-1]
        for i in front:
            l_front.append(word.rfind(i))
        for i in front.values():
            l_front.append(word.rfind(i))
        for i in back:
            l_back.append(word.rfind(i))
        for i in back.values():
            l_back.append(word.rfind(i))
        if max(l_front) > max(l_back):
            word += 'el'
        elif max(l_back) > max(l_front):
            word += 'al'
    return word

# def instrumental_(word: str) -> str:
#     vowels = {'front': {'e': 'é', 'i': 'í', 'ö': 'ő', 'ü': 'ű'},
#               'back': {'a': 'á', 'o': 'ó', 'u': 'ú'}}
#     v_ = []
#     [[k, v] for k, v in vowels.items()]

#     suffix = {'front': 'vel', 'back': 'val'}
#     digraphs = {'sz': 'ssz', 'zs': 'zzs', 'cs': 'ccs'}

#     l_front = []
#     l_back = []

#     end = word[-1]

#     # if end in vowels:


#     if word[-1] in front:  # ≡ if word.endswith(tuple(front.keys()))
#         # word = word.replace() # replaces changes all instances
#         word = word[:-1] + front[word[-1]]
#         word += suffix['front']
#     elif word[-1] in front.values():
#         word += suffix['front']
#     elif word[-1] in back:
#         word = word[:-1] + back[word[-1]]
#         word += suffix['back']
#     elif word[-1] in back.values():
#         word += suffix['back']
#     else:
#         if word[-2:] in digraphs:
#             word = word.replace(word[-2:], digraphs[word[-2:]])
#         else:
#             word += word[-1]
#         for i in front:
#             l_front.append(word.rfind(i))
#         for i in front.values():
#             l_front.append(word.rfind(i))
#         for i in back:
#             l_back.append(word.rfind(i))
#         for i in back.values():
#             l_back.append(word.rfind(i))
#         if max(l_front) > max(l_back):
#             word += 'el'
#         elif max(l_back) > max(l_front):
#             word += 'al'
#     return word
