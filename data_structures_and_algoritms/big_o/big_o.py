# Example to check performance
# To find array value 'nemo' O(n)
import time
nemo = ['nemo']
everyone = ['dory', 'sfsdf', 'sdfdsf', 'sdfdsf', 'sfds',
            'sda', 'sdfdf', 'data', 'nemo', 'dfaf', 'dfdf', 'df']


def find_nemo(array):
    start_time = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO')
    end_time = time.time()
    print("Time taken for find_nemo is {0:.7f}".format(end_time - start_time))


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
    a = 5# O(1)
    b = 10# O(1)
    c = 50# O(1)
    for i in range(data):# O(n)
        x = i + 1# O(n)
        y = i + 2# O(n)
        z = i + 3# O(n)

    for j in range(data):# O(n)
        p = j * 2# O(n)
        q = j * 2# O(n)

    whoAmI = "I don't know"#O(1)

anotherFunChallenge(100)
# anotherFunChallenge() = O(n)+O(n)+O(n)+O(n)+O(n)+O(n)+O(n)+O(1)+O(1)+O(1)+O(1)
# anotherFunChallenge() = O(4+7n) => O(n)
