def ls(n):

    nums = [45, 55, 60, 37, 100, 105, 220]
    

    for x in nums: 
        if x % n ==0:
            print(x/n)
        else:
            print('Оно с остатком')
