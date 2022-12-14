import random
data = []
idList = []
#Employee Database (empData) a quick way to add employees to a memory and view
#employees using designated IDs that the program automatically gives by random
class Employee:
   def __init__(self, name, job, id, data):
      self.name = name
      self.job = job
      self.id = random.randint(100000, 999999)
      self.data = "sample"

   def describeEmployee(self):
      self.data = f"Name: {self.name} |  Job: {self.job} | ID: {self.id}"
      print(self.data)


def addEmployee():
   name = input("Enter the name: ")
   job = input("Please enter the job: ")
   newEmployee = Employee(name, job, str(random.randint(100000, 999999)), "sample")
   newEmployee.describeEmployee()
   data.append(newEmployee.data)
   idList.append(newEmployee.id)

def viewAll():
   l = 0
   for i in range(len(data)):
      print(f"{data[l]}")
      l += 1
   l = 0

def findEmployee():
   findID = input("Please enter the employee ID: ")
   j = 0
   for m in range(len(idList)):
      if findID == idList[j]:
         print(data[j])
         break
      else:
         j += 1
   j = 0
      

while True:
   function = input("Please enter a function name: ")
   if function == 'addEmployee':
      addEmployee()
   elif function == 'viewAll':
      viewAll()
   elif function == 'findEmployee':
      findEmployee()