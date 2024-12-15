# Task 6 solution : 

math_score=int(input("Enter your math score: "))
science_score=int(input("Enter your science score: "))
english_score=int(input("Enter your english score: "))

if math_score >= 90 and science_score >=90 and english_score >= 90:
    print("Your performance is Excellent")
elif math_score >= 75 and science_score >= 75 and english_score >= 75:
    print("Your performance is Good")
else:
    print("Your performance Needs Improvement")