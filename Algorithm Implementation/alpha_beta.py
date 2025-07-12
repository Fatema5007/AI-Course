import math


count = 0


def alpha_beta(currentDepth, currentNode, isMax, score, totalDepth, alpha, beta):
    global count  
   
    if currentDepth == totalDepth:
        return score[currentNode]

    if isMax:
        best = -math.inf

        
        val = alpha_beta(currentDepth + 1, currentNode * 2, False, score, totalDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        
        if beta <= alpha:
            count += 1
            return best

       
        val = alpha_beta(currentDepth + 1, currentNode * 2 + 1, False, score, totalDepth, alpha, beta)
        best = max(best, val)
        alpha = max(alpha, best)

        return best

    else:
        best = math.inf

        
        val = alpha_beta(currentDepth + 1, currentNode * 2, True, score, totalDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        if beta <= alpha:
            count += 1
            return best

       
        val = alpha_beta(currentDepth + 1, currentNode * 2 + 1, True, score, totalDepth, alpha, beta)
        best = min(best, val)
        beta = min(beta, best)

        return best




score = []

x = int(input("Enter the number of leaf nodes : "))
for i in range(x):
    y = int(input("Enter the values of leaf node: "))
    score.append(y)


totalDepth = int(math.log2(len(score)))
startingDepth = 0
startingNode = 0
isMax = True

alpha = -math.inf
beta = math.inf

print("\nLeaf nodes:", score)

answer = alpha_beta(startingDepth, startingNode, isMax, score, totalDepth, alpha, beta)

print("\nThe best score is:", answer)
print("Number of prunings performed:",count)