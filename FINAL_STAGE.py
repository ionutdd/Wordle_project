print("Apasa 1 daca vrei sa joci jocul Wordle, apasa 0 daca vrei sa il lasi pe calculator sa iti ghiceasca cuvantul:")
n=input("n= ")
while n!="0" and n!="1":
    print("Introdu 0 sau 1")
    n=input("n= ")
n=int(n)
if n==1:
    try:__import__('FIRST_PART_buggy_free.py')
    except:print("Multumim de vizionare!")
else:
    try:__import__('SECOND_PART.py')
    except:print("Multumim de vizionare!")
