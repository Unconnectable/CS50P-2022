
class Student:
    def __init__(self , name , house):
        self.name = name
        self.house = house
        #self.god = god
        #   
    def __str__(self):
        return f"{self.name} form {self.house}"
            
    @classmethod
    def get(cls):
         name = input("Nmme: ")
         house = input("house: ")
         return cls(name,house)
    #Getter
    @property 
    def house(self):
            return self._house
    @house.setter
    def house(self,house):
            if house not in ["China","American","Japan"]:
                raise ValueError("Invalid Error")
            self._house = house
    @property
    def name(self):
         return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("missing name")

    def gods(self):
        return "🤣"
        '''
        match self.god:
            case "1":
                return "😂" 
            case "2":
                return "🤣"
            case _ :
                return "😍"
        '''
def main():
    student= Student.get()
    '''
    tuple元组不支持改变
    if student[0] =="Alice":
        student[1] = "American"
    #This is how tuple print
    print(f"{student[0]} from {student[1]}")

    #This is how dic print
    print(f"{student['name']} form {student['house']}")

    '''
    #print(f"{student.name__} from {student.house__}")4
    #   student.house = "ERRORHOUSE"
    print(student)
    
'''
把get放到class里面
def get_studnet():
    name = input("Name: ")
    house = input("House: ")
    #god = input("God: ")
    
    THIS IS A TUPLE
    return (name,house)

    return [name,house]#This is a list 
    

    return  Student(name,house)
'''   


if __name__ == "__main__":
    main()