import pathlib
import unittest
from src.Raport import Problemy, Raport, Temperatura

from main import generuj_raport


class EmptyTest(unittest.TestCase):
    def test_empty_file(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/empty_file.txt").absolute()
        expected_output = Raport(wadliwe_logi=[],
                                 procent_wadliwych_logow=100.0,
                                 czas_trwania_raportu=0,
                                 temperatura=Temperatura(None, None, None),
                                 najdluzszy_czas_przegrzania=0,
                                 liczba_okresow_przegrzania=0,
                                 problemy=Problemy(True, False))

        raport = generuj_raport(file_path)
        self.assertEqual(raport, expected_output.to_dict())

    def test_with_one_invalid_log(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/jedenWadliwyLog.txt").absolute()
        expected_output = Raport(wadliwe_logi=["2023-x1-01 23:5x 10xC"],
                                 procent_wadliwych_logow=100.0,
                                 czas_trwania_raportu=0,
                                 temperatura=Temperatura(None, None, None),
                                 najdluzszy_czas_przegrzania=0,
                                 liczba_okresow_przegrzania=0,
                                 problemy=Problemy(True, False))

        raport = generuj_raport(file_path)
        self.assertEqual(raport, expected_output.to_dict())

    def test_from_spec_first_Example(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/test_first_from_spec.txt").absolute()
        expected_output = Raport(wadliwe_logi=[],
                                 procent_wadliwych_logow=0.0,
                                 czas_trwania_raportu=70,
                                 temperatura=Temperatura(100.0, 90.0, 95.0),
                                 najdluzszy_czas_przegrzania=0,
                                 liczba_okresow_przegrzania=0,
                                 problemy=Problemy(False, False))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

    def test_from_spec_second_Example(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/test_second_from_spec.txt").absolute()
        expected_output = Raport(
            wadliwe_logi=["2023-x1-01 23:5x 10xC", "2023-01-02 00:10"],
            procent_wadliwych_logow=40.0,
            czas_trwania_raportu=70,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=95.0),
            najdluzszy_czas_przegrzania=0,
            liczba_okresow_przegrzania=0,
            problemy=Problemy(True, False))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

    def test_from_spec_third_Example(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/test_third_from_spec.txt").absolute()
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

    def test_with_incrorrect_date(self):
        file_path = (pathlib.Path(__file__).parent / "inputs/with_invalid_date.txt").absolute()
        expected_output = Raport(
            wadliwe_logi=["2023-01-32 00:10 95C"],
            procent_wadliwych_logow=25.0,
            czas_trwania_raportu=60,
            temperatura=Temperatura(max=100.0, min=90.0, srednia=96.3),
            najdluzszy_czas_przegrzania=0,
            liczba_okresow_przegrzania=0,
            problemy=Problemy(True, False))

        result = generuj_raport(file_path)
        self.assertEqual(result, expected_output.to_dict())

if __name__ == '__main__':
    unittest.main()
