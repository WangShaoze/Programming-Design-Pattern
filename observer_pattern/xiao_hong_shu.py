"""
观察者模式 -----> 发布订阅模式
"""
from abc import ABCMeta, abstractmethod
from typing import List


class Observer(metaclass=ABCMeta):  # 抽象观察者
    @abstractmethod
    def update(self, notice):
        pass


class Notice:
    def __init__(self):
        self.observers: List[Observer] = []  # 所有加入到通知群

    def follow(self, obs):
        self.observers.append(obs)  # 点关注

    def unfollow(self, obs):
        self.observers.remove(obs)  # 点取关

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class Role(Observer, Notice):
    def __init__(self):
        super().__init__()
        self.__info = None

    def create_note(self, msg):
        self.__info = msg
        self.notify()

    def update(self, role):
        self.__info = role.get_message()

    def get_message(self):
        return self.__info


if __name__ == "__main__":
    f1 = Role()
    f2 = Role()
    f3 = Role()

    bo_zhu = Role()
    bo_zhu.follow(f1)
    bo_zhu.follow(f2)

    bo_zhu.create_note("这是我发布的第一个作品")

    print(f1.get_message())
    print(f2.get_message())
    print(f3.get_message())

    bo_zhu.unfollow(f1)
    bo_zhu.follow(f2)
    bo_zhu.follow(f3)
    bo_zhu.create_note("这是我发布的第二个作品")

    print(f1.get_message())
    print(f2.get_message())
    print(f3.get_message())
