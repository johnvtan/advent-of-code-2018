#!/usr/bin/env python3

with open('sorted-input') as f:
    content = f.readlines()

def get_minute(line):
    return int(line[15:17]) 

def get_id_num(after_timestamp):
    id_str = after_timestamp.split()[1]
    return int(id_str[1:]) 

def update_record(record, id_num, sleep_times, wake_times):
    assert len(sleep_times) == len(wake_times)
    if id_num not in record:
        record[id_num] = [0 for i in range(60)]
    for start, end in zip(sleep_times, wake_times):
        assert start < 60
        assert end < 60
        for i in range(start, end):
            record[id_num][i] += 1

record = {}
curr_guard_id = -1
sleep_times = []
wake_times = []
for line in content: 
    after_timestamp = line[19:]
    if after_timestamp.startswith('Guard'):
        if curr_guard_id > 0 and len(sleep_times) > 0:
            update_record(record, curr_guard_id, sleep_times, wake_times)
        curr_guard_id = get_id_num(after_timestamp)
        sleep_times = []
        wake_times = []
    elif after_timestamp.startswith('falls'):
        sleep_times.append(get_minute(line))
    elif after_timestamp.startswith('wakes'):
        wake_times.append(get_minute(line))
    else:
        print('Different line found: %s' % after_timestamp)

guard_id, sleep_record = max(record.items(), key=lambda x: sum(x[1]))
print(guard_id * sleep_record.index(max(sleep_record)))

# part 2
most_minutes = 0
guard_with_most_minutes = -1
for guard_id in record:
    if max(record[guard_id]) > most_minutes:
        most_minutes = max(record[guard_id])
        guard_with_most_minutes = guard_id

print(guard_with_most_minutes * record[guard_with_most_minutes].index(most_minutes))
