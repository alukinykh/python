# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    pass


class OfficeEquipment:
    def __init__(self, serial_number, doc):
        self.serial_number = serial_number
        self.doc = doc


class Printer(OfficeEquipment):
    def __init__(self, serial_number, doc, print_technology):
        super().__init__(serial_number, doc)
        self.print_technology = print_technology

    def print_action(self):
        print(f'Print {self.doc}')


class Scanner(OfficeEquipment):
    def __init__(self, serial_number, doc, colored=False):
        super().__init__(serial_number, doc)
        self.colored = colored

    def scan_action(self):
        text = 'in black and white'
        if self.colored:
            text = 'colored'
        print(f'Scan {text} {self.doc}')


class Copier(OfficeEquipment):
    def __init__(self, serial_number, doc):
        super().__init__(serial_number, doc)

    def copy_action(self):
        print(f'Copy {self.doc}')


printer = Printer('p-1-1', 'doc1', 'jet')
printer.print_action()
scanner = Scanner('s-1-2', 'doc2', True)
scanner.scan_action()
copier = Copier('c-1-3', 'doc3')
copier.copy_action()
