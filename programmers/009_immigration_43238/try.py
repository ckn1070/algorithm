# NOT Solved
def solution(n, times):
    sorted(times)

    time = [0] * len(times)
    for i in range(n):
        for idx, val in enumerate(times):
            if idx + 1 < len(time) and time[idx] + val <= time[idx+1] + val:
                time[idx] += val
                break
            elif idx + 1 < len(time) and time[idx] + val > time[idx+1] + val:
                print(time[idx-1] + times[idx-1] , time[idx] + val)
                if time[idx-1] + times[idx-1] > time[idx] + val:
                    time[idx] += val
                else:
                    time[idx+1] += times[idx+1]
                break
        print(time)


    answer = sorted(time)[-1]
    print(answer)
    return answer

solution(6, [7, 10])
