class Neuron():
    # Класс, моделирует поведение нейрона в нервной системе
    def __init__(self, kod=0, axon=1, dendrite=1):
        self.kod = kod
        self.axon = axon
        self.dendrite = dendrite
        self.status = 0

    def action(self):
        if self.status == 1:
            self.status = 0
            return True
        else:
            return False

