from fastapi import FastAPI, Response, Request
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
import time

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

REQUEST_LATENCY = Histogram(
    "telecom_api_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path,
    ).observe(duration)

    return response


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
