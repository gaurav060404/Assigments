class Employee:
    employee_count = 1000
    def __init__(self):
        self.employee_id = self.generate_emp_id() 
    def generate_emp_id(self):
        self.employee_count += 1
        return 'E' + str(self.employee_count)
    def get_emp_id(self):
        return self.employee_id

class Department:
    dep_project_list = []
    employee_dict = {}

    @staticmethod
    def add_project(project_list):
        if(len(project_list) < 5):
            self.dep_project_list.append(project_list)
        else:
            return -1
    
    @staticmethod
    def add_employee(self,employee,project_id):
        emp_id = employee.generate_emp_id()
        self.employee_dict[emp_id] = project_id
        Project.update_num_of_employees(self.employee)
    
class Project:
    def __init__(self,project_id,no_of_employees):
        self.project_id = project_id
        if(no_of_employees > 10):
            print("No. of employees should be atleast 10")
            return -2
        else:
            self.no_of_employees = no_of_employees
    
    def get_project_id(self):
        return self.project_id
    
    def get_num_of_employees(self,employee):
        return (employee.employee_count - 1000)

    def update_num_of_employees(self,employee):
        self.employee.employee_count += no_of_employees
    
emp = Employee()