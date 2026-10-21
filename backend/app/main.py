from fastapi import FastAPI

app = FastAPI(title="Appt App API", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Welcome to Appt App API"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
