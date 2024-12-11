# Two Sum : LeetCode
# Method 1
def twoSum(self,nums:list[int],target:int):
   for i in range(len(nums)):
       for j in range(i+1,len(nums)):
          if i+j==target:
              return[i,j]

# Method 2 : O(n) Time Complexity : Dictionary

# nums=[2,7,11,15],target=9,Output=[0,1]
# value = index, key = what we are looking for o(n)

nums=[1,2,3,4]
target=7
d={} # Dictionary searching is o(1)
for index in range(len(nums)):
    if target-nums[index] in d:
        print(d[target-nums[index]],index)
    else:
        d[nums[index]]=index

# Method 3 :
# solution using set (Assumption return True if there's a solution,and False otherwise)
nums = [1, 2, 3, 4]
target = 7
s = set()  # Set searching is O(1)

for num in nums:
    if target - num in s:
        print(True)
        break  # Exit the loop once a solution is found
    else:
        s.add(num)
else:
    # This will execute only if the loop completes without finding a solution
    print(False)
