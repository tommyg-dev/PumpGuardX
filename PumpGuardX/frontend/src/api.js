/**
 * PumpGuardX API Client
 * Wraps communication with the Python FastAPI backend.
 */
const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const fetchAnalysis = async (tokenAddress) => {
    const response = await fetch(`${BASE_URL}/analyze`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            token_address: tokenAddress,
            network: 'solana'
        }),
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Analysis failed');
    }

    return await response.json();
};

export const checkHealth = async () => {
    const response = await fetch(`${BASE_URL}/`);
    return await response.json();
};
