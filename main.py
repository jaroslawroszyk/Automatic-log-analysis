from datetime import datetime
from Raport import Raport, Temperatura
from time_utils import time_duration
from valid_log_line import is_invalid_log

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
    tuple_logs_sorted = sorted(tuple_logs, key=lambda x : x[0])

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
        
        last_log = tuple_logs_sorted[j][0] if j < n else tuple_logs_sorted[j-1][0]
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
    procent_wadliwych_logow = 100.0
    if incorrect_log_count > 0:
        procent_wadliwych_logow = 100 * incorrect_log_count / \
            (correct_log_count + incorrect_log_count)

    return procent_wadliwych_logow

def generuj_raport(file_path):
    raport = Raport()

    correct_logs, incorrent_logs = filter_logs(file_path)
    raport.wadliwe_logi = incorrent_logs

    incorrect_log_count = len(raport.wadliwe_logi)
    correct_log_count = len(correct_logs)

    raport.procent_wadliwych_logow = count_incorrect_logs(
        incorrect_log_count, correct_log_count)
    raport.czas_trwania_raportu = time_duration(correct_logs)

    if correct_log_count > 0:
        raport.temperatura = sprawdz_temperature(correct_logs)
        periods = overheating_periods(correct_logs)
        raport.najdluzszy_czas_przegrzania = max(periods + [0])
        raport.liczba_okresow_przegrzania = len(periods)

    if raport.procent_wadliwych_logow > 10.0 and incorrect_log_count > 0:
        raport.problemy.wysoki_poziom_zaklocen_EM = True

    if raport.najdluzszy_czas_przegrzania > 10.0:
        raport.problemy.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = True
    print(raport)   

    return raport.to_dict()


generuj_raport("test/inputs/test_third_from_spec.txt")
