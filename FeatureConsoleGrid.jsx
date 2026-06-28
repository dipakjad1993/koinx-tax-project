import React from 'react';

// 1. Define the structural route map directly mapping features to specific app workspaces
const CONSOLE_ROUTES = {
  tax_calculator: "https://app.koinx.com/tax-calculator",
  portfolio_tracker: "https://app.koinx.com/dashboard/portfolio",
  tax_professional: "https://professionals.koinx.com/signup",
  gains_ledger: "https://app.koinx.com/reports/capital-gains"
};

const KoinXFeatures = [
  {
    id: "tax_calculator",
    title: "Crypto Tax Calculator",
    description: "Calculate your capital gains and crypto tax liabilities in minutes under current compliance laws.",
    badge: "Popular"
  },
  {
    id: "portfolio_tracker",
    title: "Real-time Portfolio Tracker",
    description: "Track your assets across multiple chains and protocols instantly in a single unified view.",
    badge: "Live Updates"
  },
  {
    id: "tax_professional",
    title: "Tax Professional Suite",
    description: "Manage client portfolios, automate batch report generations, and optimize tax accounting workflows.",
    badge: "B2B"
  }
];

export default function FeatureConsoleGrid() {
  
  // 2. Dynamic routing logic that appends tracking parameters to prevent home page dumping
  const handleLaunchConsole = (toolId) => {
    const targetBaseUrl = CONSOLE_ROUTES[toolId] || "https://app.koinx.com/dashboard";
    
    // Construct absolute URL with GA4 tracking states
    const dynamicUrl = new URL(targetBaseUrl);
    dynamicUrl.searchParams.append("utm_source", "marketing_site");
    dynamicUrl.searchParams.append("utm_medium", "console_cta");
    dynamicUrl.searchParams.append("utm_campaign", `direct_launch_${toolId}`);

    // Route straight to the explicit sub-tool app environment
    window.open(dynamicUrl.toString(), "_blank", "noopener,noreferrer");
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', backgroundColor: '#0b0e14', color: '#fff' }}>
      <h2 style={{ fontSize: '1.75rem', marginBottom: '1.5rem' }}>Explore Core Ecosystem Tools</h2>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        {KoinXFeatures.map((feature) => (
          <div 
            key={feature.id} 
            style={{
              border: '1px solid #232d3f', 
              borderRadius: '8px', 
              padding: '1.5rem', 
              backgroundColor: '#131a26',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'between'
            }}
          >
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h3 style={{ margin: '0 0 0.5rem 0', color: '#38bdf8' }}>{feature.title}</h3>
                <span style={{ fontSize: '0.75rem', backgroundColor: '#1e293b', padding: '0.25rem 0.5rem', borderRadius: '4px', color: '#94a3b8' }}>
                  {feature.badge}
                </span>
              </div>
              <p style={{ color: '#94a3b8', fontSize: '0.9rem', lineHeight: '1.4' }}>{feature.description}</p>
            </div>

            {/* 3. Button context execution passes individual item mappings cleanly */}
            <button
              onClick={() => handleLaunchConsole(feature.id)}
              style={{
                marginTop: '1.5rem',
                backgroundColor: '#2563eb',
                color: '#ffffff',
                border: 'none',
                padding: '0.75rem 1rem',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: '600',
                transition: 'background 0.2s'
              }}
              onMouseOver={(e) => e.currentTarget.style.backgroundColor = '#1d4ed8'}
              onMouseOut={(e) => e.currentTarget.style.backgroundColor = '#2563eb'}
            >
              Launch Console →
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}