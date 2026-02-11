# PumpGuardX Methodology

## 1. Statistical Volume Analysis
We utilize recursive Benford Distribution testing on trade sizes to identify inorganic spikes. Organic market participants typically follow a predictable distribution of trade sizes, whereas wash-trading bots exhibit high concentrations of identical or sequentially incrementing values.

## 2. Graph-Based Wallet Clustering
Our system builds a dynamic transaction graph. By applying community detection algorithms (e.g., Louvain Modularity), we identify groups of wallets that share funding sources or transact in coordinated blocks. Any cluster exceeding 5% of total supply that originated from common "central" wallets is flagged.

## 3. Bytecode Heuristics
Static analysis scans for patterns in the compiled binary or source code that allow:
- `FreezeAuthority`: The ability to stop individual wallets from selling.
- `MintAuthority`: The ability to inflate supply and dilute holders.
- `TaxDynamic`: Hidden functions to increase sell tax to 99%.

## 4. Trust Score Synthesis
The final score is a weighted average:
- Wallet Integrity (40%)
- Volume Authenticity (30%)
- Contract Security (30%)
- AI Confidence Penalty (Adjustment Factor)
