#!/usr/bin/env python
'''
2. Create an IP address converter (dotted decimal to binary):

    A. Prompt a user for an IP address in dotted decimal format.

    B. Convert this IP address to binary and display the binary result on the
screen (a binary string for each octet).

    Example output:

    first_octet    second_octet     third_octet    fourth_octet
         0b1010       0b1011000          0b1010         0b10011

'''

network = raw_input("\n\nEnter an IP address: ")

octets = network.split(".")

first_octet_bin = bin(int(octets[0]))
second_octet_bin = bin(int(octets[1]))
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

print "\n\n%15s %15s %15s %15s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%15s %15s %15s %15s\n" % (first_octet_bin, second_octet_bin,
                                 third_octet_bin, fourth_octet_bin)
