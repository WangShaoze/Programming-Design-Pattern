from abc import ABCMeta, abstractmethod


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "{}, {}, {}, {}".format(self.face, self.body, self.arm, self.leg)



class PlayerBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

class Beauty(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "可爱的脸蛋"

    def build_body(self):
        self.player.body = "性感的身材"

    def build_arm(self):
        self.player.arm = "纤细的手臂"

    def build_leg(self):
        self.player.leg = "大长腿"


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "丑陋的脸蛋"

    def build_body(self):
        self.player.body = "巨大"

    def build_arm(self):
        self.player.arm = "粗壮的手臂"

    def build_leg(self):
        self.player.leg = "一瘸一拐的腿"

class PlayerDirector:       # 控制玩家的组装顺序
    def build_player(self, builder:PlayerBuilder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


if __name__ == "__main__":
    # client
    builder = Beauty()
    directer = PlayerDirector()
    p = directer.build_player(builder)
    print(p)

    builder = Monster()
    directer = PlayerDirector()
    p = directer.build_player(builder)
    print(p)



