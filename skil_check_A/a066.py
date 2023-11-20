def max_consecutive_work_days(N: int, work_periods: list) -> int:
    """
    最大連続勤務日数を計算します。

    Args:
        N (int): 勤務期間の数。
        work_periods (list): 勤務期間の開始時間と終了時間を表すタプルのリスト。

    Returns:
        int: 最大連続勤務日数。
    """

    work_periods.sort(key=lambda x: (x[0], -x[1]))
    max_days: int = 0
    current_start, current_end = work_periods[0]

    for i in range(1, N):
        next_start, next_end = work_periods[i]
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            max_days = max(max_days, current_end - current_start + 1)
            current_start, current_end = next_start, next_end

    max_days = max(max_days, current_end - current_start + 1)

    return max_days


N: int = int(input())
work_periods = [list(map(int, input().split())) for _ in range(N)]
print(max_consecutive_work_days(N, work_periods))
