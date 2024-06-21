# lt=[]
# a=[]
# n=int(input())
# for i in range(n):
#     lt.append(input())
#     a=lt[i].split(' ')
#     lt[i]=a
# # print(lt)
# print(int(lt[0][0])+1)    
# for i in range(n):
#     for j in range(i+1,n):
#         if(lt[i][0]<=lt[j][0]<=lt[i][1] or lt[j][0]<=lt[i][0]<=lt[j][0]):
#             a.append()
def max_footfall(n, groups):
    max_time = max(groups, key=lambda x: x[1])[1] + 1
    footfall = [0] * max_time

    for group in groups:
        in_time, out_time, n_people = group
        footfall[in_time] += n_people
        footfall[out_time] -= n_people

    max_footfall = 0
    current_footfall = 0

    for people_change in footfall:
        current_footfall += people_change
        max_footfall = max(max_footfall, current_footfall)

    return max_footfall

# Input
n = int(input())
groups = [tuple(map(int, input().split())) for _ in range(n)]
print(groups)

# Output
result = max_footfall(n, groups)
print(result)




