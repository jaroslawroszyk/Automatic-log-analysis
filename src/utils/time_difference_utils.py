from datetime import datetime

from src.exceptnions.time_exception import InvalidTime

# Todo:
# When you use that funciton you should use try : execepts block

def calculate_time_difference(start_time_str, end_time_str):
    if start_time_str <= end_time_str:
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        time_delta = end_time - start_time
        total_minutes = time_delta.total_seconds() / 60
        return int(total_minutes)
    else:
        raise InvalidTime
