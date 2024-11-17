"""适配器模式"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class WeiXinPayment(Payment):
    def pay(self, money):
        print("你正在使用微信支付...")
        print("你已经消费了{}元".format(money))
        print("*" * 30)


class AlipayPayment(Payment):
    def pay(self, money):
        print("你正在使用支付宝支付...")
        print("你已经消费了{}元".format(money))
        print("*" * 30)


class BankPayment:
    def cost(self, money):
        print("你正在使用银行卡支付...")
        print("你已经消费了{}元".format(money))
        print("*" * 30)


class YinLianPayment:
    def cost(self, money):
        print("你正在使用银联支付...")
        print("你已经消费了{}元".format(money))
        print("*" * 30)


# 1. 类适配(原理就是通多多继承的方式实现两个类的适配)
class BankPaymentAdapter(Payment, BankPayment):
    def pay(self, money):
        self.cost(money)


# 2. 对象适配器(通多组合的方式)
class CostPaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


def pay():
    p = WeiXinPayment()
    p.pay(100)

    p = AlipayPayment()
    p.pay(100)

    p = BankPaymentAdapter()  # 在类层面就已经实现了对另外一个类的适配
    p.pay(100)

    y = YinLianPayment()
    p = CostPaymentAdapter(y)  # 在类层面就已经实现了对另外一个类的适配
    p.pay(100)

    b = BankPayment()
    p = CostPaymentAdapter(b)  # 在类层面就已经实现了对另外一个类的适配
    p.pay(100)


if __name__ == '__main__':
    pay()
