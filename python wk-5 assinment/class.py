# Base class
class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def call(self, number):
        if self.battery > 0:
            print(f"{self.brand} {self.model} is calling {number} 📞...")
            self.battery -= 5
        else:
            print("Battery dead! Please charge.")
    
    def text(self, number, message):
        if self.battery > 0:
            print(f"Texting {number}: {message}")
            self.battery -= 2
        else:
            print("Battery dead! Please charge.")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")


# Inherited class (specialized smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system=True):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        if self.battery > 10:
            print(f"Playing {game} on {self.brand} {self.model} 🎮...")
            self.battery -= 15
        else:
            print("Not enough battery to play a game! ⚡")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S25")
gaming_phone = GamingPhone("Asus", "ROG Phone 8")

phone1.call("123-456-789")
phone1.charge(20)

gaming_phone.play_game("Genshin Impact")
gaming_phone.charge(30)
