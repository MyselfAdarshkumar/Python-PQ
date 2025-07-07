def get_math_grade(sub_math):
    if sub_math >= 90:
        print("  Math grade = A+")
        return 10
    elif sub_math >= 80:
        print("  Math grade = B+")
        return 9
    elif sub_math >= 70:
        print("  Math grade = C+")
        return 8
    elif sub_math >= 60:
        print("  Math grade = D+")
        return 7
    elif sub_math >= 50:
        print("  Math grade = E+")
        return 6
    else:
        print("  You are fail")
        return 0# Example usage
marks = int(input("Enter your Math marks: "))
point = get_math_grade(marks)
print("Grade Point =", point)


