#create a function
#pass in int as# parameter
#loop through the range of 100 and 200
#create a conditionof div by seven
#create an 
def divisible_by_seven():
    

    seven=[n for n in range(100,200) if n%7==0] #only prints out the condition and not the value

    print(seven)
divisible_by_seven()
 #programme for finding symmetrical numbers,
 #create a string and find the mid point
 #with the midpoint divide the string into two halves
 #compare the two halves using slicing 
 #if equal word is symmetrical 
def symm(dobi):
    # dobi="originals"
    p=len(dobi)//2
    if dobi[0:p]==dobi[p+1:]:
        print(f"{dobi} is a symmetrical word")
    else:
        print("This is not a symmetrical")
symm("mum")
