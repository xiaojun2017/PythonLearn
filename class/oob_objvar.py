class Robot:
    """表示带有一个名字的机器人."""
    # 变量，记录机器人数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print('(Initializing {})'.format(self.name))

        # 当有人被创建时，人口数量自增加1
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is died".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('there are still {:d} robots working.'.format(Robot.population))

    def saye_hi(self):
        """来自机器人的问候

        没问题，你做得到"""
        print('Greetings, my masters call me {} {}'.format(self.name, self.__class__.population))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print('we have {:d} robots.'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.saye_hi()
Robot.how_many()

droid2 = Robot("R3-D3")
droid2.die()

print(Robot.__doc__)