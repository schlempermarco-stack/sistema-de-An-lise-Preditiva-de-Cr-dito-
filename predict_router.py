from fastapi import APIRouter, HTTPException, status
from app.schemas.credit_schema import PredictionInput, PredictionOutput
from app.services.predictor import model_service

router = APIRouter(prefix="/v1", tags=["Predição"])

@router.post("/predict", response_model=PredictionOutput, status_code=status.HTTP_200_OK)
async def execute_prediction(payload: PredictionInput):
    """Endpoint de Inferência Estrita (Fase 5)"""
    try:
        input_dict = payload.model_dump()
        result = model_service.predict(input_dict)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno durante o processamento da predição: {str(e)}"
        )
