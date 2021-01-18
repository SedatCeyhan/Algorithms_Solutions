def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    if len(scheduleStart) == 0 or len(scheduleEnd) == 0: return 0

    sorted_end_times = list(sorted(scheduleEnd))
    sorted_start_times = list(sorted(scheduleStart))


    counter = 1
    min_end = sorted_end_times[0]
    while min_end <= sorted_start_times[-1]:
        counter += 1
        curr_start = min_end
        while curr_start not in scheduleStart:
            curr_start += 1
        idx_curr_start = scheduleStart.index(curr_start)
        min_end = list(sorted(scheduleEnd[idx_curr_start:]))[0]


    return counter

print(maxPresentations([1,2,3,3,3], [2,2,3,4,4]))
