"""
Creado por : Yohan Alfonso Hernandez
Fecha:03-08-2023
Tema: Creación de schemas para ingesta de datos en base de datos con SQLalchemy y Fastapi
"""

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
    
    