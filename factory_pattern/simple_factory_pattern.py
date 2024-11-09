"""简单工程模式"""

from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AlyPay(Payment):
    def pay(self, money):
        print("正在使用支付宝支付，支付了%d"%money)

class BankPay(Payment):
    def pay(self, money):
        print("正在使用银行卡支付，支付了%d"%money)

class YinLianPay(Payment):
    def pay(self, money):
        print("正在使用银联支付，支付了%d"%money)

class WeiXinPay(Payment):
    def __init__(self, ka=False):
        self.ka = ka

    def pay(self, money):
        if self.ka:
            print("正在使用银行卡支付，支付了%d"%money)
        else:
            print("正在使用微信余额支付，支付了%d"%money)

class PaymentFactory:
    def create_payment(self, pay_method):
        if pay_method == "Alipay":
            return AlyPay()
        elif pay_method == "Bank":
            return BankPay()
        elif pay_method == "YinLian":
            return YinLianPay()
        elif pay_method == "WeiXin":
            return WeiXinPay()
        elif pay_method == "Ka":
            return WeiXinPay(ka=True)
        else:
            raise TypeError("支付方式错误！")

if __name__ == "__main__":
    pf = PaymentFactory()
    p = pf.create_payment("WeiXin")
    p.pay(230)
    p = pf.create_payment("YinLian")
    p.pay(120)
    p = pf.create_payment("Ka")
    p.pay(120)
