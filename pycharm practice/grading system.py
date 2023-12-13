# grading system
marks = int(input("enter the marks of student"))
if 90 <= marks < 100:
    print("outstanding you got 'A' ")
elif 80 <= marks <90:
    print('execellent! you got B in exam')
elif 70 <= marks < 80:
    print('good your reaching toward your goal , you got c ')
elif 60 >= marks > 70:
    print('you are improving and congralutin for getting D')
elif marks < 60:
    print('just do hard work believe in yourself, you got E grade')
else:
    print("invalid input")
