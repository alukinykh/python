# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

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
        if department_name not in self.department.keys():
            raise ValueError("Wrong department")
        if moving_office_equipment:
            self.department[department_name].append(moving_office_equipment)
            self.store.remove(moving_office_equipment)
        else:
            raise ValueError(f"There is no office equipment with serial number {serial_number} in store")


class OfficeEquipment:
    def __init__(self, serial_number, doc='doc1'):
        if not serial_number:
            raise ValueError("Serial number can't be empty.")
        self.serial_number = serial_number
        self.doc = doc


class Printer(OfficeEquipment):
    def __init__(self, serial_number, doc='doc3', print_technology='jet'):
        super().__init__(serial_number, doc)
        self.print_technology = print_technology

    def __str__(self):
        return f"Printer({self.serial_number})"

    def print_action(self):
        print(f'Print {self.doc}')


class Scanner(OfficeEquipment):
    def __init__(self, serial_number, doc='doc2', colored=False):
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
    def __init__(self, serial_number, doc='doc4'):
        super().__init__(serial_number, doc)

    def __str__(self):
        return f"Copier({self.serial_number})"

    def copy_action(self):
        print(f'Copy {self.doc}')


store = Store()

while True:
    print('=' * 10)
    print("ADD 'TYPE' 'SERIAL NUMBER' - add 'TYPE'(printer, scanner or copier)"
          "office equipment to warehouse.")
    print("MOVE 'SERIAL NUMBER' 'DEPARTMENT' - move office equipment"
          "with 'SERIAL NUMBER' to 'DEPARTMENT'.")
    print("PRINT - print current warehouse state.")
    print("STOP - stop program.")
    command_line = input("Command: ")
    if command_line:
        command_line = command_line.split()
        command = command_line[0]
        if command == "STOP" and len(command_line) == 1:
            break
        if command == "PRINT" and len(command_line) == 1:
            print(store)
            continue
        if command == "ADD" and len(command_line) == 3:
            equip_type = command_line[1]
            if equip_type in ["printer", "scanner", "copier"]:
                serial_number = command_line[2]
                try:
                    if equip_type == "printer":
                        store.add_equipment(Printer(serial_number))
                    elif equip_type == "scanner":
                        store.add_equipment(Scanner(serial_number))
                    else:
                        store.add_equipment(Copier(serial_number))
                except ValueError as error:
                    print(error)
            else:
                print("Wrong type of office equipment.")
            continue
        if command == "MOVE" and len(command_line) == 3:
            serial_number = command_line[1]
            department = command_line[2]
            try:
                store.move_to_department(serial_number, department)
            except ValueError as error:
                print(error)
            continue
        print("Wrong command.")