from operator import itemgetter


def getUnallocatedUsers(bids, totalShares):
    # Sort by increasing time stamp first
    bids = sorted(bids, key=itemgetter(3))

    # Sort by decreasing bid share price
    bids = sorted(bids, key=itemgetter(2), reverse=True)

    print(bids)
    idx = 0
    while totalShares > 0 and idx < len(bids):
        totalShares -= bids[idx][1]
        idx += 1

    unallocated = bids[idx:]
    return sorted([bid[0] for bid in unallocated])




print(getUnallocatedUsers([[1,5,5,0], [2,7,8,1], [3,7,5,1], [4,10,3,3]], 1))