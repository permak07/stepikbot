#===================Custom_filter=================================

# some_list=[7,14,28,32,32,'56','ghfkg']
# def custom_filter(some_list:list)->bool:
#     return sum(x for x in some_list if isinstance(x,int) and x%7==0 )<=83

# def custom_filter_v2(some_list: list) -> bool:
#     return sum(filter(lambda x: isinstance(x, int) and x % 7 == 0, some_list)) <= 83

# # другое решение
# def custom_filter(some_list):
#     return sum(filter(lambda x: type(x) == int and x % 7 == 0, some_list)) <= 83

# print(custom_filter(some_list))

#======================anonymous_filter===========================

# anonymous_filter = lambda x: isinstance(x,str) and x.lower().count('я')>=23
# print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
