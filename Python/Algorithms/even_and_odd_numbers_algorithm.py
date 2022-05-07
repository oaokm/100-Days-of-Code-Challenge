def main(array:list):
    #* Step 0: assigning variables to the function
    array_filter    = list()
    number_of_pawer = [2,3,4,5,6,7,8,9]
    #* Step 1: filter a numbers
    for i in range(len(array)):
        #* Step 2: exclude any number less than one
        if array[i] > 1:
            #* Step 3: ensure that the number is an even number
            if array[i] % 2 == 0:
                #? Note: "continue" because we do not want the even number in the array after the filter
                continue
        
            #* Step 4: exclude odd numbers
            elif array[i] % 2 == 1:
            #* Step 5: putting a for loop to expel the odd numbers
                for j in range(len(number_of_pawer)):
                    #* Step 6: It is known that odd numbers are only divisible by themselves and one,
                    #* so here he is decomposing a matrix (analsys_number) and dividing it into two parts : 
                    #* (an_part_o[analsys number one] and an_part_t[analsys number two]).

                    analsys_number       = str(array[i] / number_of_pawer[j]).split(".")
                    an_part_o, an_part_t = int(analsys_number[0]), int(analsys_number[1])

                    #* Step 7: A conditional order, one of the conditions of prime numbers is that the number is 
                    #* integer and greater than one.
                    if (an_part_o != 1 or 0) and an_part_t == 0:
                        #* Step 8: Add the required after filtering
                        array_filter.append(array[i])
                        break
                    else:
                        continue
            else:
                continue
        else:
            #* Step 8: Add the required after filtering
            array_filter.append(array[i])
    #* Step 9: return after filtring
    return array_filter

#* Step 10: RUNING
array = [1,2,4,5,9,11]
print(f"----[Befor Filter]----\n{array}\n----[After Filter]----\n{main(array)}")
