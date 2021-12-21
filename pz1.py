class Prug:
    m = []
    n = []

    def __init__(self, a, b):
        self.a = a; type(self).m.append(self.a)
        self.b = b; type(self).n.append(self.b)

    def plochad(self):
       return self.a* self.b

    @classmethod
    def total(cls):
        all = []
        k = len(cls.m)
        for i in range(0, k):
            all.append(cls.m[i]*cls.n[i])
        return all


class Kvadr(Prug):
    def __init__(self, c):
        super().__init__(c,c)




A1, A2, A3, B1, B2, = Prug(3,4), Prug(5,4), Prug(9,4),Kvadr(2), Kvadr(5)
print(Kvadr.total())

#B1, B2, = Kvadr(2), Kvadr(5)
#print(Kvadr.total())
