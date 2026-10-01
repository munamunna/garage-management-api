from fastapi import FastAPI

app = FastAPI(title="Garage Management API")


@app.get("/")
def root():
    return {"message": "Garage Management API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/customers")
def get_customers():
    return [
        {
            "id": 1,
            "name": "Ahmed",
            "email": "ahmed@example.com"
        },
        {
            "id": 2,
            "name": "Rahul",
            "email": "rahul@example.com"
        }
    ]