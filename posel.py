class Posel:
    def __init__(self, nazwa: str, partia: str, wyksztalcenie: str, szkola: str, zawod: str):
        self.nazwa = nazwa
        self.partia = partia
        self.wyksztalcenie = wyksztalcenie,
        self.szkola = szkola
        self.zawod = zawod

    def obj_into_tuple(self):
        return self.nazwa, self.partia, self.wyksztalcenie, self.szkola, self.zawod