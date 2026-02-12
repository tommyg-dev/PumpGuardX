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
logger = logging.getLogger("LUMI-Agent")

app = FastAPI(
    title="LUMI Agent API",
    description="The technical interface for the Lunaria Protocol, guiding users through the DeFi topography.",
    version="1.0.0-LUMI"
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
    # LUMI is active and guarding the protocol
    return {"status": "online", "system": "LUMI Agent Analysis Core", "version": "1.0.0"}

@app.get("/version")
async def get_version():
    return {
        "engine": "LUMI Analysis Core",
        "protocol": "Lunaria Protocol",
        "version": "1.0.0-LUMI",
        "directives": ["Optimize", "Guide", "Protect"],
        "supported_networks": ["solana"]
    }

@app.get("/status/detail")
async def get_detailed_status():
    """
    Returns detailed operational status of all analysis modules.
    """
    return {
        "status": "operational",
        "modules": {
            "wallet_analyzer": "active",
            "volume_analyzer": "active",
            "contract_scanner": "active",
            "ai_engine": "active"
        },
        "uptime": "stable"
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_token(request: AnalysisRequest):
    """
    Orchestrate the Lunaria Protocol analysis pipeline. 
    LUMI interprets raw signals and converts them into human-readable trust metrics.
    """
    logger.info(f"LUMI is starting analysis for token: {request.token_address}")
    
    try:
        # 1. Fetch raw on-chain data
        data = await fetcher.get_token_data(request.token_address)
        if not data:
            raise HTTPException(status_code=404, detail="Token data not found on-chain")
        
        # 2. Parallel Signal Interpretation
        # LUMI interprets raw blockchain signals through specialized analytical layers
        wallet_metrics = wallet_analyzer.full_analysis(data['holders'], data['transactions']) # Wallet Pattern Interpreter
        volume_metrics = volume_analyzer.analyze_volume(data['volume_history'], data['liquidity']) # Volume Authenticity Engine
        contract_safety = contract_scanner.scan(data['contract_code'], data['deployer']) # Bytecode Risk Scanner
        
        # 3. LUMI Analysis Core Verdict
        combined_features = {
            **wallet_metrics,
            **volume_metrics,
            **contract_safety
        }
        
        ai_result = ai_engine.generate_verdict(combined_features)
        
        # 4. Trust Signal Generation
        final_score = scorer.calculate_score(combined_features, ai_result['confidence'])
        
        # 5. Classify Risk
        risk_level = scorer.classify_risk(final_score)
        
        return AnalysisResponse(
            token_address=request.token_address,
            trust_score=final_score,
            verdict=ai_result['verdict'],
            risk_level=risk_level,
            analysis={
                "wallet_pattern_interpreter": wallet_metrics,
                "volume_authenticity": volume_metrics,
                "bytecode_risk_scanner": contract_safety
            },
            ai_insights=ai_result['explanation']
        )

    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
