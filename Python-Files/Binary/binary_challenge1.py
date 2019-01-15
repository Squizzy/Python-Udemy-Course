# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

# inp_num = int(input("Please enter a decimal number between 0 and 65535: "))
#
# dec_num = 0 + inp_num
# bin_num = ""
# current_bit = 0
# print("in dec: {0:>2} \tin bin: {0:>08b} \tin octal: {0:>05o}".format(dec_num))
#
# for digit in range(15, -1, -1):
#     current_bit = dec_num // 2 ** digit
#     #    print("position {}\t{}".format(digit, current_bit))
#     if bin_num != "" or current_bit != 0:
#         bin_num += str(current_bit)
#     dec_num %= 2 ** digit
#
# print("binary value: {}".format(bin_num))
#
# dec_num = 0 + inp_num
# oct_num = ""
# current_octal = 0
#
# for cur_digit in range(0, 8):
#     digit = 7 - cur_digit
#     current_octal_remain = dec_num % 8 ** digit
#     current_octal = dec_num // 8 ** digit
#     #    print("position: {}\tremainder: {}\toctal: {}".format(digit, current_octal_remain, current_octal))
#     if current_octal_remain != dec_num or oct_num != "":
#         oct_num += str(current_octal)
#     dec_num %= 8 ** digit
# # oct_num += str(current_octal)
# print("octal value: {}".format(oct_num))

powers = []
for power in range(5, -1, -1):
    powers.append(8 ** power)
print(powers)

dec_num = int(input("Please enter a decimal number between 0 and 65535: "))

printing = False

for power in powers:
    bit_val = dec_num // power
    if bit_val != 0 or power == 1:
        printing = True
    if printing:
        print(bit_val, end="")
    dec_num %= power
