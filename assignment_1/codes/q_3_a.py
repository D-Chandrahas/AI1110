from sympy import pi,simplify,sin,cos
from numpy import array

if __name__ == "__main__":
    a = pi/4
    matrix1 = array([[sin(a),-cos(a)],[cos(a),sin(a)]])
    matrix2 = array([[cos(a),sin(a)],[-sin(a),cos(a)]])
    matrix1 = matrix1 * sin(a)
    matrix2 = matrix2 * cos(a)
    answer = array(simplify(matrix1 + matrix2))
    print(answer)
