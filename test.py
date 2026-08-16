# def check_temps(temperatures):
#     for i in temperatures:
#         if i < 0:
#             return True
#     return False

# print(check_temps([12, 15, 8, -2, 5]))  # Should print True
# print(check_temps([10, 14, 22, 18]))   # Should print False
character = {
    "name": "",
    "passwd":"",
    "health":"",
    "strenght":"",
}
def assign_stats(character):
    character_login = input("write login ")
    character_stats = input("write stats ")

    login_passwd = character_login.split(" ")
    health_strenght = character_stats.split(" ")

    login = login_passwd[0]
    passwd = login_passwd[1]

    character["name"] = login
    character["passwd"] = passwd

    health = health_strenght[0]
    strenght = health_strenght[1]

    character["health"] = int(health)
    character["strenght"] = int(strenght)
    return character
print(assign_stats(character))

def deal_damage(character):
    deal = input("how much ")
    character["health"] -= int(deal)
    return character
print(deal_damage(character))