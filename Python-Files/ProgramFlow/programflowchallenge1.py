__author__ = 'dev'
# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.


ip = input("Please enter an IP address: ")

segments = 0
firstSegment = False

for num in ip:
    if num in "." and firstSegment:
        segments += 1
    if num in "012345678":
        if segments == 0:
            segments += 1
        firstSegment = True
print("Number of segments: {}".format(segments))

if segments > 0:
    segmentLength = 0
    firstSegment = False
    segNum = 0
    for num in ip:
        if num in "." and firstSegment:
            print("Segment {0} has length of {1} digits".format(segNum, segmentLength))
            segNum += 1
            segmentLength = 0
        if num in "012345678":
            firstSegment = True
            if segNum == 0:
                segNum += 1
                segmentLength = 0
            segmentLength += 1
        # if segmentLength == 0 and segNum > 0:
    print("Segment {0} has length of {1} digits".format(segNum, segmentLength))



# for i in range(0, segments):
#     print("Segment[{0}] has length {1}".format(i, segmentLength[i]))
