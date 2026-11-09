# 💳 API de Análise Preditiva de Risco de Crédito

## 📝 Descrição do Projeto
Este projeto consiste em um pipeline completo de Machine Learning pronto para produção. O objetivo do sistema é analisar o perfil financeiro e pessoal de solicitantes de crédito para prever se a proposta de crédito deve ser aprovada ou negada sob critérios estritos de modelagem matemática.

## 🔍 Origem do Modelo
O modelo preditivo foi desenvolvido utilizando um pipeline próprio de Machine Learning com base em dados simulados de crédito (comportamento de Score Serasa, Renda Anual, Idade e Taxa de Inadimplência prévia), garantindo o tratamento correto das variáveis e uma validação robusta por meio de métricas como F1-Score e ROC-AUC.

## 🛠️ Tecnologias Utilizadas
- **FastAPI**: Criação de endpoints assíncronos de alta performance.
- **Pydantic**: Validação de dados estrita de entrada e saída.
- **Scikit-Learn**: Treinamento do modelo RandomForestClassifier.
- **Uvicorn**: Servidor de aplicação ASGI.
- **Joblib**: Serialização e persistência do modelo.

---

## 🚀 Instruções de Instalação e Execução

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Criar Ambiente Virtual (venv)
python -m venv venv

# No Windows:
.\venv\Scripts\activate

# No Linux/macOS:
source venv/bin/activate
3. Instalar Dependências
pip install -r requirements.txt
4. Executar a API
uvicorn app.main:app --reload
Acesse o serviço em: http://127.0.0.1:8000

📖 Documentação da API (Swagger)
Com a API em execução, acesse a documentação interativa automatizada em:

Swagger UI: http://127.0.0.1:8000/docs
Endpoints Disponíveis:
1. GET /health
Verifica se a API e o modelo carregado em memória RAM estão operacionais.

Resposta de Sucesso (200 OK):
{
  "status": "healthy",
  "database_connection": "active",
  "ml_model_loaded_in_ram": true
}
2. POST /v1/predict
Executa a inferência de risco de crédito com base nas características enviadas.

Exemplo de Payload de Entrada:
{
  "idade": 35,
  "renda_anual": 65000.0,
  "score_serasa": 720,
  "taxa_inadimplencia": 0.12
}
Resposta Retornada (200 OK):
{
  "aprovado": 1,
  "probabilidade_aprovacao": 0.98
}
Erros de Validação (422 Unprocessable Entity): Retornado automaticamente se valores inválidos forem enviados (ex: idade menor que 18 anos ou score maior que 1000).
