
from model import Model
from viewMainWindow import View

class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def main(self):
       self.view.main()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()