from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(
    title="Telecom Cloud Platform",
    description="Cloud-native telecom operations platform",
    version="0.1.0",
)

REQUEST_COUNT = Counter(
    "telecom_api_requests_total",
    "Total number of API requests",
    ["method", "endpoint"],
)


@app.get("/")
def root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

    return {
        "service": "Telecom Cloud Platform",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health").inc()

    return {
        "status": "healthy",
    }


@app.get("/ready")
def ready():
    REQUEST_COUNT.labels(method="GET", endpoint="/ready").inc()

    return {
        "status": "ready",
    }


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
