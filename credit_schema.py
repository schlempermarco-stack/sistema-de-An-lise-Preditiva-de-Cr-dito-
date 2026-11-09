from pydantic import BaseModel, Field

# Validação de Entrada Estrita (Fase 4)
class PredictionInput(BaseModel):
    idade: int = Field(..., ge=18, le=120, description="Idade do solicitante do crédito (mínimo 18 anos)")
    renda_anual: float = Field(..., gt=0, description="Renda anual do solicitante em formato numérico positivo")
    score_serasa: int = Field(..., ge=0, le=1000, description="Pontuação de score de crédito entre 0 e 1000")
    taxa_inadimplencia: float = Field(..., ge=0.0, le=1.0, description="Taxa histórica de inadimplência entre 0.0 e 1.0")

    model_config = {
        "json_schema_extra": {
            "example": {
                "idade": 35,
                "renda_anual": 65000.0,
                "score_serasa": 720,
                "taxa_inadimplencia": 0.12
            }
        }
    }

# Validação de Saída Estrita
class PredictionOutput(BaseModel):
    aprovado: int = Field(..., description="Resultado da inferência preditiva: 1 para Aprovado, 0 para Negado")
    probabilidade_aprovacao: float = Field(..., description="Percentual de confiança da decisão preditiva")
