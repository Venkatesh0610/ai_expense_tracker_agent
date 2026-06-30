# AI Expense Tracker using OpenAI Function Calling

## Overview

AI Expense Tracker is a Python application that uses OpenAI Function Calling to automatically extract expense details from natural language and store them in a local JSON database.

Example inputs:

- Spent 250 on Swiggy
- Paid 500 for Uber
- Bought groceries for 1200

The AI identifies the amount, category, and description, then logs the expense automatically.

---

## Features

- Natural language expense logging
- OpenAI Function Calling
- Automatic expense categorization
- Local JSON storage
- Lightweight and beginner-friendly
- Easy to extend with analytics and dashboards

---

## Project Structure

```text
project/
│
├── app.py
├── tools.py
├── expenses.json
└── README.md
```

---

## How It Works

1. User enters an expense in natural language.
2. OpenAI extracts:
   - Amount
   - Category
   - Description
3. The model triggers the `save_expense_to_db()` function.
4. The expense is stored in `expenses.json`.

Example:

Input:

```text
Spent 250 on Swiggy
```

Extracted Data:

```json
{
  "amount": 250,
  "category": "Food",
  "description": "Swiggy"
}
```

Stored in:

```json
[
  {
    "amount": 250,
    "category": "Food",
    "description": "Swiggy"
  }
]
```

---

## Prerequisites

- Python 3.9+
- OpenAI API Key

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd ai-expense-tracker
```

### Install Dependencies

```bash
pip install openai
```

### Configure API Key

Replace:

```python
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
```

with:

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

---

## Running the Application

```bash
python app.py
```

Example:

```text
User : Paid 300 for Uber
```

Output:

```text
Success: Logged 300 INR under Travel.
```

---

## Example Inputs

```text
Spent 250 on Swiggy
Paid 500 for Uber
Bought groceries for 1200
Electricity bill of 1500
Movie tickets cost 700
```

---

## Tool Schema

Function:

```python
save_expense_to_db()
```

Parameters:

| Parameter | Type | Description |
|-----------|------|-------------|
| amount | number | Expense amount |
| category | string | Expense category |
| description | string | Merchant or context |

---

## Sample Database

```json
[
  {
    "amount": 250,
    "category": "Food",
    "description": "Swiggy"
  },
  {
    "amount": 500,
    "category": "Travel",
    "description": "Uber"
  }
]
```

---

## Future Enhancements

- Update expenses
- Delete expenses
- View all expenses
- Expense analytics
- Category-wise charts
- Monthly reports
- Google Sheets integration
- Cloud storage
- Multi-user support
- AI spending insights

---

## Concepts Covered

- OpenAI Function Calling
- Tool Calling
- Structured Outputs
- JSON Storage
- Python File Handling
- AI Agents Fundamentals

---

## License

This project is provided for educational and learning purposes.
