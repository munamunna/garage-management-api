from fastapi import FastAPI

app = FastAPI(title="Garage Management API")


@app.get("/")
def root():
    return {"message": "Garage Management API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}