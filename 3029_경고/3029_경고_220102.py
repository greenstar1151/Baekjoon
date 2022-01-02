# from datetime import datetime

# current_time = datetime.strptime(input(), '%H:%M:%S')
# target_time = datetime.strptime(input(), '%H:%M:%S')
# time_diff_raw = target_time - current_time
# time_diff = datetime(1900, 1, 1, 0) + time_diff_raw

# if time_diff.strftime('%H:%M:%S') == '00:00:00':
#     print('24:00:00')
# else:
#     print(time_diff.strftime('%H:%M:%S'))

# %%
def time_to_seconds(time_data):
    return sum(map(lambda x: x[0] * x[1], zip(time_data, [3600, 60, 1])))

def seconds_to_timestr(seconds):
    return '{:02d}:{:02d}:{:02d}'.format(seconds // 3600, (seconds % 3600) // 60, seconds % 60)

current_time = time_to_seconds(map(int, input().split(':')))
target_time = time_to_seconds(map(int, input().split(':')))

time_diff_raw = target_time - current_time
if time_diff_raw <= 0:
    time_diff_raw += 24 * 3600

print(seconds_to_timestr(time_diff_raw))
