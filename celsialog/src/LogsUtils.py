from datetime import datetime
import re

from src.Raport import Temperatura


def is_invalid_log(linia):
    match = re.match(
        r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+([0-9]+\.?[0-9]*C)$', linia.strip())
    if match:
        trash_tuple, temp_str = match.groups()
        try:
            date = datetime.strptime(trash_tuple, '%Y-%m-%d %H:%M')
        except ValueError:
            return True  # Data jest niepoprawna
        temp = float(temp_str[:-1])
        if temp <= 0:
            return True
        else:
            return False
    else:
        return True


def timestamp_from_log(log):
    date = log.rsplit(' ', 1)[0]
    return datetime.strptime(date.strip(), '%Y-%m-%d %H:%M').timestamp()


def time_duration(logi):
    if len(logi) < 2:
        return 0
    timestamps = map(timestamp_from_log, logi)
    sorted_timestamps = sorted(timestamps)
    return int((sorted_timestamps[-1] - sorted_timestamps[0]) / 60)


def convert_log(log):
    parts = log.rsplit(' ', 1)
    temp = parts[1]
    return float(temp[:-1])


def sprawdz_temperature(lista_logow):
    var_temp = list(map(convert_log, lista_logow))
    return Temperatura(
        min=min(var_temp),
        max=max(var_temp),
        srednia=sum(var_temp) / len(var_temp))


def convert_log_for_overheating(log):
    parts = log.rsplit(' ', 1)
    date, temp = parts[0], parts[1]
    timestamp = datetime.strptime(date.strip(), '%Y-%m-%d %H:%M').timestamp()
    temp = float(temp[:-1])
    return timestamp / 60, temp > 100


def overheating_periods(logs):
    tuple_logs = map(convert_log_for_overheating, logs)
    tuple_logs_sorted = sorted(tuple_logs, key=lambda x: x[0])

    n = len(tuple_logs_sorted)
    i, j = 0, 0
    periods = []

    while i < n:
        if not tuple_logs_sorted[i][1]:
            i += 1
            j += 1
            continue

        while j < n and tuple_logs_sorted[j][1]:
            j += 1

        last_log = tuple_logs_sorted[j][0] if j < n else tuple_logs_sorted[j - 1][0]
        periods.append((last_log - tuple_logs_sorted[i][0]))
        i = j

    return periods


def filter_logs(file_path):
    correct_logs = []
    incorrent_logs = []
    with open(file_path, 'r') as file:
        for line in file:
            if not is_invalid_log(line):
                correct_logs.append(line.strip())
            else:
                incorrent_logs.append(line.strip())
    return correct_logs, incorrent_logs


def count_incorrect_logs(incorrect_log_count, correct_log_count):
    suma = (correct_log_count + incorrect_log_count)
    if suma == 0:
        return 100.0
    return 100.0 * incorrect_log_count / suma