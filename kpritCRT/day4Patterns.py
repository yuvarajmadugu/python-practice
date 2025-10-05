# #simple sqaure pattern:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# #pattern 1:
# *
# * *
# * * *
# * * * *
# * * * * *
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("* ", end=" ")
#     print()



# #pattern 2:
# * * * * * 
# * * * *  
# * * *
# * *
# *
# n=5
# for i in range(n):
#     for j in range(i, n):
#         print("* ", end=" ")
#     print()



# #pattern 3:
# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# #pattern 3:
# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# n=5
# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# #pattern 4:
#           * 
#         * * 
#       * * *
#     * * * *
#   * * * * *
# n=5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# #pattern 5:
# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()


# #pattern 6:
#         * 
#       * * 
#     * * *
#   * * * *
# * * * * *
# n=5
# for i in range(1, n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# #pattern 7:
#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
# n=5
# for i in range(n+1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# #pattern 8:
# * * * * * * 
#   * * * * * * 
#     * * * * * *
#       * * * * * *
#         * * * * * *
# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     print()


# #pattern 9:
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * *
#         * * *
#           *
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     print()