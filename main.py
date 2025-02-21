from fastapi import FastAPI
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debug: Print the API key to verify
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.get("/motivation")
async def get_motivation():
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Generate a unique, motivational quote for productivity and goal achievement"}],
        model="llama-3.3-70b-versatile",
    )
    return {"motivation": response.choices[0].message.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)