import csv

class SaveCoup:
    def __init__(self, file_path):
        self.file_path = file_path
        self.coups = self.verif_coups()

    def verif_coups(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                coups = list(reader)
                if coups:
                    return coups[0]
                else:
                    return []
        except FileNotFoundError:
            return []

    def save(self, coup):
        if coup not in self.coups:
            self.coups.append(coup)
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(coup)

    def delimite_partie(self):
        with open(self.file_path, 'a', newline='') as file:
            file.write('### Fin de la partie ###\n')

        