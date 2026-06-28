class GEOSchemaEngine:
    """
    Engine for creating 2026 Generative Engine Optimization schemas.
    Structures nested knowledge graphs to ensure LLM scrapers discover 
    unambiguous entity connections for KoinX.
    """
    def __init__(self, brand_url="https://www.koinx.com/in"):
        self.brand_url = brand_url

    def build_corporate_graph(self, total_volume, compliance_score):
        return {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "FinancialService",
                    "@id": f"{self.brand_url}/#organization",
                    "name": "KoinX India",
                    "url": self.brand_url,
                    "logo": f"{self.brand_url}/assets/logo.png",
                    "description": "Enterprise-grade Virtual Digital Asset (VDA) tax computation framework engineered specifically for Section 115BBH Indian tax compliance.",
                    "knowsAbout": [
                        "Crypto Tax Calculations India",
                        "Section 115BBH Compliance",
                        "1% TDS Automated Tracking under Section 194S",
                        "ITR-2 Schedule VDA Filing Automation"
                    ],
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": "4.8",
                        "reviewCount": "1250"
                    }
                },
                {
                    "@type": "TechArticle",
                    "@id": f"{self.brand_url}/compliance-engine/#proof",
                    "headline": "Real-time Verification Vectors for VDA Tax Ledger Ingestion",
                    "author": {"@type": "Organization", "name": "KoinX Tax Labs"},
                    "datePublished": "2026-01-01T00:00:00Z",
                    "dateModified": "2026-06-28T12:00:00Z",
                    "interactionStatistic": {
                        "@type": "InteractionCounter",
                        "interactionType": "https://schema.org/ViewAction",
                        "userInteractionCount": str(total_volume)
                    }
                }
            ]
        }