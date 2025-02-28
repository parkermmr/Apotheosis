import time
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.logging_config import setup_logging
from app.metrics import setup_metrics
from app.routers.metrics import router as metrics_router
from app.routers.template import TemplateRouter

setup_logging()

info_logger = logging.getLogger("uvicorn.info")
info_logger.setLevel(logging.INFO)
debug_logger = logging.getLogger("uvicorn.error")
debug_logger.setLevel(logging.DEBUG)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time_ms = (time.time() - start_time) * 1000
        client_host = request.client.host if request.client else "unknown"
        info_logger.info(
            f'{client_host} - "{request.method} {request.url.path}" '
            f'{response.status_code} - {process_time_ms:.2f}ms'
        )
        return response


@asynccontextmanager
async def lifespan(app: FastAPI):
    info_logger.info("Starting application lifespan.")
    yield
    info_logger.info("Shutting down application lifespan.")


class App(FastAPI):
    def __init__(self) -> None:
        super().__init__(
            title="FastAPI Advanced Template",
            docs_url=None,
            redoc_url=None,
            openapi_url="/openapi.json",
            lifespan=lifespan
        )
        self.add_middleware(CORSMiddleware,
                            allow_origins=["*"],
                            allow_credentials=True,
                            allow_methods=["*"],
                            allow_headers=["*"],
                            )
        self.add_middleware(LoggingMiddleware)
        self.mount("/static", StaticFiles(directory="static"), name="static")
        self.include_router(metrics_router)
        self.include_router(TemplateRouter().router)
        setup_metrics(self)
        info_logger.info("Application initialized.")
