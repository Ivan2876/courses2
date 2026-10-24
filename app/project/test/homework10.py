numbers = [10, 20, 10, 30, 20, 40, 10, 50]
set_numbers = {10, 20, 10, 30, 20, 40, 10, 50}
print(numbers)
print(set_numbers)
print(len(set_numbers))
if 30 in set_numbers:
    print(30 in set_numbers)
if 100 in set_numbers:
    print(100 in set_numbers)
else:
    print(False in set_numbers)

data = [15, "Python", 15, True, "Python", 3.14, False, True]
set_data = {15, "Python", 15, True, "Python", 3.14, False, True}
print(data)
print(set_data)
set_data.add("Redis")
set_data.add(100)
set_data.remove("Python")
if True in set_data:
    print(True)
if False in set_data:
    print(True)
print(set_data)

python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"} | python_students
print(redis_students)
print(python_students.union(redis_students))
intersection1 = python_students & redis_students
intersection2 = python_students.intersection(redis_students)
print(intersection1)
print(intersection2)

all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}
difference1 = all_students - python_students
difference2 = all_students.difference(python_students)
print(difference1)
print(difference2)

numbers2 = {10, 20, 30}
numbers2.add(40)
numbers2.add(40)
numbers2.update([50, 60, 70])
numbers2.remove(20)
numbers2.discard(100)
remove_number = numbers2.pop()
print(remove_number)
print(numbers2)