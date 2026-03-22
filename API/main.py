from fastapi import FastAPI, HTTPException
from NetCalc import NetworkTopologyCalculator

app = FastAPI(title="NetCalc API")
calculator = NetworkTopologyCalculator()

@app.get("/calculate")
async def calculate(ip: str, prefix: int):
    try:
        # Validate input
        octets = [int(o) for o in ip.split(".")]
        if len(octets) != 4 or not (8 <= prefix <= 32):
            raise ValueError()
            
        # Run your logic
        results = calculator.get_all_metrics(octets, prefix)
        return results
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid IP format or prefix (8-32)")

@app.get("/health")
def check_health():
    return {"status": "online", "system": "Windows 11"}