def schedule_interview(classes):
    """
    :param classes: list of intervals length 2
    :return: int, total number of non conflicting classes
    """
    # greeedy solution
    # no weights
    classes.sort(key=lambda x:x[1])
    end = classes[0][1]
    ans = 1

    for i in range(1, len(classes)):
        if classes[i][0] >= end:
            end = classes[i][1]
            ans += 1
    return ans

    # O(nlogn)

# classes = [[1,9],[1,3],[1,2],[2,5],[2,4],[4,5], [4,8], [6,9]]
# print(schedule_interview(classes))

# you build the recurrence by finding the latest job that does not overlap with start of the current job
# find best dp[j]'s to build
# find the latest job because jobs that overlap (inc in class) tend to form a prefix of overlapping
# for a specific job, find the first thing outside of its overlapping constituents
# it will build the answer like this
#                              __________
#                         _________
#                      __________
#               _____________
#  _______________
# If I forget this visual, it builds by each iteration the best solution because we chose the latest time
# This means it builds incrementally if we didn't do this, we would be missing a lot
#
#
# if there is none, it's max(dp[i-1], weight[i])
# otherwise max(dp[i-1], weight[i] + j)
# binary search to find latest to make this O(nlogn)


def schedule_interview_weights(classes):
    """
    :param classes: list of intervals length 2
    :return: max value of classes that don't overlap
    """
    dp = [0]*len(classes)
    classes.sort(key=lambda x: x[1])
    dp[0] = classes[0][-1]

    for i in range(1, len(classes)):
        latest = -1
        for j in reversed(range(i-1)):
            if classes[j][1] <= classes[i][0]:
                latest = j
                break
        if latest != -1:
            dp[i] = max(dp[i-1], dp[latest] + classes[i][-1])
        else:
            dp[i] = max(dp[i-1], classes[i][-1])

    return dp[-1]


def bin_search(classes, start, start_):
    low = 0
    high = start-1
    while low < high:
        mid = (low+high)//2
        if classes[mid][1] <= start_:
            # find the latest one
            if classes[mid+1][1] <= start_:
                low = mid+1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def schedule_interview_binary(classes):
    """
    :param classes: list of courses
    :return: max value of classes
    """
    dp = [0]*len(classes)
    classes.sort(key=lambda x:x[1])
    dp[0] = classes[0][-1]

    for i in range(1, len(classes)):
        j = bin_search(classes, i, classes[i][0])
        include = classes[i][-1]
        if j != -1:
            include += dp[j]
        dp[i] = max(dp[i-1], include)
    return dp[-1]


course = [[1,3,2],[3,5,2],[4,6,1],[1,2,1],[2,4,1]]
print(schedule_interview_weights(course))
print(schedule_interview_binary(course))