from datetime import datetime
from calculate_percentage_of_invalid_logs import calculate_error_logs_percentage, calculate_percentage_of_invalid_logs
from time_utils import calculate_time_difference, check_correct_time, czas_trwania

from valid_log_line import is_invalid_log


def delete_white_characters(logs):
    for i in range(len(logs)):
        logs[i] = logs[i].strip()

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
        data_godzina = datetime.strptime(data + ' ' + godzina, '%Y-%d-%m %H:%M')
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
    wadliwe_logi = []
    procent_wadliwych_logow = '100.0'
    czas_trwania_raportu = 0
    temperatura_max_str = None
    temperatura_min_str = None
    temperatura_avg_str = None
    procent_wadliwych_logow_float = 0.0
    najdluzszy_czas_przegrzania = 0
    liczba_okresow_przegrzania = 0
    problemy = {
        'wysoki_poziom_zaklocen_EM': False,
        'wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury': False
    }

    with open(file_path, 'r') as file:
        number_of_logs = 0
        incorrect_logs = 0
        correct_logs = []
        for line in file:
            number_of_logs += 1
            if not is_invalid_log(line):
                correct_logs.append(line)
            else:
                wadliwe_logi.append(line)
                incorrect_logs += 1

        # procent_wadliwych_logow = calculate_error_logs_percentage(
        #     incorrect_logs, number_of_logs, correct_logs)
        # procent_wadliwych_logow_float = float(procent_wadliwych_logow)
 
        if incorrect_logs > 0:
            procent_wadliwych_logow_float = (incorrect_logs / number_of_logs) * 100
            procent_wadliwych_logow_float = round(procent_wadliwych_logow_float, 1)
            procent_wadliwych_logow = str(procent_wadliwych_logow_float)
        if incorrect_logs == 0 and len(correct_logs) > 0:
            procent_wadliwych_logow = "0.0"
        delete_white_characters(wadliwe_logi)
        delete_white_characters(correct_logs)

    czas_trwania_raportu = czas_trwania(correct_logs)
    
    if len(correct_logs) > 0:
        temperatury = sprawdz_temperatury(correct_logs)
        temperatura_min = temperatury['min_temp']
        temperatura_max = temperatury['max_temp']
        temperatura_avg = temperatury['avg_temp']
        temperatura_min_str = str(temperatura_min)
        temperatura_max_str = str(temperatura_max)
        temperatura_avg_str = str(temperatura_avg)
        najdluzszy_czas_przegrzania = time_overheating(correct_logs)
        liczba_okresow_przegrzania = overheating_periods(correct_logs)


    if procent_wadliwych_logow_float > 10:
        problemy['wysoki_poziom_zaklocen_EM'] = True

    if najdluzszy_czas_przegrzania > 10:
        problemy['wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury'] = True
    print("jarek problemy", problemy)
    raport = {
        "wadliwe_logi": wadliwe_logi,
        "procent_wadliwych_logow": procent_wadliwych_logow,
        "czas_trwania_raportu": czas_trwania_raportu,
        "temperatura": {
            "max": temperatura_max_str,
            "min": temperatura_min_str,
            "srednia": temperatura_avg_str
        },
        "najdluzszy_czas_przegrzania": najdluzszy_czas_przegrzania,
        "liczba_okresow_przegrzania": liczba_okresow_przegrzania,
        "problemy": {
            "wysoki_poziom_zaklocen_EM": problemy['wysoki_poziom_zaklocen_EM'],
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": problemy[
                'wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury']
        }
    }
    return raport


print(generate_raport("test_input_single.txt"))