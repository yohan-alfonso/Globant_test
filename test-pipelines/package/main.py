"""
Creado por : Yohan Alfonso Hernandez
Fecha:03-08-2023
Tema: ingesta de datos en base de datos con SQLalchemy y Fastapi
"""

from fastapi import FastAPI, Depends, HTTPException
from package import tablas_e_inserta_data_historica
from package import schemas

# Rest of the code remains the same
app = FastAPI()

@app.get("/") # el "/" es el home
def  get_root(): # hacer una peticion de get para retorno de información
    return" este el api de test globant" # para ejecutr esta parte se necesita uvicorn

    """
    desde el home: uvicorn  books-api.main:app --reload
    en la salida entrega el servidor http://127.0.0.1:8000
    http://127.0.0.1:8000/docs para ver la documentación de la api se agrega /docs en el browser
    
    """
    
# @app.post("/package/")
# def post_employees(request: schemas.Empresa):
#     return "Nuevo empleado" + str(request.employees.name) + " " + str(request.employees.id) + " " \
#         + str(request.employees.datetime) + " " + str(request.employees.department_id) + " " + str(request.employees.job_id)

@app.post("/package/")
def post_employees(request: schemas.Empresa):
    tablas_e_inserta_data_historica.add_employees(
        convert_into_employee_db_model(request.employees),
        convert_into_department_db_model(request.departments),
        convert_into_job_db_model(request.jobs)
    )
    return "Nuevo empleado" + str(request.employees.name) + " " + str(request.employees.id) + " " \
         + str(request.employees.datetime) + " " + str(request.employees.department_id) + " " + str(request.employees.job_id)

   
def convert_into_employee_db_model(employees: schemas.Employees):
    return tablas_e_inserta_data_historica.Employees(id=employees.id,name=employees.name, datetime= employees.datetime,department_id=employees.department_id,job_id=employees.job_id)


def convert_into_department_db_model(departments: schemas.Departments):
    return tablas_e_inserta_data_historica.Departments(id=departments.id,department=departments.department)

def convert_into_job_db_model(jobs: schemas.Jobs):
    return tablas_e_inserta_data_historica.Jobs(id= jobs.id, job=jobs.job)


