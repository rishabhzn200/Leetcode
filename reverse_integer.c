/*
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer 
overflows.
*/



int reverse(int x) {
    
    int len = sizeof(x);
    int rev = 0, b, oldr, i, p=0;
    int isNeg = 0;   //assume number is positive
    
    if(x & 0x80000000)      //check the MSB
        isNeg = 1;          //if MSB is 1, number is negative
    //    return 0;
    
    if(isNeg)               //if number is negative, take absolute of number
    {
        x = -x;
    }
    
    oldr = rev;
    while(x > 0)            //reverse the number. It might overflow as well. How to check
    {
        b = x%10;
        //Another way to do this and check overflow: rev = rev*10 + b;
        
        p = 0;
        for(i=0;i<10;i++)
        {
            p += rev;
            if(p & 0x80000000 || oldr > p)        //if last bit gets set, number becomes negative.
            {
                return 0;
            }
            oldr = p;
        }
        rev = p;
        
        
        rev += b;
        
        if(rev & 0x80000000 || oldr > rev)        //if last bit gets set, number becomes negative.
        {
            return 0;
        }
        x = x/10;
    }
    
    if(isNeg)
        rev = -rev;
    
    return rev;
}