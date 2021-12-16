# printing "Mary had a little lamb"
print("Mary had a little lamb")
# printing formatted string "Its fleece was white as {}.".format("snow")
print("Its fleece was white as {}.".format("snow"))
# printing "And everywhere that Mary went."
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do : print . 10 times

# assigning single characters to variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# at the end print() will put \n but now at end there will be space and next print will be executed there
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)
