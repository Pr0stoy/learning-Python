class Enemy:
    def __init__(self,enemy_id):
        self.id = enemy_id
        self.hp = 100
    def __repr__(self):
        return f"Enemy {self.id} has {self.hp} hp"
    def take_damage(self,amount_damage):
        self.hp -= amount_damage
        if self.hp <= 0:
            print(f"Enemy{self.id} is dead")
enemies = [Enemy(i) for i in range(1,11)]
print(enemies)
enemies[3].take_damage(60)
print(enemies)