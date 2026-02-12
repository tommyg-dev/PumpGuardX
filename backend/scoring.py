from typing import Dict, Any

class TrustScoreCalculator:
    def __init__(self):
        self.base_score = 100

    def calculate_score(self, features: Dict[str, Any], ai_confidence: float) -> float:
        """
        LUMI synthesizes all quantitative metrics and AI confidence into a final 
        0-100 Trust Score.
        """
        score = self.base_score
        
        # 1. Wallet Penalties
        # Every 1% of top holder concentration above 20% drops score by 1 point
        if features.get('top_10_holding_pct', 0) > 20:
            penalty = (features['top_10_holding_pct'] - 20) * 1.5
            score -= penalty
            
        # Fresh wallet penalty
        if features.get('fresh_wallet_percentage', 0) > 30:
            score -= (features['fresh_wallet_percentage'] - 30) * 0.8
            
        # 2. Volume Penalties
        if not features.get('is_organic', True):
            score -= 40
            
        # 3. Contract Penalties
        score -= features.get('risk_score', 0)

        # 4. Weighting by AI Confidence
        # If AI is uncertain, we pull the score toward neutral (50)
        final_score = (score * ai_confidence) + (50 * (1 - ai_confidence))
        
        return max(0, min(100, round(final_score, 1)))

    def classify_risk(self, score: float) -> str:
        """ Map numerical score to Lunaria Protocol risk tiers. """
        if score > 80:
            return "SECURE"
        elif score > 50:
            return "NEUTRAL"
        elif score > 30:
            return "CAUTION"
        else:
            return "DANGER"
