from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.Player_1= Robot("The Tin Man")
        self.Player_2= Dinosaur("Godzilla", 15)

  
    def display_welcome(self):
        print("Welcome all to the match of DEATH where only ONE will survive!")

    
    def battle_phase(self):
        
        
        while self.Player_1.health > 0 and self.Player_2.health >0:
            self.Player_1.attack(self.Player_2) 
            self.Player_2.attack(self.Player_1)
            print (f"Robot {self.Player_1.name} attacked dinosaur {self.Player_2.name} with a {self.Player_1.active_weapon.name} for {self.Player_1.active_weapon.attack_power} damage! ")
            print (f"Dinosaur {self.Player_2.name} has a {self.Player_2.health} health remaining!")
            if self.Player_2.health== 0:
                break
            print(f"Dinosaur {self.Player_2.name} attacked {self.Player_1.name} for {self.Player_2.attack_power} damage!")
            print(f"Robot {self.Player_1.name} has {self.Player_1.health} health remaining!")
            
                
        




    def display_winner(self):

        if self.Player_1.health ==0:
            print (f"{self.Player_2.name} has won the match!! {self.Player_1.name} lost! ")

        elif self.Player_2.health ==0:
            print(f"{self.Player_1.name} has won the match!! {self.Player_2.name} lost!")

           
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


