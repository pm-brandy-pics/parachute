class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
e1=Employee(1,'Gojo Satoru',700000)
e2=Employee(2,'Toji Fushiguro',80000)
print('Displaying employee with the highest salary')
if e1.salary>e2.salary:
    print(e1.name,'has a higher salary at',e2.salary)
else:
        print(e2.name,'has a higher salary at',e1.salary)

