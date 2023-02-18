Questions and Answers of Quiz week 1

Question 8
What is the value of a after these three bitwise operations (in hexadecimal)?

1. unsigned short a = 0xFFFF;
2. a = ~( a ^ ( a<<4 ) );

Answer: Since a = 0xFFFF = 1111 1111 1111 1111 
        a<<4 = 1111 1111 1111 0000 
        and a ^ (a<<4) =>as following where ^ is the XOR operation (different bit produces 1) 

          1111 1111 1111 1111 
        ^ 1111 1111 1111 0000
          ____________________
          0000 0000 0000 1111
          ____________________
        Now ~( a ^ ( a<<4 ) ) is 1111 1111 1111 0000 which is [0xFFF0]

Question 9
What is the following unsigned binary number in decimal, 0b110101101?

Answer: 1 1010 1101 = 256 + 128 + 0 + 32 + 0 + 8 + 4 + 0 + 1   = 429


Question 12
What is the following signed 2’s complement binary number in decimal, 0b110101101?

Answer:  1 1010 1101 (first bit is sign bit)
           0101 0010
                   1
         ___________
           0101 0011  =  64 + 0 + 16 + 0 + 0 + 2 + 1 = -83 (sign bit is 1)

