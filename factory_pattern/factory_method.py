"""工厂方法模式"""

from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AlyPay(Payment):
    def __init__(self, hua_bei=False, ka=False):
        self.is_hua_bei = hua_bei
        self.is_ka = ka

    def pay(self, money):
        if self.is_hua_bei:
            print("正在使用花呗支付，支付了%d"%money)
        if self.is_ka:
            print("正在使用银行卡支付，支付了%d"%money)
        else:
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

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self, method=""):
        pass

class AlypayFactory(PaymentFactory):
    def create_payment(self, method=""):
        if method == "":
            return AlyPay()
        elif method == "KA":
            return AlyPay(ka=True)
        elif method == "HB":
            return AlyPay(hua_bei=True)
        else:
            raise TypeError("支付方式出错！")


class WeiXinFactory(PaymentFactory):
    def create_payment(self, method=""):
        if method == "":
            return WeiXinPay()
        elif method == "KA":
            return WeiXinPay(ka=True)
        else:
            raise TypeError("支付方式出错！")

class YinLianFactory(PaymentFactory):
    def create_payment(self, method=""):
        return YinLianPay()


if __name__ == "__main__":
    f = WeiXinFactory()
    p = f.create_payment()
    p.pay(100)

    p = f.create_payment("KA")
    p.pay(100)

    f = AlypayFactory()
    p = f.create_payment()
    p.pay(100)

    f = AlypayFactory()
    p = f.create_payment("KA")
    p.pay(100)

    f = AlypayFactory()
    p = f.create_payment("HB")
    p.pay(100)


    f = YinLianFactory()
    p = f.create_payment()
    p.pay(100)

