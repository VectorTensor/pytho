my_list = [1,2,3,4,5,6,7,8,9,10,11]
n=int(input("Enter the number you want to search: "))
search = False
ans=0
while search==False:
    l=len(my_list)
  # print(f"list {l} ")
    if l % 2 == 0:
        if n>my_list[(int(l/2)-1)]:
            ans=ans+(int(l/2))
            del my_list[0:int(l/2)]
        
        elif n<my_list[(int(l/2)-1)]:
            del my_list[(int(l/2)-1):l]   
        else:
            ans=ans+int(l/2)-1
            search=True 

    else:
        
        if n>my_list[int(l/2)]:
            ans=ans+int(l/2)+1
            del my_list[0:(int(l/2)+1)]
        
        elif n<my_list[int(l/2)]:
            del my_list[int(l/2):l]   
        else:
            ans=ans+int(l/2) 
            search=True 

       
print(f"The number is in the index {ans}")
   

    
