from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="API de Gestión de Estudiantes",
    description="API RESTful para registrar y consultar estudiantes",
    version="1.1.0"
)


class Student(BaseModel):
    nombre: str
    apellido: str
    correo: str


students = []
next_id = 1

@app.get("/")
def root():
    return {"mensaje": "API de Gestión de Estudiantes", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok", "version": app.version}


@app.post("/students", status_code=201)
def create_student(student: Student):
    global next_id

    new_student = {
        "id": next_id,
        "nombre": student.nombre,
        "apellido": student.apellido,
        "correo": student.correo
    }

    students.append(new_student)
    next_id += 1

    return new_student


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado"
    )
