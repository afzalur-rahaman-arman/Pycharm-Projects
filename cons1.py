class person:
    Name="Afzal"
    print(Name)
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("This is self: ", self)
        print(name)
        print(age)

p1=person("Rahaman", 26)
p1.name="Rahaman2"
p1.age=30
print(p1.name)