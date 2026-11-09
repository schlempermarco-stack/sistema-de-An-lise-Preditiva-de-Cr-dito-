from fastapi import APIRouter, status, Response
from app.services.predictor import model_service

router = APIRouter(tags=["Monitoramento"])

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check(response: Response):
    """Endpoint de Monitoramento de Saúde Operacional (Fase 5)"""
    # Verifica se o modelo está carregado em memória RAM
    model_loaded = model_service.model is not None

    if model_loaded:
        return {
            "status": "healthy",
            "database_connection": "active",
            "ml_model_loaded_in_ram": True
        }
    else:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {
            "status": "unhealthy",
            "ml_model_loaded_in_ram": False
        }
