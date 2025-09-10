class emp:
    def __init__(self, n, s): self.n, self.s = n, s
    def inc(self, p): self.s += self.s * p / 100
    def pr(self): print(f"emp: {self.n} salary: {self.s}")

e = emp(input("Enter employee name: "), float(input("Enter employee salary: ")))
e.inc(float(input("Enter increment percentage: ")))
e.pr()

