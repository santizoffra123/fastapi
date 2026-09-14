from fastapi import FastAPI, Depends
from pydantic import BaseModel
from conexion import getConexion, initDb
import sqlite3


class Estudiante(BaseModel):
    nombre: str
    apellido: str


app = FastAPI()


@app.on_event("startup")
def startup():
    initDb()


@app.get("/")
def root():
    return "hola si, un fort?"


@app.post("/agregar_estudiante")
def agregar_estudiante(
    estudiante: Estudiante,
    conexion: sqlite3.Connection = Depends(getConexion)
):
    conexion.execute(
        "INSERT INTO estudiantes (nombre, apellido) VALUES (?, ?)",
        (estudiante.nombre, estudiante.apellido)
    )

    conexion.commit()
    conexion.close()

    return "estudiante agregado"


@app.get("/obtener_estudiante")
def leer_estudiantes():
    conexion = getConexion()

    res = conexion.execute(
        "SELECT * FROM estudiantes"
    ).fetchall()

    conexion.close()

    return [dict(item) for item in res]


@app.delete("/borrar_estudiante/{id}")
def eliminar_estudiante(id: int):
    conexion = getConexion()

    conexion.execute(
        "DELETE FROM estudiantes WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()

    return "estudiante eliminado"