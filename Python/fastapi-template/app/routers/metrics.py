from fastapi import APIRouter


class MetricsRouter:
    """
    Class-based router for all metrics-related endpoints, including
    health checks and version info. Prefixed with /metrics.
    """
    def __init__(self) -> None:
        self.router = APIRouter(prefix="/metrics", tags=["metrics"])
        self.router.add_api_route("/health",
                                  self.health,
                                  methods=["GET"],
                                  response_model=dict)
        self.router.add_api_route("/version",
                                  self.version,
                                  methods=["GET"],
                                  response_model=dict)

    async def health(self) -> dict:
        """
        Return a simple health status. Could be expanded to check DB, cache, etc.
        """
        return {"status": "ok"}

    async def version(self) -> dict:
        """
        Return service version or build metadata.
        """
        return {"version": "1.0.0"}


router = MetricsRouter().router
