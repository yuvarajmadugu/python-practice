# # WAP to count the number of students with the “A” grade in the following tuple.
# grades = ("C", "D", "A", "A", "B", "B", "A")
# count_a = grades.count("A")
# print(f"Number of students with 'A' grade: {count_a}")
# #store the above value is order "A" to "D"
# grades.sort()
# print("Sorted grades:", grades)


# #You are given a list of subjects chosen by students. Each unique subject needs one classroom. Some subjects are repeated because multiple students chose them.
# #wap Using set in Python to find how many classrooms are needed.
# subjects = ["python", "java", "C++", "python", "js", "java", "python", "java", "C++", "C"]
# unique_subjects = set(subjects)
# classrooms_needed = len(unique_subjects)
# print("Unique subjects:", unique_subjects)
# print("Number of classrooms needed:", classrooms_needed)


# #wap for give 2 texts - Find common words, Find words unique to text1 & Count total unique words across both texts
# text1 = "Python is a great programming language"
# text2 = "Many developers love the Python language"
# words1 = set(text1.lower().split())
# words2 = set(text2.lower().split())
# common_words = words1.intersection(words2)
# unique_to_text1 = words1.difference(words2)
# all_unique_words = words1.union(words2)
# total_unique_count = len(all_unique_words)
# print("Words in both texts:", common_words)
# print("Words unique to text1:", unique_to_text1)
# print("Total unique words across both texts:", total_unique_count)


# #Given a list, print all elements that contain duplicates. [3, 5, 7, 3, 9, 5, 3, 9]
# list = [3, 5, 7, 3, 9, 5, 3, 9]
# unique_elements = set(list)
# print(unique_elements)
# #sort the set in assending order:
# order = sorted(unique_elements)
# print(order)
# # print all elements that appear twice, only twice.
# twice = set()
# for num in list:
#     if list.count(num) == 2 and num not in twice:
#         print(f"Element {num} appears twice.")
#         twice.add(num)


# # Given a list of integers and a target sum, find all unique pairs that add up to the target. Avoid duplicates-(2,5)&(5,2) are same.
# nums = [2, 5, 3, 4, 1, 6, 7, 2]
# target = 7
# # Set to store unique pairs
# seen = set()
# pairs = set()
# for num in nums:
#     complement = target - num
#     if complement in seen:
#         # Use tuple with sorted values to avoid (a,b) and (b,a) being treated differently
#         pair = tuple(sorted((num, complement)))
#         pairs.add(pair)
#     seen.add(num)
# print("Unique pairs that sum to", target, "are:", pairs)


# # From a list, remove all duplicates except for the first occurrence of each element. Don't use Sets
# nums = [5, 1, 2, 1, 5, 2]
# result = []
# for n in nums:
#     if n not in result:
#         result.append(n)
# print("List after removing duplicates:", result)



 




