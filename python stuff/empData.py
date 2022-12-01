import random
data = []
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

def viewEmployeeData():
   print("\n")
   j = 0
   for i in range(len(data)):
      print(f"{data[j]}")
      j += 1

while True:
   function = input("Please enter a function name: ")
   if function == 'addEmployee':
      addEmployee()
   elif function == 'viewEmployeeData':
      viewEmployeeData()