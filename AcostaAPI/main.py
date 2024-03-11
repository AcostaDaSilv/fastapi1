from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from fastapi import APIRouter, Response, status
from ..config.db import conn
from ..models.user import users
from ..schemas.user import Data
from starlette.status import HTTP_204_NO_CONTENT

data = APIRouter()


@app.post("/empleados/")
async def crear_empleado(empleado: Data):
    query = "INSERT INTO empleados (id,nombre, apellido, edad, cargo, salario) VALUES (%s,%s, %s, %s, %s, %s)"
    valores = (empleado.id,empleado.nombre, empleado.apellido, empleado.edad, empleado.cargo, empleado.salario)
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Empleado creado exitosamente"}

@app.get("/empleados/{id_empleado}")
async def obtener_empleado(id_empleado: int):
    query = "SELECT * FROM empleados WHERE id = %s"
    cursor.execute(query, (id_empleado,))
    empleado = cursor.fetchone()
    if empleado:
        return {"id": empleado[0], "nombre": empleado[1], "apellido": empleado[2], "edad": empleado[3], "cargo": empleado[4], "salario": empleado[5]}
    else:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

@app.put("/empleados/{id_empleado}")
async def actualizar_empleado(id_empleado: int, empleado: Empleado):
    query = "UPDATE empleados SET id = %s,nombre = %s, apellido = %s, edad = %s, cargo = %s, salario = %s WHERE id = %s"
    valores = (empleado.id,empleado.nombre, empleado.apellido, empleado.edad, empleado.cargo, empleado.salario, id_empleado)
    cursor.execute(query, valores)
    mysql_conn.commit()
    return {"mensaje": "Detalles del empleado actualizados exitosamente"}

@app.delete("/empleados/{id_empleado}")
async def eliminar_empleado(id_empleado: int):
    query = "DELETE FROM empleados WHERE id = %s"
    cursor.execute(query, (id_empleado,))
    mysql_conn.commit()
    return {"mensaje": "Empleado eliminado exitosamente"}
