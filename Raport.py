import json


class Temperatura:

    def __init__(self,
                 max=None,
                 min=None,
                 srednia=None):
        self.max = max
        self.min = min
        self.srednia = srednia

    def to_dict(self):
        return {
            "max": None if self.max is None else str(round(self.max, 1)),
            "min": None if self.min is None else str(round(self.min, 1)),
            "srednia": None if self.srednia is None else str(round(self.srednia, 1))
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self) -> str:
        return self.to_json().replace("null", "None")


class Problemy:

    def __init__(self,
                 wysoki_poziom_zaklocen_EM=False,
                 wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury=False):
        self.wysoki_poziom_zaklocen_EM = wysoki_poziom_zaklocen_EM
        self.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury

    def to_dict(self):
        return {
            "wysoki_poziom_zaklocen_EM": self.wysoki_poziom_zaklocen_EM,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury": self.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self) -> str:
        s = self.to_json()
        return s.replace("false", "False").replace("true", "True")


class Raport:

    def __init__(self,
                 wadliwe_logi=[],
                 procent_wadliwych_logow=100.0,
                 czas_trwania_raportu=0,
                 temperatura=Temperatura(),
                 najdluzszy_czas_przegrzania=0,
                 liczba_okresow_przegrzania=0,
                 problemy=Problemy()):
        self.wadliwe_logi = wadliwe_logi
        self.procent_wadliwych_logow = procent_wadliwych_logow
        self.czas_trwania_raportu = czas_trwania_raportu
        self.temperatura = temperatura
        self.najdluzszy_czas_przegrzania = najdluzszy_czas_przegrzania
        self.liczba_okresow_przegrzania = liczba_okresow_przegrzania
        self.problemy = problemy

    def to_dict(self):
        return {
            "wadliwe_logi": self.wadliwe_logi,
            "procent_wadliwych_logow": str(self.procent_wadliwych_logow),
            "czas_trwania_raportu": self.czas_trwania_raportu,
            "temperatura": self.temperatura.to_dict(),
            "najdluzszy_czas_przegrzania": self.najdluzszy_czas_przegrzania,
            "liczba_okresow_przegrzania": self.liczba_okresow_przegrzania,
            "problemy": self.problemy.to_dict()
        }

    #For debugging purposes :) 
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self) -> str:

        s = self.to_json()
        return s.replace("false", "False").replace("true", "True").replace("null", "None")
