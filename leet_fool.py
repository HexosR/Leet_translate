SUBSTITUTIONS = [['a', '4'], ['b', '8'], ['c', '['], ['d', ')'], ['e', '3'],
                 ['f', '|='], ['g', '6'], ['h', '#'], ['i', '1'], ['j', '_|'],
                 ['k', '|<'], ['l', '|_'], ['m', '/\\/\\'], ['n', '/\\/'],
                 ['o', '0'], ['p', '|*'], ['q', '9'], ['r', '|2'], ['s', '5'],
                 ['t', '7'], ['u', '(_)'], ['v', '\\/'], ['w', '\\/\\/'],
                 ['x', '><'], ['y', '`/'], ['z', '2']] 

def get_leet_match(character):
    ''' (str) -> str

    Return the leet symbol corresponding to the imput character
    '''
    pass

def encoder(text):
    ''' (str) -> str

    Return the input text converted into leet text.
    '''
    tekst = text.lower()
    print(tekst)
    a_list = []
    chars = []
    for a in tekst:
        a_list.append(a)
    for i in range(len(a_list)):
        for j in range(len(SUBSTITUTIONS)):
            if(ord(a_list[i]) >= 97 and ord(a_list[i]) <= 122):
                if (a_list[i] == SUBSTITUTIONS[j][0]):
                    chars.append(SUBSTITUTIONS[j][1])
            else:
                chars.append(a_list[i])
                break
    here = ''.join(chars)
    return here

    
    

def test_encoder():
    print(encoder("What happened when the strawberry attempted to cross the\
road? There was a traffic jam!"))
    print(encoder("If you can read this you really need to get a life!"))
    
    
