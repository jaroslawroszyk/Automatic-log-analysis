from datetime import datetime


def calculate_time_difference(start_time_str, end_time_str):
    if start_time_str < end_time_str:
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        time_delta = end_time - start_time
        total_minutes = time_delta.total_seconds() / 60
        return int(total_minutes)
    else:
        return 0


def timestamp_from_log(log):
    date = log.rsplit(' ', 1)[0]
    return datetime.strptime(date.strip(), '%Y-%m-%d %H:%M').timestamp()


def time_duration(logi):
    if len(logi) < 2:
        return 0
    timestamps = map(timestamp_from_log, logi)
    sorted_timestamps = sorted(timestamps)
    return int((sorted_timestamps[-1] - sorted_timestamps[0]) / 60)
