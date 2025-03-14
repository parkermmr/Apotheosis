from contextlib import asynccontextmanager
import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from util.logging.logger import Logger
from app.metrics import setup_metrics
from app.routers.metrics import router as metrics_router
from app.routers.template import TemplateRouter

middleware_logger = Logger("app.middleware", level=20, colored=True)
error_logger = Logger("uvicorn.error", level=40, colored=True)


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for capturing request logs at varying levels
    based on status codes and for logging errors.
    """

    async def dispatch(self, request: Request, call_next):
        """
        Processes incoming requests, measures response times,
        and logs the outcome with the appropriate log level.
        """
        start_time = time.time()
        try:
            response = await call_next(request)
        except Exception as exc:
            error_logger.error(
                f"Error processing request {request.method} {request.url.path}: {exc}",
                extra={"caller": "LoggingMiddleware.dispatch"},
            )
            raise
        process_time_ms = (time.time() - start_time) * 1000
        client_host = request.client.host if request.client else "unknown"
        status_code = response.status_code
        log_msg = (
            f'{client_host} - "{request.method} {request.url.path}" '
            f"{status_code} - {process_time_ms:.2f}ms"
        )
        if status_code >= 500:
            middleware_logger.error(
                log_msg,
                extra={"caller": "LoggingMiddleware.dispatch"},
            )
        elif status_code >= 400:
            middleware_logger.warning(
                log_msg,
                extra={"caller": "LoggingMiddleware.dispatch"},
            )
        else:
            middleware_logger.info(
                log_msg,
                extra={"caller": "LoggingMiddleware.dispatch"},
            )
        return response


class Lifespan:
    """
    Manages application lifespan events.
    """

    def __init__(self):
        pass

    async def startup(self):
        """
        Executes startup routine.
        """
        middleware_logger.info(
            "Starting application lifespan.",
            extra={"caller": "lifespan"},
        )

    async def shutdown(self):
        """
        Executes shutdown routines.
        """
        middleware_logger.info(
            "Shutting down application lifespan.",
            extra={"caller": "lifespan"},
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the application lifespan events. Logs startup
    and shutdown, and gracefully shuts down the app.
    """
    app.state.lifespan = Lifespan()
    try:
        await app.state.lifespan.startup()
        yield
    finally:
        await app.state.lifespan.shutdown()


class App(FastAPI):
    """
    Custom FastAPI application that includes a lifespan context manager,
    CORS middleware, logging middleware, static files, default routers,
    and metrics setup.
    """
    _initialized_once = False

    def __init__(self) -> None:
        """
        Initializes the FastAPI app, sets up middleware, mounts static files,
        includes routers, and logs a single initialization message.
        """
        super().__init__(
            title="FastAPI Advanced Template",
            docs_url=None,
            redoc_url=None,
            openapi_url="/openapi.json",
            lifespan=lifespan,
        )
        self.add_middleware(
            CORSMiddleware,
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
        if not App._initialized_once:
            App._initialized_once = True
            middleware_logger.info(
                "Application initialized.",
                extra={"caller": "App.__init__"},
            )
