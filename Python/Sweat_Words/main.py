
#// Add V+ing, V+out and,..,  after "+"" for confusion and find swear words more.

#* Import Module *#
    import json

#! functions *#
#* LangFIND: is option for exploration language used it  *#
#TODO You'll have to complete this functon#
def langFIND():
    FILE = open('data/swear_words.json', 'r')
    JSONFILE = json.loads(FILE.read())


#// You'll have to create a word prediction system for this function and the tangled words#
#? Tangled words for example: "[word]," or "0[word]0", etc.
def text_analysis(txt:str):
    FILE = open('swear_words.json', 'r')
    JSONFILE = json.loads(FILE.read())

    filter_words = list()
    for i in range(len(txt)):
        text_analy = txt
        if text_analy[0:i] in JSONFILE["EN"]["swear"]:
            filter_words.append(text[0:i])
            return True
        else:
            None


#* find: is option for exploration sewar words *#
def find(text:str):
    #* Step 1: Contact JSON file *#
    FILE = open('swear_words.json', 'r')
    JSONFILE = json.loads(FILE.read())

    #* Step 2: Text to list, and exploration any swear words*#
    #// the text after text small, recaver to Narmal or as it was. 

    text = text.lower()
    textTOlist = text.split(" ")
    swears = list()

    for i in range(len(textTOlist)):
        if textTOlist[i] in JSONFILE["EN"]["swear"]:
            swears.append(i)
        elif text_analysis(textTOlist[i]):
            swears.append(i)
        else:
            None
    return [swears,textTOlist]


def confusion(SwearWords:list):
    #* Step 1: Sett all value from find *#
    positionWords, Text = SwearWords[0], SwearWords[1]

    #* Step 2: Confusion all swear words in text *# 
    for i in range(len(positionWords)):
        Text[positionWords[i]] = "*"*len(Text[positionWords[i]])

    #* Step 3: return text after confusion *#
    return print(" ".join(Text))


#* RUN *#

text = input("Enter any word > ")
confusion(find(text))
    
