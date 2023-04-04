import unittest

from main import generate_raport


class EmptyTest(unittest.TestCase):
    def test_empty_file(self):
        file_path = "test/inputs/empty_file.txt"
        expected_output = {
            "wadliwe_logi": [],
            "procent_wadliwych_logow": "100.0",
            "czas_trwania_raportu": 0,
            "temperatura": {
                "max": None,
                "min": None,
                "srednia": None
            },
            "najdluzszy_czas_przegrzania": 0,
            "liczba_okresow_przegrzania": 0,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": False,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
            }
        }
        self.assertEqual(generate_raport(file_path), expected_output)

    def test_from_spec_first_Example(self):
        file_path = "test/inputs/test_first_from_spec.txt"

        expected_output = {
            "wadliwe_logi": [],
            "procent_wadliwych_logow": "0.0",
            "czas_trwania_raportu": 70,
            "temperatura": {
                "max": "100.0",
                "min": "90.0",
                "srednia": "95.0"
            },
            "najdluzszy_czas_przegrzania": 0,
            "liczba_okresow_przegrzania": 0,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": False,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
            }
        }
        self.assertEqual(generate_raport(file_path), expected_output)

    def test_from_spec_second_Example(self):
        file_path = "test/inputs/test_second_from_spec.txt"

        expected_output = {
            "wadliwe_logi": [
            "2023-x1-01 23:5x 10xC",
                             "2023-01-02 00:10"],
            "procent_wadliwych_logow": "40.0",
            "czas_trwania_raportu": 70,
            "temperatura": {
                "max": "100.0",
                "min": "90.0",
                "srednia": "95.0"
            },
            "najdluzszy_czas_przegrzania": 0,
            "liczba_okresow_przegrzania": 0,
            "problemy": {
                "wysoki_poziom_zaklocen_EM": True,
                "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": False
            }
        }
        self.assertEqual(generate_raport(file_path), expected_output)


if __name__ == '__main__':
    unittest.main()
