import json
import os


class Car():
    def __init__(self, name="", type=0, creator=0, color=0, privod=0, box_type=0, v_engine=0):
        self.name = str(name)
        self.type = type
        self.creator = creator
        self.color = color
        self.privod = privod
        self.box_type = box_type
        self.door_status = ["closed", "closed", "closed", "closed"]
        self.rotators_status = ["not_work", "not_work"]
        self.v_engine = v_engine
        if name != "":
            self.save()
            cars_dict[str(name)] = self

    def get_info(self):
        return [f"""Имя: {self.name}
Тип машины {self.type}
Производитель: {self.creator}
Привод: {self.privod}
Тип коробки: {self.box_type}
Объем двигателя: {float(self.v_engine)}
Статус дверей:
    Левая передняя: {self.door_status[0]}
    Правая передняя: {self.door_status[1]}
    Левая задняя: {self.door_status[2]}
    Правая задняя: {self.door_status[3]}
Статус поворотников:
    Левый: {self.rotators_status[0]}
    Правый: {self.rotators_status[1]}
""", f"<font color='{self.color}' size = 21 >▉</font>"]

    def open_door(self, door_index: int):
        if self.door_status[door_index] == "open":
            self.door_status[door_index] = "close"
        else:
            self.door_status[door_index] = "open"
        self.save()

    def activate_rotator(self, rotator_index: int):
        if self.rotators_status[rotator_index] == "work":
            self.rotators_status[rotator_index] = "not_work"
        else:
            self.rotators_status[rotator_index] = "work"
        self.save()

    def restore(self, name):
        with open(f"data/cars/{name}.json", "r") as r_file:
            car = json.load(r_file)
            self.name = car["name"]
            self.type = car["type"]
            self.creator = car["creator"]
            self.color = car["color"]
            self.privod = car["privod"]
            self.box_type = car["box_type"]
            self.door_status = car["door_status"]
            self.rotators_status = car["rotators_status"]
            self.v_engine = car["v_engine"]
            cars_dict[str(self.name)] = self

    def save(self):
        with open(f"data/cars/{self.name}.json", "w", encoding="utf-8") as w_file:
            car = {
                "name": self.name,
                "type": self.type,
                "creator": self.creator,
                "color": self.color,
                "privod": self.privod,
                "box_type": self.box_type,
                "door_status": self.door_status,
                "rotators_status": self.rotators_status,
                "v_engine": self.v_engine
            }
            json.dump(car, w_file)
        with open(f"data/info/names.json", "r", encoding="utf-8") as r_file:
            old_data = json.load(r_file)
            if self.name not in old_data["names"]:
                old_data["names"].append(self.name)
                with open(f"data/info/names.json", "w", encoding="utf-8") as r_file:
                    json.dump(old_data, r_file)

    def delete_data(self):
        os.remove(f'data/cars/{self.name}.json')
        if self.name in cars_dict.keys():
            del cars_dict[str(self.name)]
        with open(f"data/info/names.json", "r", encoding="utf-8") as r_file:
            old_data = json.load(r_file)
            if self.name in old_data["names"]:
                old_data["names"].remove(str(self.name))
            with open(f"data/info/names.json", "w", encoding="utf-8") as r_file:
                json.dump(old_data, r_file)


class Tools():
    def get_cars_list():
        with open(f"data/info/names.json", "r", encoding="utf-8") as r_file:
            names = json.load(r_file)["names"]
        return names

    def check_name(name):
        with open(f"data/info/names.json", "r", encoding="utf-8") as r_file:
            names = json.load(r_file)["names"]
            if name in names:
                return False
            else:
                return True

    def get_correct_car_object(name):
        if name in cars_dict.keys():
            car = cars_dict[name]
        else:
            car = Car()
            car.restore(name)
        return car


cars_dict = {}