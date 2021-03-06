
def prefix_sum(A):
    """Prefix Sums: bla bla bla....
    """
    n = len(A)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k -1]
    return P

def count_total(P, x, y):
    """Count Total: bla bla bla
    """
    return P[y + 1] - P[x]


def passing_cars(A):
    """Passing cars...
    """
    total = 0
    for i in range(len(A)):
        if A[i] != 0:
            continue

        for j in range(i + 1, len(A)):
            if A[j] == 1:
                print ("({0}, {1})".format(i, j))
                total += 1

    return total


def foo():
    print("bar.com")


def call_ftr1():
    print("Calling feature1")


if __name__ == '__main__':
    #A = [2, 6, 2, 7, 5, 9]
    A = [0, 1, 0, 1, 1]
    P = prefix_sum(A)
    print(A)
    print(P)
    print(passing_cars(A))
