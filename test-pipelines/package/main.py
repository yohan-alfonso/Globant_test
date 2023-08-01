from fastapi import FastAPI, Depends, HTTPException
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
#     return "Nuevo empleado" + str(request.employees.name) + " " + request.employees.id + " " \
#         + str(request.employees.datetime) + " " + request.employees.department_id + " " + request.employees.job_id

@app.post("/package/")
def post_employees(request: schemas.Empresa):
    return "Nuevo empleado: " + request.employees.name + " " + str(request.employees.id) + " " \
        + request.employees.datetime + " " + str(request.employees.department_id) + " " + str(request.employees.job_id)
