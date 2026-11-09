import joblib
import numpy as np
from typing import Dict, Any

class ModelService:
    def __init__(self):
        self.model = None

    def load_model(self, model_path: str):
        """Carrega o modelo uma única vez na memória (Fase 3)"""
        self.model = joblib.load(model_path)

    def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executa a inferência preditiva desacoplada de regras HTTP (Fase 2)"""
        if self.model is None:
            raise RuntimeError("O modelo preditivo não foi carregado corretamente na memória RAM.")

        # Converter dados de entrada para formato de matriz numpy bidimensional
        features = np.array([[
            input_data["idade"],
            input_data["renda_anual"],
            input_data["score_serasa"],
            input_data["taxa_inadimplencia"]
        ]])

        predicao = int(self.model.predict(features)[0])
        probabilidades = self.model.predict_proba(features)[0]
        probabilidade_final = float(probabilidades[1]) if predicao == 1 else float(probabilidades[0])

        return {
            "aprovado": predicao,
            "probabilidade_aprovacao": probabilidade_final
        }

# Instanciação global que será gerenciada no lifespan da API
model_service = ModelService()
