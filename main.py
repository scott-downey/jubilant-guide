import random
import customtkinter
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('CustomTkinter - Example App')
        self.geometry('700x450')
        self.t = customtkinter.CTkLabel(master=self, text="Hello World!").pack()
        self.m = customtkinter.CTkOptionMenu(master=self).pack()
        self.menu = tkinter.Menu()
        self.notebook = customtkinter.CTkTabview(self, width=10, height=10)
        self.notebook.add("Tab1")
        self.notebook.add("Tab2")
        self.notebook.pack(padx=20, pady=20, expand=True)


class Simulation(object):
    def __init__(self, weapon, ship):
        self.Weapon = weapon
        self.Ship = ship

    def run(self, iterations = 100):
        aggregate = {}
        for shot in range(iterations):
            result = self.Ship.attack(self.Weapon, False)
            if aggregate.keys().__contains__(result):
                aggregate[result] += 1
            else:
                aggregate[result] = 1
        print('results', aggregate)

class WeaponClass(object):
    def __init__(self, shots: int, strength: int):
        self.Attacks = shots
        self.Strength = strength


class Weapons(object):
    def __init__(self):
        self.EnergyCannon = WeaponClass(3,1)
        self.GigaCannon = WeaponClass(1,4)
        self.LinkedRailgun = WeaponClass(3,1)
        self.PlasmaCannon = WeaponClass(2,3)


class ShipClass(object):
    def __init__(self, lvl: int, tough, evasion):
        self.Level = lvl
        self.Toughness = tough
        self.Evasion = evasion

    def attack(self, weapon: WeaponClass, rearShot: bool):
        successfulShots = 0

        for shot in range(weapon.Attacks):
            # print('\tShot: ', shot + 1)
            # The attacker rolls as many dice as the weapon's attacks, trying to score the target's evasion value
            # 1 hit per => evasion
            # If rearShot, +1 to hit
            unmodifiedRoll = random.randrange(1, 6)
            roll = unmodifiedRoll + 1 if rearShot else unmodifiedRoll
            # print('\tRoll: ', roll, 'against Evasion:', self.Evasion)
            if roll >= self.Evasion:
                # print('\tHit!')
                successfulShots += 1

        damage = successfulShots
        # print('Rolling for', successfulShots, 'successfulShots') #This is back to front, you're rolling to save
        for hit in range(successfulShots):
            unmodifiedRoll = random.randrange(1, 6)
            roll = unmodifiedRoll - 1 if rearShot else unmodifiedRoll
            # print('\tRoll: ', roll, 'minus Weapon Strength:', weapon.Strength ,'against,', self.Toughness)
            if roll - weapon.Strength >= self.Toughness:
                # print('Dmg!')
                damage -= 1
            # Roll against self.Toughness
            # - weapon.Strength
            # If rearShot, -1
        return damage

class Ships(object):
    def __init__(self):
        self.Destroyer = ShipClass(3,3,3)

if __name__ == "__main__":
    customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
    app = App()
    weapons = Weapons()
    ships = Ships()
    sim = Simulation(weapons.LinkedRailgun, ships.Destroyer)
    sim.run(10000)
    app.mainloop()