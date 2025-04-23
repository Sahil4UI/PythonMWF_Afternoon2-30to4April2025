# Nested Loop
'''
*****
*****
*****
*****
*****
'''
# for row in range(1,6):
#     for col in range(1,6):
#         print("*",end="")
#     print()
    
# *
# **
# ***
# ****
# *****

for row in range(1,6):
    for col in range(row):
        print("*",end="")
    print()
        
# 1
# 12
# 123
# 1234
# 12345
# for row in range(1,6):
#     for col in range(0,row):
#         print(col+1,end="")
#     print()

# 1
# 22
# 333
# 4444
# 55555
for row in range(1,6):
    for col in range(row):
        print(row,end="")
    print()

# 1
# 01
# 010
# 1010
# 10101
# x = 1
# for row in range(1,6):
#     for col in range(row):
#         if x%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#         x+=1
#     print()
#     *
#    **
#   ***
#  ****
# *****

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# *   *
# *   *
# *****
# *   *
# *   *

