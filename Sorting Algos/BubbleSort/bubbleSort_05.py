# sorting in custom objects

class Student:
  name = ""
  grade = ""

def bubbleSort(array):
  for i in range(0,len(array)):
    for j in range(0,len(array)-1):
      if(array[j].grade > array[j+1].grade):
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
  return array


st1 = Student()
st1.name = "Ali"
st1.grade = "F"

st2 = Student()
st2.name = "Hassan"
st2.grade = "B"

st3 = Student()
st3.name = "Fatima"
st3.grade = "A"

st4 = Student()
st4.name = "Zain"
st4.grade = "C"


array = [st1,st2,st3,st4]
bubbleSort(array)
for student in array:
  print(f"Name: {student.name}, Grade: {student.grade}")