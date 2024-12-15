# Task 6 solution : flag
math_score=int(input("Enter your math score: "))
science_score=int(input("Enter your science score: "))
english_score=int(input("Enter your english score: "))

flag=""

if math_score >= 90 and science_score >= 90 and english_score >= 90:
    flag="Excellent"
elif math_score >= 75 and science_score >= 75 and english_score >= 75:
    flag="Good"
else:
    flag="Need Improvement"

print(f"your performance is {flag}")
