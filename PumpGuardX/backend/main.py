import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import logging

from wallet_analyzer import WalletAnalyzer
from volume_analyzer import VolumeAnalyzer
from contract_scanner import ContractScanner
from ai_engine import AIEngine
from scoring import TrustScoreCalculator
from data_fetcher import OnChainDataFetcher

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PumpGuardX-API")

app = FastAPI(
    title="PumpGuardX API",
    description="AI-powered analysis engine for detecting manipulated token launches on Pump.fun",
    version="0.1.0-alpha"
)

# Initialize modules
fetcher = OnChainDataFetcher()
wallet_analyzer = WalletAnalyzer()
volume_analyzer = VolumeAnalyzer()
contract_scanner = ContractScanner()
ai_engine = AIEngine()
scorer = TrustScoreCalculator()

class AnalysisRequest(BaseModel):
    token_address: str
    network: str = "solana" # Default to Solana for Pump.fun
    include_market_depth: bool = True

class AnalysisResponse(BaseModel):
    token_address: str
    trust_score: float
    verdict: str
    risk_level: str
    analysis: Dict[str, Any]
    ai_insights: str

@app.get("/")
async def health_check():
    return {"status": "online", "system": "PumpGuardX Analysis Engine", "version": "0.1.0"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_token(request: AnalysisRequest):
    """
    Orchestrate the full analysis pipeline for a given token address.
    """
    logger.info(f"Starting analysis for token: {request.token_address}")
    
    try:
        # 1. Fetch raw on-chain data
        data = await fetcher.get_token_data(request.token_address)
        if not data:
            raise HTTPException(status_code=404, detail="Token data not found on-chain")
        
        # 2. Parallel Analysis Execution
        # In a production env, these would use asyncio.gather for true concurrency
        wallet_metrics = wallet_analyzer.full_analysis(data['holders'], data['transactions'])
        volume_metrics = volume_analyzer.analyze_volume(data['volume_history'], data['liquidity'])
        contract_safety = contract_scanner.scan(data['contract_code'], data['deployer'])
        
        # 3. AI Verdict Generation
        combined_features = {
            **wallet_metrics,
            **volume_metrics,
            **contract_safety
        }
        
        ai_result = ai_engine.generate_verdict(combined_features)
        
        # 4. Final Scoring
        final_score = scorer.calculate_score(combined_features, ai_result['confidence'])
        
        # 5. Classify Risk
        risk_level = scorer.classify_risk(final_score)
        
        return AnalysisResponse(
            token_address=request.token_address,
            trust_score=final_score,
            verdict=ai_result['verdict'],
            risk_level=risk_level,
            analysis={
                "wallet_clustering": wallet_metrics,
                "volume_integrity": volume_metrics,
                "contract_security": contract_safety
            },
            ai_insights=ai_result['explanation']
        )

    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
