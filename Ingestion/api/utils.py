import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def describe_image_with_groq(image_path: str, prompt: str = "Describe this image in detail"):
    client = Groq()

    # Read & encode image
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    data_url = f"data:image/jpeg;base64,{image_b64}"

    # Build message aligned with allowed types
    messages = [
        {
            "role": "user",
            "content": [
                { "type": "text", "text": prompt },
                { "type": "image_url", "image_url": { "url": data_url } }
            ]
        }
    ]

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",  # use a vision-capable model
        messages=messages,
        temperature=0.8,
        max_completion_tokens=512,
        top_p=1,
        stream=True
    )

    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""
    return result
