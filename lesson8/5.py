# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class Store:
    def __init__(self):
        self.store = []
        self.department = {'first': [], 'second': [], 'third': []}

    def __str__(self):
        warehouse_str = " ".join(str(office_equipment)
                                 for office_equipment in self.store)
        departments_str = "\n".join(
            f"{department}: {' '.join(str(equip) for equip in equips)}"
            for department, equips in self.department.items())
        return f"***\nIn store: {warehouse_str}\nIn departments:\n{departments_str}\n***"

    def add_equipment(self, equipment):
        self.store.append(equipment)

    def move_to_department(self, serial_number, department_name):
        moving_office_equipment = next(
            (office_equipment for office_equipment in self.store
             if office_equipment.serial_number == serial_number), None)
        if department_name in self.department.keys() and moving_office_equipment:
            self.department[department_name].append(moving_office_equipment)
            self.store.remove(moving_office_equipment)


class OfficeEquipment:
    def __init__(self, serial_number, doc):
        self.serial_number = serial_number
        self.doc = doc


class Printer(OfficeEquipment):
    def __init__(self, serial_number, doc, print_technology):
        super().__init__(serial_number, doc)
        self.print_technology = print_technology

    def __str__(self):
        return f"Printer({self.serial_number})"

    def print_action(self):
        print(f'Print {self.doc}')


class Scanner(OfficeEquipment):
    def __init__(self, serial_number, doc, colored=False):
        super().__init__(serial_number, doc)
        self.colored = colored

    def __str__(self):
        return f"Scanner({self.serial_number})"

    def scan_action(self):
        text = 'in black and white'
        if self.colored:
            text = 'colored'
        print(f'Scan {text} {self.doc}')


class Copier(OfficeEquipment):
    def __init__(self, serial_number, doc):
        super().__init__(serial_number, doc)

    def __str__(self):
        return f"Copier({self.serial_number})"

    def copy_action(self):
        print(f'Copy {self.doc}')


store1 = Store()
store1.add_equipment(Printer('p-1-1', 'doc1', 'jet'))
store1.add_equipment(Printer('p-2-1', 'doc2', 'jet'))
store1.add_equipment(Scanner('s-1-2', 'doc2', True))
store1.add_equipment(Scanner('s-2-2', 'doc2', False))
store1.add_equipment(Copier('c-1-3', 'doc3'))
print(store1)

store1.move_to_department('s-1-2', 'first')
store1.move_to_department('c-1-3', 'second')
store1.move_to_department('p-2-1', 'third')
print(store1)
