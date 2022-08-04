
#* import module
from random import randint as rand
import json
import sys

#* Values
try_error = 0
try_agen  = 3

#* functions *#
def read_json (target:str, data:str):
    #* step one: read json file
    file     = open(f'./data.json', 'r')
    JSONFILE = json.loads(file.read())

    #* step tow: import the vlaue and return
    return JSONFILE[target][data]


def generator(level:str, loger:int):
    if loger >= 8:
        #* step one: set a values
        EMH = read_json("level", level)
        length   = len(EMH)
        password = str()

        #* step tow: Generate a password
        for _ in range(loger):
            password += EMH[rand(0, length-1)]
        return password, len(password)
    else:
        return False

def check_Error (vlu:int, stop:int):
    if vlu == stop:
        return True
    else:
        print(f"[check_Error: #{try_error}] Sorry, you entered the wrong system\n -------")

#? level: It is he who sets the difficulty level of the password.
#? Where 1 means easy, 2 means medium and 3 difficult
def level(level:str):
    #* step one: A know the difficulty level
    lengthTe = len(level)
    # print(f"[level - output] lengthTe: {lengthTe}")
    #* step tow: Sets the difficulty level of the password, and return a value
    try:
        if lengthTe in [1, 2, 3] and "f" in level:
            if lengthTe == 1:
                # print(f"[level - output] f")
                return "E"
            elif lengthTe == 2:
                # print(f"[level - output] ff")
                return "M"
            else:
                # print(f"[level - output] fff")
                return "H"
        else:
            print("[level - Erorr] Sorry, you entered the wrong system")
    except TypeError:
        print("[level - TypeError] Sorry, you entered the wrong system")

#*RUNING*#
print("\t[PASSWORD GENERATOR]")
while True:
    try:
        #* step one: Enter the input required
        if sys.argv[1:3]:
            newpass = sys.argv[1:3]
        else:
            newpass = input("Enter the level the password and the length, like -> (level(f:E+f:M+f:H) length of password) \n > ").split(" ")
        
        #? If the second field is required (password length), this will automatically be added.
        try:
            if newpass[1] == "": newpass[1] = 8
        except:
            newpass += " "
            newpass[1] = 8

        #* step tow: Set a vales
        lev = level(newpass[0])
        Gen = generator(lev, int(newpass[1]))
        
        #* step three: Error detection and generation
        if Gen == False or newpass == "":
            try_error += 1
            if check_Error(try_error, try_agen):
                break
            else:
                continue
        else:
            print(generator(lev, int(newpass[1])))
            break
    except IndexError:
        try_error += 1
        if check_Error(try_error, try_agen):
            print("[Erorr - IndexError] Sorry, you entered the wrong system")
            break
    except KeyError:
        try_error += 1
        if check_Error(try_error, try_agen):
            print("[Erorr - KeyError] Sorry, you entered the wrong system")
            break
                
