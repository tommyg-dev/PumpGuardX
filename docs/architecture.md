# LUMI Agent Architecture

LUMI Agent is the sophisticated interface for the Lunaria Protocol, a system designed to guide users through the complex topography of decentralized finance.

```mermaid
graph LR
    User -->|Token Address| Frontend[LUMI Interface]
    Frontend -->|POST /analyze| API[Lunaria Protocol Gateway]
    API -->|Fetch RPC| RPC[On-Chain Data Indexer]
    API -->|Raw Signals| Engine{LUMI Analysis Core}
    
    subgraph LUMI Analysis Core
        W[Wallet Pattern Interpreter]
        V[Volume Authenticity Engine]
        C[Bytecode Risk Scanner]
    end
    
    W -->|Trust Signals| Score[Trust Signal Generator]
    V -->|Trust Signals| Score
    C -->|Trust Signals| Score
    
    Score -->|Final Verdict| User
```

## System Directives
- **Backend:** Python 3.10+, FastAPI, NumPy, NetworkX (Lunaria Protocol Core)
- **Frontend:** React, Framer Motion, Tailwind (LUMI Interface)
- **Data:** On-Chain Data Indexer (Helius/Birdeye Integration)
- **AI Core:** LUMI Ensemble Intelligence

LUMI translates cold, binary signals into human-readable metrics, ensuring that the path through DeFi is always illuminated.
