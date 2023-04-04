import pprint
import json

class Temperatura:
    max = 0.0
    min = 0.0
    srednia = 69.0

    def to_json(self) -> str:
        obj = {
            "max": str(round(self.max, 1)),
            "min": str(round(self.min, 1)),
            "srednia": str(round(self.srednia, 1))
        }
        return json.dumps(obj, indent=2)

    def __repr__(self) -> str:
        return self.to_json()

class Problemy:
    wysoki_poziom_zaklocen_EM = False
    wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = False

    def to_json(self) -> str:
        obj = {
            "wysoki_poziom_zaklocen_EM" : self.wysoki_poziom_zaklocen_EM,
            "wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury" : self.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury
        }
        return json.dumps(obj, indent=2)

    def __repr__(self) -> str:
        s = self.to_json()
        return s.replace("false", "False").replace("true", "True")


class Raport:
    wadliwe_logi = []
    procent_wadliwych_logow = 0.0
    czas_trwania_raportu = 0
    temperatura = Temperatura()
    najdluzszy_czas_przegrzania = 0
    liczba_okresow_przegrzania = 0
    problemy = Problemy()

    def to_json(self) -> str:
        obj = {
            "wadliwe_logi": self.wadliwe_logi,
            "procent_wadliwych_logow": str(self.procent_wadliwych_logow),
            "czas_trwania_raportu": self.czas_trwania_raportu,
            "temperatura": json.loads(self.temperatura.to_json()),
            "najdluzszy_czas_przegrzania": self.najdluzszy_czas_przegrzania,
            "liczba_okresow_przegrzania": self.liczba_okresow_przegrzania,
            "problemy": json.loads(self.problemy.to_json())
        }
        return json.dumps(obj, indent=2)

    def __repr__(self) -> str:
    
        s = self.to_json()
        return s.replace("false", "False").replace("true", "True")

if __name__ == '__main__':
    temperatura = Temperatura()
    temperatura.max = 100.0
    temperatura.min = 2.0
    temperatura.srednia = 69.0
    problemy = Problemy()
    problemy.wysoki_poziom_zaklocen_EM = True
    problemy.wysokie_ryzyko_uszkodzenia_silnika_z_powodu_temperatury = False
    raport = Raport()
    raport.wadliwe_logi = ["dupa","dupa2"]
    print(raport)
