def getPowerSet(curr_index,arr,ans):

    if curr_index==len(arr):
        print(sorted(ans,key=len))
        return

    new_ans = []
    for i in ans:
        new_ans.append(i)
        new_ans.append(i+[arr[curr_index]])
    getPowerSet(curr_index+1,arr,new_ans)

arr = [int(x) for x in input().split()]
getPowerSet(0,arr,[[]])