from fastapi import FastAPI

app = FastAPI(
    title="Telecom Cloud Platform",
    description="Cloud-native telecom operations platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "Telecom Cloud Platform",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }
