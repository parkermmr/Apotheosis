from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator


def setup_metrics(app: FastAPI) -> None:
    """
    Instruments the FastAPI application for Prometheus metrics,
    exposed at /internal/metrics
    """
    Instrumentator().instrument(app).expose(app, endpoint="/internal/metrics")
