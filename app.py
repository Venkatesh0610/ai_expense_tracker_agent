import json
from openai import OpenAI
from tools import expense_tool_schema, save_expense_to_db

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
system_prompt = "You are a precise expense tracker. Convert casual entries into strict categories: Swiggy -> Food, Uber -> Travel."
user_input = input("User : ")

if user_input.strip():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
        tools=[expense_tool_schema],
    )
    if response.choices[0].message.tool_calls:
        tool_call = response.choices[0].message.tool_calls[0]
        if tool_call.function.name == "save_expense_to_db":
            args = json.loads(tool_call.function.arguments)
            print(save_expense_to_db(amount=args.get("amount"), category=args.get("category"), description=args.get("description")))
    else:
        print(f"\nModel Response: {response.choices[0].message.content}")
else:
    print("No input provided. Exiting.")
