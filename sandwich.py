# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]
# count = 0
# while sandwiches:
#     for i in range(len(students)):
#         if len(students) != 0 or len(sandwiches) != 0:
#             if students[i] == sandwiches[i]:
#                 e = students.pop(0)
#                 # print("poped",e)
#                 l = sandwiches.pop(0)
#                 # print("poped sand",l)
#                 count += 1
#                 # print(count)
#                 s = count
#                 break
#             else:
#                 students.append(students[i])
#                 students.pop(0)
#                 break
#
# print(count)
students = [1, 1, 0,0]
sandwiches = [ 0, 1, 0, 1]
# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]
count = 0

while sandwiches:
    if sandwiches[0] in students:
        if len(students) != 0 and len(sandwiches) != 0:
            if students[0] == sandwiches[0]:
                e = students.pop(0)
                l = sandwiches.pop(0)
                count += 1
            else:
                students.append(students.pop(0))
    else:
         break

print(len(students))

