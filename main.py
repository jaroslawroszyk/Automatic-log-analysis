from datetime import datetime
from Raport import Raport, Temperatura
from time_utils import calculate_time_difference, time_duration

from valid_log_line import is_invalid_log

# def convert_log(log):
#     parts = log.rsplit(' ', 1)
#     date, temp = parts[0], parts[1]
#     timestamp = datetime.strptime(date.strip(), '%Y-%m-%d %H:%M').timestamp()
#     tempStamp = temp[:-1]
#     return timestamp, tempStamp

def convert_log(log):
    parts = log.rsplit(' ', 1)
    temp = parts[1]
    return float(temp[:-1])

def sprawdz_temperature(lista_logow):
    var_temp = list(map(convert_log, lista_logow))
    return Temperatura(
        min=min(var_temp),
        max=max(var_temp),
        srednia=round(sum(var_temp) / len(var_temp), 1))

def time_overheating(logs):
    okresy = {}

    czas_start = ''
    for log in logs:
        data, godzina, temperatura = log.split()
        data_godzina = datetime.strptime(
            data + ' ' + godzina, '%Y-%d-%m %H:%M')
        czas = data_godzina.strftime('%Y-%d-%m %H:%M')
        if float(temperatura[:-1]) > 100:
            if not czas_start:
                czas_start = czas
        else:
            if czas_start:
                czas_trwania = calculate_time_difference(czas_start, czas)
                okresy[f"okres{len(okresy) + 1}"] = czas_trwania
                czas_start = ''

        if czas_start:
            okresy[f"okres{len(okresy) + 1}"] = calculate_time_difference(czas_start, czas)
    result = max(okresy.values(), default=0)
    return result


def overheating_periods(logs):
    if len(logs) > 0:
        periods = 0
        current_period = False
        if logs is not None:
            for i in range(1, len(logs)):
                temp1 = float(logs[i - 1].split()[2][:-1])
                temp2 = float(logs[i].split()[2][:-1])

                if temp1 <= 100 and temp2 > 100:
                    current_period = True
                    periods += 1
                elif temp1 > 100 and temp2 <= 100:
                    current_period = False

            return periods
        else:
            return 0
    else:
        return 0


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


def generate_raport(file_path):
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

        raport.najdluzszy_czas_przegrzania = time_overheating(correct_logs)
        raport.liczba_okresow_przegrzania = overheating_periods(correct_logs)

    if raport.procent_wadliwych_logow > 10.0 and incorrect_log_count > 0:
        raport.problemy.wysoki_poziom_zaklocen_EM = True

    if raport.najdluzszy_czas_przegrzania > 10.0:
        raport.problemy.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = True

    return raport.to_dict()


generate_raport("test/inputs/test_second_from_spec.txt")
