import unittest
from Raport import Problemy, Raport, Temperatura

from main import generuj_raport


class EmptyTest(unittest.TestCase):
    def test_empty_file(self):
        file_path = "test/inputs/empty_file.txt"
        expected_output = Raport()

        raport = generuj_raport(file_path)
        self.assertEqual(raport, expected_output.to_dict())

    def test_with_one_invalid_log(self):
        file_path = "test/inputs/jedenWadliwyLog.txt"
        expected_output = Raport(
            wadliwe_logi=["2023-x1-01 23:5x 10xC"],
            procent_wadliwych_logow=100.0
        )

        raport = generuj_raport(file_path)
        self.assertEqual(raport, expected_output.to_dict())

    def test_from_spec_first_Example(self):
        file_path = "test/inputs/test_first_from_spec.txt"
        expected_output = Raport(
            czas_trwania_raportu=70,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=95.0))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

    def test_from_spec_second_Example(self):
        file_path = "test/inputs/test_second_from_spec.txt"
        expected_output = Raport(
            wadliwe_logi=["2023-x1-01 23:5x 10xC", "2023-01-02 00:10"],
            procent_wadliwych_logow=40.0,
            czas_trwania_raportu=70,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=95.0),
            problemy=Problemy(wysoki_poziom_zaklocen_EM=True))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

    def test_from_spec_second_Example(self):
        file_path = "test/inputs/test_third_from_spec.txt"
        expected_output = Raport(
            wadliwe_logi=["2023-x1-01 23:5x 10xC",
                          "2023-01-02 00:15 -78C",
                          "2023-01-02 01:10"],
            procent_wadliwych_logow=30.0,
            czas_trwania_raportu=120,
            temperatura=Temperatura(max=115.3, min=90.0, srednia=102.4),
            najdluzszy_czas_przegrzania=40,
            liczba_okresow_przegrzania=2,
            problemy=Problemy(True, True))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

    def test_with_przegrzanie_alkoholowe(self):
        file_path = "test/inputs/fast_pivo.txt"
        expected_output = Raport(
            wadliwe_logi=[
                          "2023-01-02 01:20"],
            procent_wadliwych_logow=20.0,
            czas_trwania_raportu=50,
            temperatura=Temperatura(max=115.3, min=100.1, srednia=105.4),
            najdluzszy_czas_przegrzania=50,
            liczba_okresow_przegrzania=1,
            problemy=Problemy(True, True))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())


if __name__ == '__main__':
    unittest.main()
