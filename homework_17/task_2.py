id_counter = 1

class Car:
    global id_counter
    def __init__(self):
        global id_counter
        self.id = id_counter
        id_counter += 1


class CarCommander:
    global id_counter
    def __init__(self):
        global id_counter
        self.id = id_counter
        id_counter += 1


class CarGunner:
    global id_counter
    def __init__(self):
        global id_counter
        self.id = id_counter
        id_counter += 1


def check_object_id_collector():
    expected_ids = (1, 2, 3, 4, 5)
    actual_ids = (CarGunner().id, CarGunner().id, Car().id, CarCommander().id, Car().id)
    if actual_ids == expected_ids:
        print('Test passed. Amazing job!')
    else:
        print(f'Expected_ids: {expected_ids}. Actual_ids: {actual_ids}.')


check_object_id_collector()

