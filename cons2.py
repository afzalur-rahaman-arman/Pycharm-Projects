class person:
    def __init__(self,name,roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        sum=0;
        for i in self.marks:
            sum=sum+i

        print("Hi,",self.name,". Your Roll: ",self.roll, ". Your avg mark:",sum/3)

p1=person("Afzalur Rahaman", 101766, [60,75,80])
p2=person("Afzal", 101756, [68,75,80])