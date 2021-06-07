# gladiator
import random

# armor, speed, weapon reach, health, damage


murmillo = [60, 20, 70, 30, 5]

retiarius = [20, 50, 100, 20, 15]

thraex = [40, 100, 20, 25, 10]

classes = [murmillo, retiarius, thraex]
player = []
opponent = []

setup = True
in_combat = False

# functions


def interface():
    print(health_bar(health))


def health_bar(hp):
    display_hp = hp * '|'
    return display_hp


def hit_chance(armor, speed, weapon_reach):
    pct_chance = (speed + weapon_reach) / armor * 10
    return pct_chance


def attack(x):
    if x > random.randint(1, 100):
        return True
    else:
        return False


def defend():
    print('holder')


print("""Choose your class:
                
                1 - Murmillo
                2- Retiarius
                3- Thraex   
                                        Enter 'I' for info.
                                        """)

while setup:
    class_choice = input("""Enter the number corresponding with your class choice.
    > """).lower()
    if class_choice == '1':
        print('you have chosen murmillo')
        player = murmillo
        break
    elif class_choice == '2':
        print('you have chosen retiarius')
        player = retiarius
        break
    elif class_choice == '3':
        print('you have chosen thraex')
        player = thraex
        break
    elif class_choice == 'i':
        print("""Thraex: 
Armed with a small rectangular or circular shield called a parmula. A very short
sword with a slightly curved blade called a sica, which was intended to maim the
opponents unarmoured back. His other armor included greaves, a protective belt
above a loin cloth, and a helmet with a visor. The Thraex relied on his speed and
agility to outmaneuver his more heavily armored opponents.

Retiarius: 
The net-fighter made up for his lack of protective gear by using his speed and
agility to avoid his opponent's attacks and waiting for the opportunity to strike.
He first tried to throw his net over his rival. If this succeeded, he attacked
with his trident while his adversary was entangled. Another tactic was to ensnare
his enemy's weapon in the net and pull it out of his grasp, leaving the opponent
defenceless.

Murmillo: 
Depends on his strength and endurance to survive the battle
against foes who were more suited to attacking. The tower shield gave him an
edge in defence and the gladius enabled him to thrust and swing at his enemies
when in close range.
""")
    else:
        print('Invalid Input')
setup = False
opponent = random.choice(classes)
print('Your opponent will be...')
if opponent == retiarius:
    print('the retiarius')
if opponent == murmillo:
    print('the murmillo')
if opponent == thraex:
    print('the thraex')
health = player[3]
enemy_health = opponent[3]
# is_ready = input("""are you ready? y/n """).lower()
# if is_ready == 'y':
#     in_combat = True
# elif is_ready == 'n':
#     print('take your time...')
# else:
#     print('invalid input')
in_combat = True
while in_combat:
    print(f'*  Your health: {health_bar(health)}', end=str(abs(25 - health) * ' ' + ' * '))
    print(f'Enemy Health: {health_bar(enemy_health)}', end=str(abs(25 - enemy_health) * ' ' + ' * '))
    print(' ')
    test = input('press f to fight ')
    if test == 'f':
        fight = attack(hit_chance(opponent[0], player[1], player[2]))
        if fight:
            print('you did damage')
            enemy_health -= random.randint(1, player[4])
        elif not fight:
            print('you missed')
        enemy_fight = attack(hit_chance(player[0], opponent[1], opponent[2]))
        if enemy_fight:
            print('enemy did damage')
            health -= random.randint(1, opponent[4])
            # print(f"Health: {health}")
        elif not enemy_fight:
            print('you dodged the attack')
        if enemy_health <= 0:
            print('you won the fight!')
            break
        elif health <= 0:
            print('you lost the fight.')
            break
print('thank you for playing')
