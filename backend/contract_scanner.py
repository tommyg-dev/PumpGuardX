from typing import Dict, List, Any
import re

class ContractScanner:
    def __init__(self):
        # Patterns for common malicious functions in Solidity/Rust (Anchor)
        self.risk_patterns = {
            "blacklist": r"(blacklist|block_user|freeze_account)",
            "mint_authority": r"(mint_to|mint\s*\{)",
            "fake_renounce": r"(renounce_ownership\s*\{.*\/\/.*fake)", # Conceptual regex
            "high_tax": r"(fee\s*=\s*[2-9][0-9])" # Fees > 20%
        }

    def scan(self, bytecode: str, deployer_address: str) -> Dict[str, Any]:
        """
        Performs static analysis on the contract code/bytecode to identify risks.
        """
        findings = []
        risk_score = 0
        
        if not bytecode:
            return {"risk_score": 100, "findings": ["No bytecode verified"]}
            
        # 1. Check for Mint Authority (Infinite Mint risk)
        if self._check_pattern(bytecode, "mint_authority"):
            findings.append("Mint authority detected (Inflation risk)")
            risk_score += 30
            
        # 2. Check for Blacklist Capability (Honeypot risk)
        if self._check_pattern(bytecode, "blacklist"):
            findings.append("Blacklist function detected (Censorship risk)")
            risk_score += 40
            
        # 3. Check for Renounced Ownership
        # In Sol: owner() == address(0)
        renounced = self._verify_renouncement(bytecode)
        if not renounced:
            findings.append("Ownership not renounced")
            risk_score += 10
            
        return {
            "risk_score": min(risk_score, 100),
            "is_verified": True,
            "findings": findings,
            "can_mint": "Mint authority detected" in findings,
            "can_freeze": "Blacklist function detected" in findings
        }

    def _check_pattern(self, code: str, pattern_name: str) -> bool:
        # Conceptual implementation using regex on source code
        regex = self.risk_patterns.get(pattern_name)
        if regex:
            return bool(re.search(regex, code, re.IGNORECASE))
        return False
        
    def _verify_renouncement(self, code: str) -> bool:
        # Mock check
        return False
