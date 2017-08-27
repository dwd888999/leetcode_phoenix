# -*- coding:utf-8 -*-
__author = 'Phoenix'
'''
can place flower
'''

class Solution(object):
    def canPlaceFlowers(self,flowerbed,n):
        numberofzero=1
        result=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                numberofzero+=1
            else:
                result+=(numberofzero-1)/2
                numberofzero = 0
        if flowerbed[-1]==0:
            result+=(numberofzero)/2
        return result>=n

if __name__=='__main__':
    flowerbed=[1,0,0,0,1]
    n=1
    s=Solution()
    print s.canPlaceFlowers(flowerbed,n)