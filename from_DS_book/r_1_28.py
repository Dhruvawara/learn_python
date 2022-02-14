"""
The p-norm of a vector v = ( v1, v2, . . . , vn) in n-dimensional space is 
defined as ‖v‖= p√v1^p + v2^p + ···+ vn^p .
For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the
Euclidean norm of a two-dimensional vector with coordinates (4, 3) has a
Euclidean norm of √4^2 + 3^2 = √16 + 9 = √25 = 5. Give an implementation 
of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of number.
"""


def main():
    v = (-5, 2, 9,  7,  6, 4, -3, 0, 5, 1)
    print(p_norm(v, 5))


def p_norm(v, p):
    return sum([abs(value) ** p for value in v]) ** (1 / p)


if __name__ == '__main__':
    main()
