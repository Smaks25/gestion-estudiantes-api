# API de Gestión de Estudiantes

API RESTful hecha con **FastAPI** para registrar y consultar estudiantes. Incluye pruebas automáticas, contenedor Docker y un pipeline de CI en AWS CodeBuild.

## Tecnologías

- Python 3.12
- FastAPI + Uvicorn
- Pydantic
- Pytest
- Docker
- AWS CodeBuild (CI)

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Mensaje de bienvenida y enlace a la documentación |
| GET | `/health` | Estado del servicio y versión |
| POST | `/students` | Crea un estudiante (devuelve 201) |
| GET | `/students` | Lista todos los estudiantes |
| GET | `/students/{student_id}` | Consulta un estudiante por id (404 si no existe) |

Ejemplo de cuerpo para `POST /students`:

```json
{
  "nombre": "Ana",
  "apellido": "Pérez",
  "correo": "ana@example.com"
}
```

La documentación interactiva (Swagger) está disponible en `/docs`.

## Cómo correrla en local

```bash
git clone https://github.com/Smaks25/gestion-estudiantes-api.git
cd gestion-estudiantes-api
python -m venv venv
venv\Scripts\activate        # En Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Luego abre http://localhost:8000/docs

## Con Docker

```bash
docker build -t gestion-estudiantes-api .
docker run -p 8000:8000 gestion-estudiantes-api
```

## Pruebas

```bash
pip install pytest httpx
python -m pytest -v
```

## Integración continua

El archivo `buildspec.yml` define el pipeline de AWS CodeBuild: instala dependencias, ejecuta las pruebas y empaqueta los artefactos.

## Limitaciones conocidas

Los estudiantes se guardan en memoria, así que se pierden al reiniciar el servicio.

## Próximos pasos

- Agregar base de datos (por ejemplo PostgreSQL o DynamoDB)
- Validar el formato del correo
- Agregar endpoints para actualizar y eliminar estudiantes

## Autor

Santiago Cogollo Peña · [LinkedIn](www.linkedin.com/in/santiago-cogollo-96196a260)