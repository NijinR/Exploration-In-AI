name=input("Enter Student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range (1,n+1):
    mark=float(input(f"Enter mark for subject{i}:"))
    total+=mark
percentage=total/n
if percentage>=90:
     grade="A+"
     performance+"Outstanding"
elif percentage>=80:                     
     grade="A"
     perfomance="Excellent"
elif percentage>=70:           
     grade="B"
     perfomance="Very Good"
elif percentage>=60:
     grade="C"
     perfomance="Good"
elif percentage>=50:
     grade="D"
     perfomance="Average"
else:
    grade="F"
    perfomance="Need Improvement"
print("\n---Academic Perfomance---")
print("Student Name:",name)
print("Total Marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("Perfomance:",perfomance)
