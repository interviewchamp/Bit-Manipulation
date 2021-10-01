# Caeser Cipher Bit Manipulation Example

def add_num(x: int, y: int): 
    ''' 
    Adds a number x by another number y using bitwise operators. 
    :param x:   Any number between 97 and 122. 
    :param y:   Number to add to x. 
    ''' 
    # Iterate till there is no carry   

    while (y != 0): 
        # carry now contains common  
        # set bits of x and y  
        carry = x & y  
        # Sum of bits of x and y where at  
        # least one of the bits is not set  
        x = x ^ y 
        # Carry is shifted by one so that     
        # adding it to x gives the required sum  
        y = carry << 1 
     return x 

def subtract_num(x: int, y: int): 
    ''' 
    Subtracts a number x from another number y using bitwise operators. 
    :param x:   Any number between 97 and 122. 
    :param y:   Number to subtract from y. 
    ''' 
    # Iterate till there is no carry  

    while (y != 0):  
        # borrow contains common   
        # set bits of y and unset  
        # bits of x  
        borrow = (~x) & y  
        # Subtraction of bits of x  
        # and y where at least one  
        # of the bits is not set  
        x = x ^ y  
        # Borrow is shifted by one   
        # so that subtracting it from  
        # x gives the required sum 
        y = borrow << 1       
      return x    
def encrypt_lower_case(letter: str, pattern: int):      
        #Shifts a given character according to the shift pattern in Caeser Cipher algorithm.      
        #:param letter:  Any number between 97 and 122.      
        #:param pattern: Number to add to x.
        
        letter_unicode = ord(letter)      
        # Check if character is a letter between a and z. If not raise ValueError exception.      
        if letter_unicode not in range(97,123):          
            raise ValueError("Error! Input not in allowed range...")      
        result_unicode = add_num(letter_unicode, pattern)      
        
        # If letter exceeds z, shift starts from a again.     
        if result_unicode > 122: 
              diff = subtract_num(result_unicode, 123) 
              result_unicode = add_num(97, diff) 
        return chr(result_unicode) 

plain_letter = input("Enter letter a-z to encrypt: ") 
pattern = input("Enter Ceaser Cipher shift pattern: ") 
print(f"{plain_letter} -> {encrypt_lower_case (plain_letter, int(pattern))}")
