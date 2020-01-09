#!/usr/bin/python3

import sys
import math

def display_help():
    print("USAGE")
    print("\t./108trigo fun a0 a1 a2...\n")
    print("DESCRIPTION\n")
    print('\tfun\tfunction to be applied among at least "EXP", "COS", "SIN", "COSH" and "SINH"\n')
    print("\tai\tcoeficients of the matrix")
    sys.exit(0)

def my_exp(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 150):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, i), math.factorial(i)))
    return tmp

def my_cos(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 17):
        if i % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i), math.factorial(2 * i)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * i), math.factorial(2 * i)))
    return tmp

def my_sin(tab):
    tmp = tab
    for i in range(1, 17):
        if i % 2 == 0:
            tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), math.factorial(2 * i + 1)))
        else:
            tmp = sub_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), math.factorial(2 * i + 1)))
    return tmp

def my_cosh(tab):
    tmp = identity_mat(len(tab))
    for i in range(1, 17):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i), math.factorial(2 * i)))
    return tmp

def my_sinh(tab):
    tmp = tab
    for i in range(1, 17):
        tmp = add_mat(tmp, div_mat(pow_mat(tab, 2 * i + 1), math.factorial(2 * i + 1)))
    return tmp

def tab_fcts():
    fct_tab = [my_exp, my_cos, my_cosh, my_sinh]

def identity_mat(n):
    tmp = []
    for i in range(n):
        tab = []
        for j in range(n):
            tab.append(1 if j == i else 0)
        tmp.append(tab)
    return tmp

def init_mat(n, k):
    tmp = []
    for i in range(n):
        tab = []
        for j in range(n):
            tab.append(k)
        tmp.append(tab)
    return tmp

def mat_mult(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        tab = []
        for j in range(len(mat2[0])):
            a = 0
            for k in range(len(mat1[0])):
                a += mat1[i][k] * mat2[k][j]
            tab.append(a)
        tmp.append(tab)
    return tmp

def add_mat(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] + mat2[i][j])
        tmp.append(c)
    return tmp

def sub_mat(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] - mat2[i][j])
        tmp.append(c)
    return tmp

def pow_mat(mat, n):
    tmp = mat
    for i in range(n - 1):
        tmp = mat_mult(tmp, mat)
    return tmp

def div_mat(mat, k):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] /= k
    return mat

def check_parameters():
    if "--help" in sys.argv or "-h" in sys.argv:
        display_help()
    if len(sys.argv) <= 2 \
            or sys.argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        print("Bad format, see --help, -h, or man entry for more info",
              file=sys.stderr)
        sys.exit(84)
    try:
        for i in range(2, len(sys.argv)):
            sys.argv[i] = float(sys.argv[i])
    except ValueError:
        print("Argument %d (%s) must be a number"
              % (i, sys.argv[i]), file=sys.stderr)

def error_management():
    i = len(sys.argv) - 2
    sqi = math.trunc(math.sqrt(i))
    if math.trunc(math.sqrt(i)) ** 2 != i:
        print("Not enough parameters to create a matrix",
              file = sys.stderr)
        sys.exit(84)
    return sqi

def print_matrix(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%.2f%c" % (tab[i][j],
                              '\t' if (j != len(tab[i]) - 1) else '\n'),
                  end="")

def launch_func(tab):
    args = ["EXP", "COS", "SIN", "COSH", "SINH"]
    fct_tab = [my_exp, my_cos, my_sin, my_cosh, my_sinh]
    for i in range(len(fct_tab)):
        if sys.argv[1] == args[i]:
            tab = fct_tab[i](tab)
    return tab

def main():
    tab = []
    check_parameters()
    nb = error_management()
    for i in range(int(nb)):
        tab.append([])
        for j in range(int(nb)):
            tab[i].append(sys.argv[i * int(nb) + j + 2])
    tab = launch_func(tab)
    print_matrix(tab)

if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception:
        sys.exit(84)

