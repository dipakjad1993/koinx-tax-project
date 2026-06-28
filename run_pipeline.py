import json
from core.mapper_engine import KoinXDataMapper

def main():
    # Initialize engine targeting the specific brand market endpoint
    mapper = KoinXDataMapper(brand_url="https://www.koinx.com/in")
    
    print("🚀 Ingesting raw crypto data files...")
    processed_data = mapper.process_and_map("data/raw_wallet_data.csv")
    seo_schema = mapper.generate_seo_entity_schema()
    
    # Bundle the data mapping matrix and web entity structures into one output payload
    final_output = {
        "mapped_transactions": processed_data,
        "search_entity_schema": seo_schema
    }
    
    # Save the processed structure safely to your data folder
    output_path = "data/output_mapped.json"
    with open(output_path, "w") as f:
        json.dump(final_output, f, indent=4)
        
    print(f"✅ Success! Your mapping architecture has been saved to: {output_path}")

if __name__ == "__main__":
    main()