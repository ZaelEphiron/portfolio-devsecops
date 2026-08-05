from fastapi import FastAPI

app = FastAPI(
    title="Portfolio DevSecOps API",
    version="0.1.0",
    description="API minimaliste pour démonstration DevSecOps"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
