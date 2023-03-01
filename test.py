def her(nums) :
    zero , one , two , i = [] , [] , [] , 0

    while (i<len(nums)) :
        print(i)
        print('Listaa : ',nums)
        if nums[i]<1 :
            nums.pop(i)
            nums.insert(0,0)
            i+=1
        elif nums[i]>1 :
            nums.pop(i)
            nums.append(2)
        else :
            i+=1



her([2,0,2,1,1,0])