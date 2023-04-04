from datetime import datetime
from Raport import Raport
from calculate_percentage_of_invalid_logs import calculate_error_logs_percentage, calculate_percentage_of_invalid_logs
from time_utils import calculate_time_difference, check_correct_time, czas_trwania

from valid_log_line import is_invalid_log


def sprawdz_temperatury(logi):
    if len(logi) > 1:
        temperatury = []
        for log in logi:
            log = log.split()
            temperatura = log[2].rstrip("C")
            temperatury.append(float(temperatura))

        min_temp = min(temperatury)
        max_temp = max(temperatury)
        avg_temp = round(sum(temperatury) / len(temperatury), 1)

        mapa_temperatur = dict()
        mapa_temperatur["min_temp"] = min_temp
        mapa_temperatur["max_temp"] = max_temp
        mapa_temperatur["avg_temp"] = avg_temp

        return mapa_temperatur
    elif len(logi) == 1:
        temperatury = []

        log = logi[0]
        log = log.split()
        temperatura = log[2].rstrip("C")
        temperatury.append(float(temperatura))

        min_temp = log[2]
        max_temp = log[2]
        avg_temp = log[2]

        mapa_temperatur = dict()
        mapa_temperatur["min_temp"] = min_temp
        mapa_temperatur["max_temp"] = max_temp
        mapa_temperatur["avg_temp"] = avg_temp

        return mapa_temperatur
    else:
        return None


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
        logs = check_correct_time(logs)

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

def generate_raport(file_path):
    raport = Raport()

    with open(file_path, 'r') as file:
        number_of_logs = 0
        incorrect_logs = 0
        correct_logs = []
        for line in file:
            number_of_logs += 1
            if not is_invalid_log(line):
                correct_logs.append(line)
            else:
                raport.wadliwe_logi.append(line.strip())
                incorrect_logs += 1

        # procent_wadliwych_logow = calculate_error_logs_percentage(
        #     incorrect_logs, number_of_logs, correct_logs)
        # procent_wadliwych_logow_float = float(procent_wadliwych_logow)

        if incorrect_logs > 0:
            raport.procent_wadliwych_logow = (
                incorrect_logs / number_of_logs) * 100

    raport.czas_trwania_raportu = czas_trwania(correct_logs)

    if len(correct_logs) > 0:
        temperatury = sprawdz_temperatury(correct_logs)
        print("JR! temperatury xD", temperatury)
        raport.temperatura.min = temperatury['min_temp']
        raport.temperatura.max = temperatury['max_temp']
        raport.temperatura.srednia = temperatury['avg_temp']

        raport.najdluzszy_czas_przegrzania = time_overheating(correct_logs)
        raport.liczba_okresow_przegrzania = overheating_periods(correct_logs)

# ADD to konsturkutro
    if raport.procent_wadliwych_logow > 10.0 and incorrect_logs > 0:
        raport.problemy.wysoki_poziom_zaklocen_EM = True

    if raport.najdluzszy_czas_przegrzania > 10.0:
        raport.problemy.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = True

    return raport


# print(generate_raport("test_input_single.txt"))
