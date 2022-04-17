
#TODO Add V+ing, V+out and,..,  after "+"" for confusion and find swear words more.

#* Import Module *#
import json

#* functions *#
def find(text:str):
    #* Step 1: Contact JSON file *#
    FILE = open('swear_words.json', 'r')
    JSONFILE = json.loads(FILE.read())

    #* Step 2: Text to list, and find any swear words*#
    #TODO the text after text small, recaver to Narmal or as it was. 

    text = text.lower()
    textTOlist = text.split(" ")
    swears = list()

    for i in range(len(textTOlist)):
        if textTOlist[i] in JSONFILE:
            swears.append(i)
    return [swears,textTOlist]


def confusion(SwearWords:list):
    #* Step 1: Sett all value from find *#
    positionWords, Text = SwearWords[0], SwearWords[1]

    #* Step 2: Confusion all swear words in text *# 
    for i in range(len(positionWords)):
        Text[positionWords[i]] = "*"

    #* Step 3: return text after confusion *#
    return print(" ".join(Text))


#* RUN *#
text = input("Enter any word > ")
confusion(find(text))
