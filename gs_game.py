# generate random number
import random

rn_num = random.randint(1,100)

#print(rn_num)
counter = 1
end_trn = 5

while counter <= end_trn:
    print("Turn :  ",counter,"/",end_trn)
    # get guessed number
    gs_num = input('Guess : ')

    if gs_num == "":
        print('Null is not  a Number !!!')
    elif not gs_num.isdigit():
        print('Not a Number !!!')
    else:
        gs_num = int(gs_num)


# compare two numbers
    if gs_num > rn_num:
        if gs_num - rn_num < 5:
            end_trn += 1
            print("so close")
        else:
            print('too big')
    elif gs_num < rn_num:
        if rn_num - gs_num < 5:
            end_trn += 1
            print("so close")
        else:
            print('too small')
    else:
        print('you win')
        break
    counter += 1

else:
    print('you lose the number was ',rn_num)





