
arrive=['8','3','4']
depart=['12','7','10']
my_dict = {k: v for k, v in zip(arrive, depart)}
print(my_dict)
res=sorted(my_dict.items(),key=lambda x:x[0])
print(res)
size=len(res)
count=1
for i in range(len(res)-1):
    current=res[i][1]
    next=res[i+1][0]
    if current<next:
        count+=1
print(count)

# Function to process each test case
# def process_test_case(arrive, depart):
#     my_dict = {k: v for k, v in zip(arrive, depart)}
#     print(my_dict)
#
#     res = sorted(my_dict.items(), key=lambda x: x[0])
#     print(res)
#
#     count = 1  # Initialize count for each test case
#     for i in range(len(res) - 1):
#         current = res[i][1]
#         next_arrive = res[i + 1][0]
#         if current < next_arrive:
#             count += 1
#
#     print("Number of occurrences where departure time is before the next arrival time:", count)
#
#
# # Get number of test cases from user
# num_test_cases = int(input("Enter the number of test cases: "))
#
# # Process each test case
# for idx in range(1, num_test_cases + 1):
#     print(f"Test Case {idx}:")
#     # Get arrival times from user
#     arrive = input("Enter arrival times separated by space: ").split()
#     # Get departure times from user
#     depart = input("Enter departure times separated by space: ").split()
#     process_test_case(arrive, depart)

