import React from 'react';
import TrustScoreCard from './TrustScoreCard';

const Dashboard = ({ data, address, onReset }) => {
    return (
        <div className="dashboard-container">
            <header className="dash-header">
                <button className="back-btn" onClick={onReset}>← New Analysis</button>
                <h2>Forensic Report: {address.substring(0, 8)}...</h2>
            </header>

            <div className="dash-grid">
                <div className="main-stats">
                    <TrustScoreCard
                        score={data.trust_score}
                        risk={data.risk_level}
                        verdict={data.verdict}
                    />
                    <div className="ai-insight-box">
                        <h4>AI Reasoning</h4>
                        <p>{data.ai_insights}</p>
                    </div>
                </div>

                <div className="detailed-metrics">
                    <div className="metric-item">
                        <span>Volume Integrity</span>
                        <div className={`status-tag ${data.analysis?.volume_integrity?.is_organic ? 'secure' : 'warning'}`}>
                            {data.analysis?.volume_integrity?.is_organic ? 'ORGANIC' : 'INORGANIC'}
                        </div>
                    </div>
                    <div className="metric-item">
                        <span>Wallet Distribution</span>
                        <span>{data.analysis?.wallet_clustering?.top_10_holding_pct?.toFixed(1)}% in Top 10</span>
                    </div>
                    <div className="metric-item">
                        <span>Sniper Activity</span>
                        <span>{data.analysis?.wallet_clustering?.sniper_count} Wallets Identifed</span>
                    </div>
                    <div className="metric-item">
                        <span>Contract Vulnerability</span>
                        <span className="danger-text">{data.analysis?.contract_security?.risk_score}/100</span>
                    </div>
                </div>
            </div>

            <section className="raw-data">
                <h4>System Log / Metadata</h4>
                <pre>{JSON.stringify(data.analysis, null, 2)}</pre>
            </section>
        </div>
    );
};

export default Dashboard;
