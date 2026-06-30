import json
import os

def save_expense_to_db(amount: float, category: str, description: str) -> str:
    expense_item = {"amount": amount, "category": category, "description": description}
    file_path = "expenses.json"
    data = []
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
                
    data.append(expense_item)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
        
    return f"Success: Logged {amount} INR under {category}."

expense_tool_schema = {
    "type": "function",
    "function": {
        "name": "save_expense_to_db",
        "description": "Call this whenever the user wants to log, record, or track a financial expense.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number", "description": "The numeric cost of the expense in INR."},
                "category": {"type": "string", "description": "The category (e.g., Food, Travel, Shopping, Bills)."},
                "description": {"type": "string", "description": "The merchant or context (e.g., Swiggy, Uber)."}
            },
            "required": ["amount", "category", "description"]
        }
    }
}
