class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

        self.armore = None
        self.weapon = None

        self.inventory = {
            "броня": [],
            "оружие": [],
            "хилки": [],
            "ключи": [],
            "другие предметы": []
        }

    def add_armore(self, name, health, absorption):
        if health <= 0:
            print("Прочность новой брони должна быть больше нуля.")
            return

        if absorption < 0 or absorption > 100:
            print("Поглощение должно быть от 0 до 100%.")
            return

        self.inventory["броня"].append({
            "name": name,
            "health": health,
            "absorption": absorption
        })

    def add_weapon(self, name, damage):
        if damage < 0:
            print("Урон оружия не может быть отрицательным.")
            return

        self.inventory["оружие"].append({
            "name": name,
            "damage": damage
        })

    def add_heal(self, name, healing):
        if healing <= 0:
            print("Лечение должно быть больше нуля.")
            return

        self.inventory["хилки"].append({
            "name": name,
            "healing": healing
        })

    def add_item(self, name, category):
        if category not in ("ключи", "другие предметы"):
            print("Здесь можно добавить ключ или другой предмет.")
            return

        self.inventory[category].append({"name": name})

    def get_inventory(self):
        """Общий список предметов."""
        items = []

        for category in self.inventory:
            items.extend(self.inventory[category])

        return items

    def show_inventory(self):
        for category, items in self.inventory.items():
            print(f"\n{category}:")

            if not items:
                print("  Пусто")

            for index, item in enumerate(items):
                print(f"  {index}: {item['name']}")

    def get_item(self, category, index):
        if category not in self.inventory:
            print("Такой категории нет.")
            return None

        if not isinstance(index, int):
            print("Номер предмета должен быть целым числом.")
            return None

        items = self.inventory[category]

        if index < 0 or index >= len(items):
            print("Предмета с таким номером нет.")
            return None

        return items[index]

    def equip_armore(self, index):
        item = self.get_item("броня", index)

        if item is None:
            return

        if item["health"] <= 0:
            print("Эта броня сломана.")
            return

        self.armore = item
        print(f"Надета броня: {item['name']}.")

    def equip_weapon(self, index):
        item = self.get_item("оружие", index)

        if item is None:
            return

        self.weapon = item
        print(f"Выбрано оружие: {item['name']}.")

    def take_damage(self, damage):
        if damage < 0:
            print("Урон не может быть отрицательным.")
            return 0

        if self.health <= 0:
            print(f"{self.name} уже погиб.")
            return 0

        absorbed = 0

        if self.armore is not None and self.armore["health"] > 0:
            # Сколько урона броня должна поглотить.
            absorption = damage * self.armore["absorption"] / 100

            # Нельзя поглотить больше оставшейся прочности.
            absorbed = min(absorption, self.armore["health"])
            self.armore["health"] -= absorbed

            print(f"Броня поглотила {absorbed} урона.")

            if self.armore["health"] == 0:
                print("Броня сломалась.")

        remaining_damage = damage - absorbed
        lost_health = min(self.health, remaining_damage)
        self.health -= lost_health

        print(f"{self.name} потерял {lost_health} HP.")

        if self.health == 0:
            print(f"{self.name} погиб.")

        return lost_health

    def attack(self, enemy):
        if self.health <= 0:
            print("Погибший игрок не может атаковать.")
            return 0

        if self.weapon is None:
            print("Сначала выбери оружие.")
            return 0

        return enemy.take_damage(self.weapon["damage"])

    def use_heal(self, index):
        if self.health <= 0:
            print("Хилка не может воскресить погибшего игрока.")
            return 0

        item = self.get_item("хилки", index)

        if item is None:
            return 0

        self.health += item["healing"]
        self.inventory["хилки"].pop(index)

        print(f"Восстановлено {item['healing']} HP.")
        return item["healing"]
    