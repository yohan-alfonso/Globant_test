from pydantic import BaseModel

class Employees(BaseModel):
    id: int
    name: str
    datetime:str
    department_id: int
    job_id : int
    
class Departments(BaseModel):
    id : int
    department : str
    

class Jobs(BaseModel):
    id : int
    job : str
    
class Empresa(BaseModel):
    employees: Employees
    departments : Departments
    jobs : Jobs
    
    