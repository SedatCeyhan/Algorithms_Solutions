from collections import defaultdict
from collections import Counter
import itertools

def mostVisitedPattern(username, timestamp, website):
    tuples = []
    userTuNumDict, webDict = {}, defaultdict(lambda: 0)
    for i in range(len(username)):
        if username[i] in userTuNumDict:
            userTuNumDict[username[i]] += 1
        else: userTuNumDict[username[i]] = 1
        tuples.append([username[i], timestamp[i], website[i]])

    tuples = sorted(sorted(tuples, key=lambda item: item[1]), key=lambda item:item[0])
    userTuNumDict = sorted(userTuNumDict.items(), key=lambda item:item[0])

    curr = 0
    for user in userTuNumDict:
        temp = set()
        for i in range(curr, curr + user[1] - 2):
            for j in range(i + 1, curr + user[1] - 1):
                for k in range(j + 1, curr + user[1]):
                    threeSeq = tuples[i][-1] + "," + tuples[j][-1] + "," + tuples[k][-1]
                    temp.add(threeSeq)
        for item in temp:  webDict[item] += 1
        curr += user[1]

    webDict = sorted(sorted(webDict.items()), key=lambda item:item[1], reverse=True)
    return webDict[0][0].split(",")









#print(mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"],[1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"]))
# names = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
#
# times = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
#
# webs = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]

#print(mostVisitedPattern(names, times, webs))

names = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]

times = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]

webs = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]

print(mostVisitedPattern(names, times, webs))


#
# def mostVisitedPattern(username, timestamp, website):
#     dp = defaultdict(list)
#     for t, u, w in sorted(zip(timestamp, username, website)):
#         dp[u].append(w)
#     print(str(dp) + '\n\n')
#     count = sum([Counter(set(itertools.combinations(dp[u], 3))) for u in dp], Counter())
#     print(count)
#     return list(min(count, key=lambda k: (-count[k], k)))
#
#
#
# print('\n\n')
