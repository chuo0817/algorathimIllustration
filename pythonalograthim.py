#coding=utf-8
# 算法图解第一章  二分查找（有序）
# def binary_search(list,item):
#     low = 0;
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high)/2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid -1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1,3,5,7,9]
# print binary_search(my_list,3)
# print binary_search(my_list,-1)
# 第三章 递归
# def countdown(i):
#     print i
#     if i <= 0:
#         return
#     else:
#         countdown(i-1)
# countdown(6)
# 阶乘
def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
print fact(3)
