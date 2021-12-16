# Example to check performance
# To find array value 'nemo' O(n)
import time
start_time = time.time()
nemo = ['nemo']
everyone = ['dory', 'sfsdf', 'sdfdsf', 'sdfdsf', 'sfds',
            'sda', 'sdfdf', 'data', 'nemo', 'dfaf', 'dfdf', 'df']


def find_nemo(array):

    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO')


find_nemo(everyone)  # more time
find_nemo(nemo)  # less time

# Output:
# Found NEMO
# Time taken for find_nemo is 0.0000443
# Found NEMO
# Time taken for find_nemo is 0.0000291

# To print text O(1)
boxes = [0, 1, 2, 3, 4, 5]


def log_first_Two_boxes(boxes):
    print(boxes[0])  # O(1)
    print(boxes[3])  # O(1)


log_first_Two_boxes(boxes)  # O(2)


# Excesise : What is the Big O of the below function? (Hint, you may want to go line by line)
def funChallenge(data):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(data)):  # O(n)
        anotherFunction()  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)

    return a  # O(1)


def anotherFunction():
    pass


funChallenge(boxes)
# funChallenge() = O(1)+O(1)+O(1)+O(n)+O(n)+O(n)+O(n)
# funChallenge() = O(3+4n) => O(n)

# What is the Big O of the below function? (Hint, you may want to go line by line)


def anotherFunChallenge(data):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)
    for i in range(data):  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(data):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoAmI = "I don't know"  # O(1)


anotherFunChallenge(100)
# anotherFunChallenge() = O(n)+O(n)+O(n)+O(n)+O(n)+O(n)+O(n)+O(1)+O(1)+O(1)+O(1)
# anotherFunChallenge() = O(4+7n) => O(n)


# here we larn to remove constants in big 0
def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = len(items)//2  # O(1)
    index = 0

    while index < middle_index:  # O(n/2) because it iterates half
        print(items[index])
        index += 1

    for i in range(100):  # O(100)
        print("Hi!! Boi")


print_first_item_then_first_half_then_say_hi_100_times(everyone)

# O(1 + n/2 + 100)
# O(n + 1) 101 => remove 1 and, n/2 => n => O(n)

# O(2n) => O(n)


# Log all pairs of the list


def log_all_pairs_of_array(pairs):
    for i in range(len(pairs)):  # O(n^n)
        for j in range(len(pairs)):  # O(n)
            print("[{0},{1}]".format(pairs[i], pairs[j]))


pairs = [1, 2, 3, 4, 5]
log_all_pairs_of_array(pairs)  # O(n^n) => O(n^2)


# To print number and sum

def print_all_numbers_then_all_pair_sums(numbers):

    print('These are the numbers : ')
    for i in numbers:  # O(n)
        print(i)

    print('And these are their sums : ')
    for i in numbers:  # O(n^n)
        for j in numbers:  # O(n)
            print(i+j)


numbers = [43, 4, 324, 2, 34, 23, 4, 23, 4, 3, 43, 24234,
           45, 34, 5, 23, 45, 45, 3, 3, 2, 34, 23, 4, 234, 2, 3, 3]

print_all_numbers_then_all_pair_sums(numbers)
# O(n^2 + n) => O(n^2) drop non-domenent term n
end_time = time.time()
print("Time taken for find_nemo is {0:.7f}".format(end_time - start_time))
