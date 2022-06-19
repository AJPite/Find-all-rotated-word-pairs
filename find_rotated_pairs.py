def get_ords(s):  # get Unicode of each chr in str, return list of Unicodes
    c_list = []
    for c in s:
        c_list.append(ord(c))
    return c_list

def convert_ords(ords):  # get new str from new ords passed by rotate word
    s = ''
    for o in ords:
        s += chr(o)
    return s

def rotate_word(s, n):  # call get_ords and convert_ords to rotate str by num as specified by find_rotated_pairs
    ords = get_ords(s)
    for i in range(len(ords)):
        ords[i] += n
        if ords[i] > 122:
            ords[i] = 96 + (ords[i]-122)
    rotated = convert_ords(ords)
    return rotated

def find_rotated_pairs(w_list):  # return list of all rotated pairs
    ''' This function creates a dictionary out of all legal crossword words then calls
    rotate word function to rotate each word up until the first letter == 'z' so that it
    doesn't return any duplicate words by looping around the alphabet. If a rotated word
    is in the word dictionary, append the word and the rotated word to the list and return
    the list. A dictionary is used for fast iteration.'''
    d = {}
    v = 0
    for word in w_list:  # create {} out of all words in word list
        v+= 1

    pairs_ls = []  # initialize list to store all rotated pairs
    for word in d:  # rotate each word in {} by steps 1 through (ord('z') - ord(first chr))
        for i in range(122 - ord(word[0])):
            rotated = rotate_word(word, i+1) 
            if rotated in d:  # if rotated word is in d, append both word and rotated word
                pairs_ls.append(word)
                pairs_ls.append(rotated)

    return pairs_ls  # return list of all rotated word pairs
    

fin = open('words.txt')
words = []
for line in fin:
    word = line.strip()
    words.append(word)

pairs = find_rotated_pairs(words)
