#Steven Zhou
#BinHexDecimalConvert
#2018/6/19

print("---------------------------------------------------------------------------------------------------------------------------")
while True:
  print("Welcome to the Binary, Hexadecimal and Decimal Converter! \n")
  Choice = input("What do you want to convert? \n - Binary to Decimal (type in 'bd') , \n - Hexadecimal to Decimal (type in 'hd') , \n - Decimal to Binary (type in 'db') , \n - Decimal to Hexadecimal (type in 'dh') , \n - Binary to Hexadecimal (type in 'bh') , \n - Hexadecimal to Binary (type in 'hb') ? ")
  print("---------------------------------------------------------------------------------------------------------------------------")
  while x == 0:
    print("\n"*5)
    if Choice == 'bd':
      BinNumber = input("Please type in the number you want to convert from binary to decimal:")
      print("\n")
      print("Your number is:",int(BinNumber ,2))
      print("---------------------------------------------------------------------------------------------------------------------------")
    if Choice == 'hd':
     HexNumber = input("Please type in the number you want to convert from hexadecimal to decimal:")
     print("\n")
     print("Your number is:",int(HexNumber ,16))
     print("---------------------------------------------------------------------------------------------------------------------------")
    if Choice == 'db':
      DecNumber = input("Please type in the number you want to convert from decimal to binary:")
      print("\n")
      print("Your number is:",bin(int(DecNumber)))
      print("---------------------------------------------------------------------------------------------------------------------------")
    if Choice == 'dh':
      DecNumber = input("Please type in the number you want to convert from decimal to hexadecimal:")
      print("\n")
      print("Your number is:",hex(int(DecNumber)))
      print("---------------------------------------------------------------------------------------------------------------------------")
    if Choice == 'bh':
      BinNumber = input("Please type in the number you want to convert from binary to hexadecimal:")
      print("\n")
      print("Your number is:",hex(int(BinNumber ,2)))
      print("---------------------------------------------------------------------------------------------------------------------------")
    if Choice == 'hb':
      HexNumber = input("Please type in the number you want to convert from hexadecimal to binary:")
      print("\n")
      print("Your number is:",bin(int(HexNumber ,1 6)))
      print("---------------------------------------------------------------------------------------------------------------------------")
