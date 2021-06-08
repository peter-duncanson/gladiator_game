# gladiator

import random

# armor, speed, weapon reach, health, damage

murmillo = [60, 20, 70, 25, 5]

retiarius = [20, 50, 100, 15, 15]

thraex = [40, 100, 20, 20, 10]

classes = [murmillo, retiarius, thraex]
player = []
opponent = []
wins = 0
deaths = 0
setup_1 = True
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
                2 - Retiarius
                3 - Thraex   
                                        Enter 'I' for info.
                                        """)

while setup_1:
    class_choice = input("""Enter the number corresponding with your class choice.
    > """).lower()
    if class_choice == '1':
        print("""
        You are the Murmillo, heavily armored, but slow.
        """)
        player = murmillo
        break
    elif class_choice == '2':
        print("""
        You are the Retiarius, your Net, Trident, and quick reflexes
        make up for your lack of armor. 
        """)
        player = retiarius
        break
    elif class_choice == '3':
        print("""
        You are the Thraex, lightning fast attacks and evasive maneuvers
        are your greatest ally.
        """)
        player = thraex
        in_combat = True
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
alive = True
setup_1 = False
is_dead = False
choose_class = False
while alive:

    print("Enter 'Y' to begin fight. ")
    begin = input("> ").lower()
    if begin == 'y':
        choose_class = True
    else:
        print('Invalid Input')
        choose_class = False
        in_combat = False
    while choose_class:
        opponent = random.choice(classes)
        print('Your opponent will be...', end=' ')
        if opponent == retiarius:
            print('The Retiarius')
        if opponent == murmillo:
            print('The Murmillo')
        if opponent == thraex:
            print('The Thraex')
        choose_class = False
        in_combat = True

    while in_combat:
        health = player[3]
        enemy_health = opponent[3]
        print(f'*  Your health: {health_bar(health)}', end=str(abs(25 - health) * ' ' + ' * '))
        print(f'Enemy Health: {health_bar(enemy_health)}', end=str(abs(25 - enemy_health) * ' ' + ' * '))
        print(' ')
        print("Enter 'F' to attack.")
        attack_enemy = input('> ').lower()
        if attack_enemy == 'f':
            fight = attack(hit_chance(opponent[0], player[1], player[2]))
            if fight:
                # murmillo
                if opponent == classes[0]:
                    print("""
                    You manage to hit a weak spot in the Murmillo's armor!
                    """)
                # retiarius
                elif opponent == classes[1]:
                    print("""
                    The Retiarius failed to dodge your attack!
                    """)
                # thraex
                elif opponent == classes[2]:
                    print("""
                    The Thraex was too slow for you!
                    """)
                enemy_health -= random.randint(1, player[4])
            elif not fight:
                # murmillo
                if opponent == classes[0]:
                    print("""
                    You failed to penetrate the Murmillo's armor!
                    """)
                # retiarius
                elif opponent == classes[1]:
                    print("""
                    The Retiarius gracefully dodges your attack!
                    """)
                # thraex
                elif opponent == classes[2]:
                    print("""
                    You miss the Thraex entirely!
                    """)
        elif attack_enemy != 'f':
            print('Invalid Input.')
        enemy_fight = attack(hit_chance(player[0], opponent[1], opponent[2]))
        if enemy_fight:
            # murmillo
            if opponent == classes[0]:
                print("""
                    The Murmillo hits you with a crushing blow!
                """)
            # retiarius
            elif opponent == classes[1]:
                print("""
                    The Retiarius tangles you in his net, and stabs you swiftly with his trident!
                """)
            # thraex
            elif opponent == classes[2]:
                print("""
                    The Thraex's curved sword slices into your skin!
                """)
            health -= random.randint(1, opponent[4])
            # print(f"Health: {health}")
        elif not enemy_fight:
            # murmillo
            if opponent == classes[0]:
                print("""
                     The Murmillo failed to hit you!
                 """)
            # retiarius
            elif opponent == classes[1]:
                print("""
                     The Retiarius attempts to tangle you in his net but fails!
                     Not today fish boy!
                 """)
            # thraex
            elif opponent == classes[2]:
                print("""
                     You manage to avoid the Thraex's attack!
                 """)
        if enemy_health <= 0:
            wins += 1
            print('Victory is yours!')
            break
        elif health <= 0:
            deaths += 1
            print('Oh dear, you are dead!')
            is_dead = True
            in_combat = False
            while is_dead:
                print("""
                    1 - Play again
                    2 - Quit
                    """)
                play_again = input('> ')
                if play_again == '1':
                    is_dead = False
                    in_combat = False
                if play_again == '2':
                    alive = False
                    in_combat = False
                    break
        # if attack_enemy == 'd':
        #     defend()

print('Thank you for playing.')
print(f"Kills: {wins}")
print(f"Deaths: {deaths}")
