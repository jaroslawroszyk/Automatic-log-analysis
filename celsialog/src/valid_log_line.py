import re


def is_invalid_log(line):
    match = re.match(
        r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+([0-9]+\.?[0-9]*C)$', line.strip())
    if match:
        trash_tuple, temp_str = match.groups()
        temp = float(temp_str[:-1])
        if temp <= 0:
            return True
        else:
            return False
    else:
        return True
