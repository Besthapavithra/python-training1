def leftover(a,b):
    left=" "
    remove=set(b)
    
    for ch in a:
        
        if ch not in remove:
            
            
            left+=ch
            
    if left:
                
        print(left)
               
    else:
        print("empty")
            
a="ABCDEF"
b="BDEF"
leftover(a,b)
