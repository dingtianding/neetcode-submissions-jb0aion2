"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Min number of room = max number of overlaps one a single point time
#0123456789
#1----  ----
#2  -----
#3   --
#cur = 1
#max = 1  
# return max
#[(0,40),(5,10),(15,20)]
# start = 0,5,15 -> 3
# end = 10,20,null
# if we hit a start, +1 active room
# if we hit end time, -1 active room.
# from min 20 to min 40:
# start1 = 15
# end1 = 20
# cur = 0
# max = 2  
# return max
# osrt s
# Time = Log * N(length-starttime) * N(length of starttime)
# N = 3 M = 40
# space 1
# need 3 room to make it happen
# var all time max 
# var current room active
# Optimizations:
# 1 if no there no more start time, we can't have a higher max: we can end early -> while loop on the start time 
# 2. 1-4 -> if statement 
# end > start = upcoming event is start -> open a room
# end < start = upcoming event is end -> close a room
# [(0,40),(5,10),(15,20)]

# 0,5,15
# 5,20,40
# if start = end 
# we close first. This a real case where we need a extra
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort() #small to big
        end.sort()

        cur, res = 0, 0
        p1, p2 = 0, 0

        while p1 < len(start): # start = end = 15
            if start[p1] < end[p2]: #upcoming is start
                cur += 1
                p1 += 1
            else: #upcoming event is end
                cur -=1
                p2 += 1
            res = max(res, cur)

        return res
# hash like object
# Computer is store data in data strcuture
# then client/ server, processing to make stuff happen.
# LoL Client, create a char on your
# map = {}
# game = { y, x, z, name: garen, class:warrior, nationa Demacia, atk: 100, items:{slot1: Warmog{HP:1000, Effect:{time out of 5, extrra health eneed 2000, % hp turn atk; 2 }},slot2} 
# }
# AWS log = {server; NEasw, SSD. Cluster:{c;lister}}
#
# sorting problem hash can't solve
#
# think hash like table of content:
#
# Garen[Class] = Warrior
# hash[key] = value
# database/book
# chapter 1(key) - page 1,
# chapter 1.1
# chapter 2 - page 10
# chapter 3 - page 100
# page 45 >50 
# 51-100
# 25 < 45
# drop 24
# N. 10
# 3.000000000001 != 2.999999999992
# round it to close integer
# int()
# function int(input):(in C) C -> 0010101011
#   if input is string: 
#           it deso 
# Englishy/Brute/Human: 
# Code int()
# Language Pyt
# Log N = Sorting(Different )
# N^2 10* 10

# implement
# function sort(array):
#  iteraete:
# compare num1 vs num2 :
# 
# 








