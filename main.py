class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"Начинается битва между {self.player.name} и {self.computer.name}!")

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} пал в бою. {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} пал в бою. {self.computer.name} победил!")
                break


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
