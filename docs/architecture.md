# PumpGuardX System Architecture

```mermaid
graph LR
    User -->|Token Address| Frontend[React Dashboard]
    Frontend -->|POST /analyze| API[FastAPI Gateway]
    API -->|Fetch RPC| RPC[Solana Node / Helius]
    API -->|Raw Data| Engine{Analysis Core}
    
    subgraph Analysis Core
        W[Wallet Analyzer]
        V[Volume Analyzer]
        C[Contract Scanner]
    end
    
    W -->|Metrics| Score[Scoring Engine]
    V -->|Metrics| Score
    C -->|Metrics| Score
    
    Score -->|Final Result| User
```

## Tech Stack
- **Backend:** Python 3.10+, FastAPI, NumPy, NetworkX
- **Frontend:** React, Framer Motion, Tailwind (CSS)
- **Data:** Helius RPC, Birdeye API (Integration Layer)
- **AI Model:** Proprietary Ensemble Classifier
