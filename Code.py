Coding:

n=int(input())
my_list = list(map(int,input().split()))
my_set = set(my_list)
my_new_list = list(my_set)
v=len(my_new_list)
my_new_list.sort()
for i in range(0,v-1):
    print(my_new_list[i],end=" ")
print(my_new_list[v-1])
