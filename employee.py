# Employee class
class Employee:
    
    # Initalize with employee attributes
    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title
    
    # Get the employee name
    def get_name(self):
        return self.__name 
    
    # Get the employee id
    def get_id(self):
        return self.__id

    # Get the employee department    
    def get_department(self):
        return self.__department

    # Get employee job title    
    def get_job_title(self):
        return self.__job_title
    