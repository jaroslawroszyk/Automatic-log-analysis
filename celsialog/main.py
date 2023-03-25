from src.Raport import Temperatura, Raport, Problemy
import src.LogsUtils as utils


def generuj_raport(file_path):
    raport = Raport(problemy=Problemy())

    correct_logs, incorrent_logs = utils.filter_logs(file_path)
    raport.wadliwe_logi = incorrent_logs

    incorrect_log_count = len(raport.wadliwe_logi)
    correct_log_count = len(correct_logs)

    raport.procent_wadliwych_logow = utils.count_incorrect_logs(
        incorrect_log_count, correct_log_count)
    raport.czas_trwania_raportu = utils.time_duration(correct_logs)

    if correct_log_count > 0:
        raport.temperatura = utils.sprawdz_temperature(correct_logs)
        periods = utils.overheating_periods(correct_logs)
        raport.najdluzszy_czas_przegrzania = max(periods + [0])
        raport.liczba_okresow_przegrzania = len(periods)

    if raport.procent_wadliwych_logow > 10.0:
        raport.problemy.wysoki_poziom_zaklocen_EM = True

    if raport.najdluzszy_czas_przegrzania > 10.0:
        raport.problemy.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = True
    print(raport)

    return raport.to_dict()


if __name__ == '__main__':
    generuj_raport("tests/inputs/test_first_from_spec.txt")
