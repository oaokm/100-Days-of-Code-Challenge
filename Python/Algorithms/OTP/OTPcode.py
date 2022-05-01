#* import module *#
from random import randint


def OTP():
    #* step 1: Sett values 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=+/*.'
    OTP = str()
    length = len(string)

    #* step 2: Text length is random & return OTP value
    for i in range(randint(6, 10)):
        OTP += string[randint(0, length-1)]
    
    return OTP

#* print OTP value
print(f'Password OTP: {OTP()}')
