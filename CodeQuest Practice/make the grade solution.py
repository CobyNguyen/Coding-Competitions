from typing import NamedTuple, Tuple, Set, List, Dict, Sequence, NewType
import sys
from io import StringIO
#from decimal import Decimal
import decimal as _decimal
#import math
#from datetime import datetime

GRADE_THRESHOLDS = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]
StudentAnswers = NamedTuple('StudentAnswers', [('name', str), ('answers', List[str])])

# for testing:
#s = StringIO("""1
#3 ABCDDCBA
#Bob ABCDDDDD
#Sarah ABCDDCCC
#Kris AACDDCBA
#""")
#sys.stdin = s

# for testing
#file = open("C:/Users/hmendenh/Desktop/temp/sample-Make The Grade.2.in", "r")
#sys.stdin = file

def round2(number, ndigits=None):
    """
    Implementation of Python 2 built-in round() function.
    Rounds a number to a given precision in decimal digits (default
    0 digits). The result is a floating point number. Values are rounded
    to the closest multiple of 10 to the power minus ndigits; if two
    multiples are equally close, rounding is done away from 0.
    ndigits may be negative.
    See Python 2 documentation:
    https://docs.python.org/2/library/functions.html?highlight=round#round
    """
    if ndigits is None:
        ndigits = 0

    if ndigits < 0:
        exponent = 10 ** (-ndigits)
        quotient, remainder = divmod(number, exponent)
        if remainder >= exponent // 2 and number >= 0:
            quotient += 1
        return float(quotient * exponent)
    else:
        exponent = _decimal.Decimal("10") ** (-ndigits)

        d = _decimal.Decimal.from_float(number).quantize(
            exponent, rounding=_decimal.ROUND_HALF_UP
        )

        return float(d)

n_cases = int(sys.stdin.readline())

for case_number in range(n_cases):

    f: List[str] = sys.stdin.readline().rstrip().split(" ")
    #n_students, correct_answers = (int(f[0]), list(f[1]))
    n_students = int(f[0])
    correct_answers = list(f[1])
    print(f"{n_students=} {correct_answers=}")
    #print("n_students: ", n_students)
    #print("correct_answers: ", correct_answers)

    students: List[StudentAnswers] = []
    for n in range(n_students):
        f = sys.stdin.readline().rstrip().split(" ")
        student = StudentAnswers(f[0], list(f[1]))
        #print("student:", student)
        students.append(student)

    #print(f"{students=}")

    for student in students:
        students_correct_answers = list(map(lambda student_answer, correct_answer: student_answer == correct_answer, student.answers, correct_answers))
        #print("students_correct_answers: ", students_correct_answers)
        count_of_students_correct_answers = students_correct_answers.count(True)
        students_percentage_of_correct_answers = (count_of_students_correct_answers / len(correct_answers)) * 100
        for grade_threshold, grade_letter in GRADE_THRESHOLDS:
            if students_percentage_of_correct_answers >= grade_threshold:
                break
        print(f"{student.name} {round2(students_percentage_of_correct_answers, 1):.1f}% {grade_letter}")
