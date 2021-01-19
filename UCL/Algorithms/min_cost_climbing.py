#On a staircase, the i-th step has some non-negative cost cost[i] 
#assigned to it. The staircase starts at index i=0. Once you pay the 
# cost, you can either climb one or two steps. Design and implement 
# an algorithm to find the minimum cost to reach the top floor. 
# You can start your climb from either step index 0, or step index 1.
# For example, given a staircase of 9 floors (from 0 to 8) and input cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], the min-cost climb starting from 0 is 6.

def minCostClimbingStairs(cost):
    p1 , p2 = 0, 0
    for i in range(2, len(cost) + 1):
        p1, p2 = p2, min(p2 + cost[i-1], p1 + cost[i-2])
    print(p2)
    
minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

#or

def minCostClimbingStairs(cost):
    dp_0 = cost[0]
    dp_1 = cost[1]
    for i in range(2, len(cost)):
        dp_i = min(dp_0+cost[i], dp_1+cost[i])
        dp_0 = dp_1
        dp_1 = dp_i
    return min(dp_0, dp_1)

print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))