import sys
from pathlib import Path

from fastapi import FastAPI

# Ensure the project root is importable when this file is loaded as `main`
# from inside dbAPI, as well as when loaded as `dbAPI.main` from the root.
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dbAPI.routers.patients import router as patients_router

app = FastAPI(title="Patient API")
app.include_router(patients_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Patient API is running"}
