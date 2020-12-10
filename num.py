print("Select one operation -\n" "1. DEC TO BIN \n" "2. DEC TO HEX\n" "3. DEC TO OCT")
select = int(input("Select operations form 1, 2, 3:"))
dec = int(input('Enter your Decimal Number : '))
if select == 1:
     print( dec, "in binary = " , bin(dec))
elif select == 2:
        print( dec, "in octadecimal = " , oct(dec))
elif select == 3:
        print( dec, "in hexadecimal = ", hex(dec))
else:
       print("Invalid input")
