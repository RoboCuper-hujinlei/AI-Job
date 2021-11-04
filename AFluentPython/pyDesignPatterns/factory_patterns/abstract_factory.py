import os
import sys


'''
    抽象工厂，简单理解抽象工厂是多个工厂模式的集合, 当我们需要跟踪对象创建，解耦对象创建与使用。使用这两种模式
'''
# 青蛙角色
class Frog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)

# 虫
class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


'''
    FrogWorld类是一个工厂模式，它的主要任务是创建游戏中的主角和障碍物。保持创建方法的独立性和名称的通用性

    我们将不需要修改任何代码，动态的更改处于激活状态的工厂(游戏)
'''
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    
    def __str__(self):
        return '\n\n\t-------Frog world----------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()



# Wizard factory
class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()



        

# test
def Game_FrogWorld():
    # Frog("frog").interact_with(Bug())
    game = FrogWorld("FROG")

    player = game.make_character()
    obs = game.make_obstacle()
    player.interact_with(obs)

def Game_Wizard():
    game = WizardWorld("Wizard")
    player = game.make_character()
    obs = game.make_obstacle()
    player.interact_with(obs)


# 抽象工厂 
class game_environment():
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)
        

def validate_age(name): # 控制有效输入的age 异常处理
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name? ")
    valid_input = False     # 控制有效输入

    while not valid_input:
        valid_input, age = validate_age(name)

    game = FrogWorld if age < 18 else WizardWorld
    environment = game_environment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
    
