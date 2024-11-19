class Sender:
    flag = True

    @classmethod
    def report(self):
        if self.flag:
            print("Greetings!")
            self.flag = False
        else:
            print("Get away!")


class Asker:
    @staticmethod
    def askall(lst):
        for el in lst:
            el.report()


s = [Sender(), Sender(), Sender()]
a = Asker()
a.askall(s)

