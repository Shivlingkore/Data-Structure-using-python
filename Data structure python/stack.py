class stack:
    def __init__(self):
        self.array = []
    
    def push(self,x):
       # x=int(input('Enter number'))
        self.array.append(x)

    def pop(self):
        self.array.pop()

    def tos(self):
        print(self.array[len(self.array)-1])

    def travrse(self):
        for i in self.array:
            print(i, end='  ')


s1 =stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

s1.travrse()
print("\n")

s1.pop()
s1.pop()
s1.travrse()
print("\n")
s1.tos()
print("\n")
