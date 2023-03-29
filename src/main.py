from datetime import datetime
from logs.valid_log_line import is_invalid_log
from utils.calculate_percentage_of_invalid_logs import calculate_percentage_of_invalid_logs
# from utils.time_difference_utils import calculate_time_difference
# from exceptnions.time_exception import InvalidTime


def delete_white_characters(logs):
    for i in range(len(logs)):
        logs[i] = logs[i].strip()


def generate_raport(file_path):
    wadliwe_logi = []
    procent_wadliwych_logow = '100.0'
    czas_trwania_raportu = 0
    temperatura = {
        'min': '0',
        'max': '0',
        'srednia': '0'
    }
    # temperatura_max_str = None
    # temperatura_min_str = None
    # temperatura_avg_str = None
    najdluzszy_czas_przegrzania = 0
    liczba_okresow_przegrzania = 0
    problemy = {
        'wysoki_poziom_zaklocen_EM': False,
        'wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury': False
    }

    with open(file_path, 'r') as file:
        number_of_logs = 0
        incorrect_logs = 0
        tmp_incorrect = []
        correct_logs = []
        for line in file:
            number_of_logs += 1
            if not is_invalid_log(line):
                correct_logs.append(line)
            else:
                wadliwe_logi.append(line)
                tmp_incorrect.append(line)
                incorrect_logs += 1
        # print("incorrect_logs", incorrect_logs)
        # print("number_of_logs", number_of_logs)
        procent_wadliwych_logow = calculate_percentage_of_invalid_logs(
            incorrect_logs, number_of_logs)
        delete_white_characters(wadliwe_logi)
        delete_white_characters(correct_logs)
        # print("wadliwe_logi[i]",  wadliwe_logi)
        # print("procent_wadliwych_logow", procent_wadliwych_logow)

        # print("Correct_logs", correct_logs)
        # print("incorrect_logs", tmp_incorrect)

    raport = {
        "wadliwe_logi": wadliwe_logi,
        "correct_logs": correct_logs,
        "procent_wadliwych_logow": procent_wadliwych_logow
    }
    return raport


print(generate_raport('test_input_single.txt'))

# test correcrt behavour
# try:

#     start = "2023-03-29 00:00"
#     end = "2023-03-28 00:00"

#     print(calculate_time_difference(start,end))
# except InvalidTime:
#     print(InvalidTime)
