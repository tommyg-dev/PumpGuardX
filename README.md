# PumpGuardX AI

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![Frontend](https://img.shields.io/badge/react-18-teal.svg)]()
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)]()

**Advanced On-Chain Forensic Protocol for Pump.fun Assets**

---

## 1. Project Overview & Mission Statement

PumpGuardX is a decentralized intelligence system designed to sanitize the Solana token launch ecosystem. Our mission is to provide retail participants with institutional-grade forensic tools that detect algorithmic manipulation, Sybil attacks, and malicious contract patterns in real-time.

As the velocity of token launches increases, the technical barrier for due diligence has become too high for the average user. PumpGuardX bridges this gap by abstracting complex graph theory and statistical analysis into a simple, interpretable **Trust Score**.

## 2. Problem Statement

The "Pump and Dump" economy on platforms like Pump.fun relies on information asymmetry. Malicious actors use sophisticated tooling to:
*   **Fake Volume:** Using wash-trading bots to simulate market interest and attract retail buy-in.
*   **Cluster Holdings:** Distributing supply across hundreds of "fresh" wallets to bypass concentration alerts.
*   **Manipulate Charts:** Coordinated buy/sell pressure designed to trigger FOMO.

PumpGuardX treats these activities as **Anomalies** and applies algorithmic detection to separate organic market behavior from artificial manipulation.

## 3. Features

*   **Multivariate Wallet Clustering:** Detects linked entities through funding-graph analysis and transaction proximity.
*   **Volume Authenticity Engine:** Applies statistical tests (recursive Benford testing) to trade histories to identify bot-driven distributions.
*   **Bytecode Risk Scanner:** Static analysis of Solana/Anchor contracts to detect hidden freeze or mint authorities.
*   **AI Verdict System:** A specialized ensemble model trained on thousands of successful and failed launches provides a qualitative risk assessment.
*   **Interactive Forensic Dashboard:** Real-time visualization of risk metrics and supply distribution.

## 4. System Architecture

```text
[Frontend/React] <---> [FastAPI Backend] <---> [On-Chain Data Indexer]
                            |
           _________________|_________________
          |                 |                 |
    [Wallet Clusterer] [Volume Analyzer] [Contract Scanner]
          |                 |                 |
          |_________________V_________________|
                            |
                 [AI Scoring & Verdict Engine]
```

## 5. AI Methodology & Trust Score

PumpGuardX utilizes a multi-step inference pipeline:
1.  **Feature Extraction:** Normalizes raw RPC data into 150+ quantitative features.
2.  **Pattern Recognition:** Identifies signatures of known botting scripts and "Developer-Exit" scenarios.
3.  **Synthesis:** Combines quantitative penalties (concentration, taxes) with qualitative AI confidence scores.

The resulting **Trust Score (0-100)** is categorized into risk tiers:
*   **80-100 (LOW):** Organic behavior, decentralized supply.
*   **50-79 (MEDIUM):** Some suspicious clustering or low liquidity.
*   **30-49 (HIGH):** Significant inorganic volume or centralized holdings.
*   **0-29 (CRITICAL):** Malicious contract code or extreme Sybil manipulation.

## 6. Installation

### Backend (Python)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --reload
```

### Frontend (React)
```bash
cd frontend
npm install
npm start
```

## 7. Roadmap

*   **Phase Alpha (Current):** Core analysis engine and static wallet clustering.
*   **Phase Beta:** Integration with real-time mempool data for "Pre-Pump" warnings.
*   **Phase Public:** Community-driven risk labeling system and API for Telegram bots.
*   **Phase DAO:** Governance of risk weighting parameters via PGX token holders.

## 8. Disclaimer

**PumpGuardX is an experimental research tool and NOT financial advice.** Decentralized finance (DeFi) involves high risk. This software uses probabilistic models that may not capture all types of exploits. Always conduct independent research before interacting with digital assets.

---

*Built by the PumpGuardX Research Group. Open Source and Verifiable.*
