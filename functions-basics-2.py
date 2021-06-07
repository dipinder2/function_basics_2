#1. Countdown - recursively
def countdown(num, ret_list):
    if num<0:
        return 0
    ret_list.append(num)
    countdown(num-1,ret_list)
    return ret_list
print(countdown(5,[]))
#2. Print and Return
def print_and_return(l1):
    print(l1[0])
    return l1[1]
print_and_return([1,2])

#3. First Plus Length 
def first_plus_length(l1):
    return l1[0]+len(l1)
print(first_plus_length([1,2,3,4,5]))
#4.Values Greater than Second - iteratively
def values_greater_than_second(l1):
    if len(l1)<2:
        return False
    newlist = list()
    for i in l1:
        if i>l1[1]:
            newlist.append(i)
    print(len(newlist))
    return newlist
print(values_greater_than_second([5,2,3,2,1,4]))
#same solution recursively
def values_greater_than_second_recursive(l1, startidx,new_list):
    if len(l1)<2:
        return False
    if startidx >=len(l1):
        return 
    if l1[startidx]>l1[1]:
        new_list.append(l1[startidx])
    values_greater_than_second_recursive(l1, startidx+1, new_list)
    return new_list
print(values_greater_than_second_recursive([5,2,3,2,1,4], 0 , []))

#5. this length, that value
def length_and_value(l,v):
    l1 = list()
    for i in range(l):
        l1.append(v)
    return l1
print(length_and_value(4,7))
