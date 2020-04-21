def find_median(seq, rank):

    pivot = median_medians(seq, 5)
    left = [i for i in seq if i < pivot]
    right = [i for i in seq if i > pivot]

    k = len(left)+1

    if k == rank:
        return pivot
    elif k < rank:
        return find_median(right, rank-k+1)
    else:
        return find_median(left, rank)



def partitions(seq, k):
    """
    :param seq: list of ints
    :return: sublists of length 5 indices start and ends
    """
    partition = []
    start = 0
    end = 0
    while end < len(seq)-1:
        while (end - start + 1) != k:
            end += 1
        partition.append([start, end])
        start = end+1

    return partition

def median_medians(seq, k):
    if len(seq) == 1:
        return seq[0]

    else:
        n = len(seq)//5
        if n == 0 or n == 1:
            return sorted(seq)[len(seq)//2]

        else:
            medians = []
            partition = partitions(seq, k)
            for i, j in partition:
                # print(seq[i:j+1], "OH FUCK")
                medians.append(median_medians(seq[i:j+1], k))
            return sorted(medians)[len(medians)//2]




# print(median_medians([10,9,6,7,13,2,3,4,5,8,1,0,14,12,11]), "I THINK THIS IS WRONG BRUV")
# print(median_medians([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))

print(find_median([10,9,6,7,13,2,3,4,5,8,1,0,14,12,11], 7))
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# print(find_median([0,1,2,3,4,5,6,7,8,9], 0))




