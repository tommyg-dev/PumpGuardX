import React from 'react';

const TrustScoreCard = ({ score, risk, verdict }) => {
    const getScoreColor = (s) => {
        if (s > 75) return '#00ffcc'; // Teal/Safe
        if (s > 40) return '#ffcc00'; // Yellow/Warning
        return '#ff3366'; // Red/Danger
    };

    return (
        <div className="score-card">
            <div className="score-circle-container">
                <svg viewBox="0 0 36 36" className="circular-chart">
                    <path className="circle-bg"
                        d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                    <path className="circle"
                        strokeDasharray={`${score}, 100`}
                        stroke={getScoreColor(score)}
                        d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                    <text x="18" y="20.35" className="percentage" fill={getScoreColor(score)}>{score}</text>
                </svg>
            </div>
            <div className="score-label">
                <h3>AI Verdict: <span style={{ color: getScoreColor(score) }}>{verdict}</span></h3>
                <p>Risk Exposure: {risk}</p>
            </div>
        </div>
    );
};

export default TrustScoreCard;
