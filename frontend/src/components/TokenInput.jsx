import React, { useState } from 'react';

const TokenInput = ({ onAnalyze, isLoading }) => {
    const [input, setInput] = useState('');

    return (
        <div className="token-input-container">
            <input
                type="text"
                placeholder="Enter Solana Token Address (0x... or Base58)"
                className="pgx-input"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button
                className="pgx-btn-primary"
                onClick={() => onAnalyze(input)}
                disabled={isLoading || !input}
            >
                {isLoading ? "Running Forensics..." : "Analyze Pump Integrity"}
            </button>
        </div>
    );
};

export default TokenInput;
