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
        
    hashmap = {}
    for element in arr:
        if element not in hashmap:
            hashmap[element] = 1
        else:
            hashmap[element] += 1
    for key, value in hashmap.items():
        if value == k:
            return key
    
    # count_map = {}
    # n = len(arr)
    # ans = []
    # for i in range(0, n):
    #     if(arr[i] in count_map.keys()):
    #         count_map[arr[i]] += 1
    #     else:
    #         count_map[arr[i]] = 1
    # for i in range(0, n):
    #     if (count_map[arr[i]] == k):
    #         return arr[i]
    # return -1


    # counter_value = Counter(arr)
    # for i in range(0,len(arr)):
    #     if (counter_value[arr[i]] == k):
    #         ans.append(i)
    #         return ans
        

    # return -1

print(frequency([8, 7, 9, 6, 7, 5, 1],2))


# Time Complexity: O(n)
# Space Complexity: O(n)