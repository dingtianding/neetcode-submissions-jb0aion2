class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #set up result
        n = len(nums)
        res = [1] * n

        
        #set up a var for running products
        #set the cur as the product
        #multiply the running product with cur num
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #go back ward same as with a running product
        #multiply the number with the running prodcut
        #multipy the running product with cur num
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        #return the res
        