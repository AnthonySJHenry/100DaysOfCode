class Person:
    __count = 0
    def __init__(this, age=0, name = ""):
        Person.__count += 1
        this._IDnum = Person.__count
        this._name = name
        this._age = age
    
    @classmethod
    def getCount(cl):
        return cl.__count
    
        
    def __str__(this):
        if this.name:
            return "Name: " + str(this.name) + "\nID: " + str(this.IDnum)
        else:
            return "Error: No name; Please set name for user."
#----------------------------------PROPERTIES-----------------------------  
    #------------------------------name----------------------------------
    @property
    def name(this):
        return this._name
    
    @name.setter
    def name(this, name):
        if name:
            print(f"Name changed to {name}")
            this._name = name
        else: print("Error: User needs characters for name!")
    
    #--------------------------------IDnum--------------------------------
    @property
    def IDnum(this):
        return f"{this._name}'s ID#: {this._IDnum}"
    
    #--------------------------------age--------------------------
    @property
    def age(this):
        return this._age
    
    @age.setter
    def age(this, age):
        this._age = age

#---------------------------------------MAIN-----------------------------
if __name__ == '__main__':
    person1 = Person(26)
    person1.name = "Anthony"
    print(person1.IDnum)
    
    person2 = Person(26, "John")
#   person2.IDnum = 0 <-- Line will not work. One cannot change the ID#
    print(person2.IDnum)
    

    
    
    
