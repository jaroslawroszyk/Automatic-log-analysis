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

def check_correct_time(logi):
    if len(logi) > 1:
        last_time_str = logi[0].split()[0] + ' ' + logi[0].split()[1]
        valid_logs = []
        for log in logi:
            log_time_str = log.split()[0] + ' ' + log.split()[1]
            last_time = datetime.strptime(last_time_str, '%Y-%m-%d %H:%M')
            log_time = datetime.strptime(log_time_str, '%Y-%m-%d %H:%M')
            if last_time_str is None or log_time >= last_time:
                valid_logs.append(log)
                last_time_str = log_time_str
            else:
                continue
        if len(valid_logs) > 1:
            return valid_logs
        else:
            return []

    else:
        return logi


def czas_trwania(logi):
    valid_logs = check_correct_time(logi)
    if valid_logs is not None:
        start_time_str = ''
        end_time_str = ''
        for log in valid_logs:
            log = log.split()[:2]
            if not start_time_str:
                start_time_str = ' '.join(log)
            end_time_str = ' '.join(log)
        return calculate_time_difference(start_time_str, end_time_str)
    else:
        return 0
