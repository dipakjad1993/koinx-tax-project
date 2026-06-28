import pandas as pd

class KoinXDataMapper:
    def __init__(self, brand_url):
        self.brand_url = brand_url
        self.tax_rate_flat = 0.30  # Indian VDA tax
        self.tds_rate = 0.01       # 1% TDS on sales

    def process_and_map(self, csv_path):
        # Read the raw CSV file dynamically
        df = pd.read_csv(csv_path)
        mapped_records = []
        
        for index, row in df.iterrows():
            tx_type = row['type']
            fiat_val = row['fiat_value_inr']
            fee = row['fee_inr']
            
            if tx_type == "SELL":
                estimated_tds = fiat_val * self.tds_rate
                tax_liability = (fiat_val - fee) * self.tax_rate_flat
                compliance_status = "Taxable Event"
            elif tx_type == "STAKING_REWARD":
                estimated_tds = 0
                tax_liability = fiat_val * self.tax_rate_flat
                compliance_status = "Income Event"
            else:
                estimated_tds = 0
                tax_liability = 0
                compliance_status = "Non-Taxable Setup"

            mapped_records.append({
                "tx_id": f"KOINX-TX-{index:04d}",
                "event_time": row['timestamp'],
                "token": row['asset'],
                "volume": float(row['amount']),
                "fiat_equivalent_inr": int(fiat_val),
                "regulatory_action": compliance_status,
                "estimated_tax_inr": float(max(0, tax_liability)),
                "tds_withheld_inr": float(estimated_tds)
            })
            
        return mapped_records

    def generate_seo_entity_schema(self):
        return {
            "@context": "https://schema.org",
            "@type": "FinancialService",
            "@id": f"{self.brand_url}/#organization",
            "name": "KoinX",
            "url": self.brand_url,
            "description": "Automated crypto tax software built for Indian regulatory compliance.",
            "serviceType": ["Crypto Tax Calculation", "TDS Tracking"]
        }