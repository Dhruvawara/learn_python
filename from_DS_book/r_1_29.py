"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""

from itertools import permutations

def main():
    print([''.join(permut) for permut in permutations('c','a','t','d','o','g')])

if __name__ == '__main__':
    main()
