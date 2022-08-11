import logging
#create and configure logger
logging.basicConfig(filename='mine.log',
                    level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s: %(name)s: %(message)s')

#file_handler = logging.FileHandler('mine.log')
#file_handler.setLevel(logging.DEBUG)

class Calculations:
    def __init__(self,list):
        self.list = list
    def add(self):
        addition = self.list[1]+self.list[2]
        logging.info('Add :' f'{addition}')
    def sub(self):
        subtraction = self.list[5] - self.list[5]
        logging.debug('Sub :' f'{subtraction}')
    def mul(self):
        multiplication = self.list[6] * self.list[7]
        logging.debug('Mul :' f'{multiplication}')
    def div(self):
        try:
            division = self.list[9] / self.list[10]
            logging.debug('Div :' f'{division}')
        except ZeroDivisionError:
            logging.exception("Tried to divide by 0")
        else:
            print(self.list[9] / self.list[10])

list = [10,9,8,7,6,5,4,3,2,1,0]
p1 = Calculations(list)
p1.add()
p1.sub()
p1.mul()
p1.div()
