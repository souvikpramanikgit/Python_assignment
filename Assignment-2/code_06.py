sub1=int(input("Enter the marks of subject1: "))
sub2=int(input("Enter the marks of subject2: "))
sub3=int(input("Enter the marks of subject3: "))
avg_mark=int((sub1+sub2+sub3)/3)

if avg_mark>=90 and avg_mark<=100:
    print("Grade: A")
elif avg_mark>=80 and avg_mark<90:
    print("Grade: B")
elif avg_mark>=70 and avg_mark<79:
    print("Grade: C")
elif avg_mark>=60 and avg_mark<69:
    print("Grade: D")
else:
    print("Grade: F")