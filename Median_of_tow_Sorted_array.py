'''
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
def medium(a,b):
    s=0
    for i in (a+b):
        s+=i

    return (s/len(a+b))

print(medium([1,2],[3,4]))

def medium_2(li1,li2): 
    return (sum(li1+li2)/len(li1+li2))

print(medium_2([1,2],[3,4]))
