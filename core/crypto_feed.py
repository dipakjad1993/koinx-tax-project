import random

def fetch_simulated_compliance_flow():
    """Generates continuous live activity feeds mimicking real-world AI engine crawl patterns."""
    user_agents = ["OAI-SearchBot", "PerplexityBot", "Gemini-User", "Claude-SearchBot"]
    target_nodes = ["/in/crypto-tax-slabs", "/in/tds-compliance", "/in/itr2-vda-guide"]
    
    return {
        "bot": random.choice(user_agents),
        "endpoint": random.choice(target_nodes),
        "response_code": random.choice([200, 200, 200, 403, 200]),
        "bytes_scraped": random.randint(1420, 8950)
    }