from collections import Counter
import heapq
def frequency(arr,k):
    # countDict = {}
    # for i in range(len(arr)):
    #     if arr[i] in countDict.keys():                
    #         countDict[arr[i]] +=1
    #     else:
    #         countDict[arr[i]] = 1
    # print(countDict)
    # heap = []
    # for key, val in countDict.items():
    #     heapq.heappush((heap), (val, key))        
    #     if len(heap) >k:
    #         heapq.heappop(heap)
    # res = [x[1] for x in heap]        
    # return res
        
    # hashmap = {}
    # for element in arr:
    #     if element not in hashmap:
    #         hashmap[element] = 1
    #     else:
    #         hashmap[element] += 1
    # for key, value in hashmap.items():
    #     if value == k:
    #         return key
    
    # count_map = {}
    # n = len(arr)
    # ans = []
    # for i in range(n):
    #     if(arr[i] in count_map.keys()):
    #         count_map[arr[i]] += 1
    #     else:
    #         count_map[arr[i]] = 1
    # for i in range(n):
    #     if (count_map[arr[i]] == k):
    #         return ans.append(arr[i])
    # return ans if ans else -1  

    ans = []
    counter_value = Counter(arr)
    # print(counter_value)
    for num in counter_value:
        if (counter_value[num] == k):
            ans.append(num)
    return ans if ans else 0 
    
print(frequency([8, 7, 9,1, 6, 7, 5, 1],2))
print(frequency([1, 2, 3],3))
print(frequency([1, 2, 2, 1, 4, 5],2))
print(frequency([],2))
# Time Complexity: O(n)
# Space Complexity: O(n)