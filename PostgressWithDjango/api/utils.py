from typing import Generator
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def stream_groq_response(query: str) -> Generator[str, None, None]:
    """
    Streams a markdown-formatted blog article from Groq,
    yielding text chunks as they arrive.
    """
    client = Groq()

    system_prompt = (
        "You write exceptionally high-quality, structured, Markdown-formatted, "
        "long-form, SEO-optimized blog posts. You stream copy in small coherent segments that render cleanly."
    )

    user_prompt = f"""
You are a world-class expert blogger, known for deep expertise, clarity of
thought, & elegant storytelling.

Write a high-quality, long-form blog post based on the topic below.

# Requirements

## Writing Style
- human, engaging, confident
- insightful with original angles
- clear, friendly, intelligent
- NOT generic or fluffy

## Structure (MANDATORY, in Markdown)
- catchy title (H1)
- 2–4 sentence opening hook
- table of contents
- sections with H2/H3
- real-world examples
- bullet points when useful
- short paragraphs
- conclusion
- 5 FAQs at the end

## SEO (MANDATORY)
- keyword variations naturally placed
- semantic richness
- meaningful subheadings
- avoid repetition
- avoid keyword stuffing

## Formatting Rules
- always markdown
- never wrap results inside ``` fenced blocks
- stream in readable micro-chunks

# Topic:
{query}

Begin now.
"""

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0.9,
        max_completion_tokens=8192,
        stream=True,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    for chunk in completion:
        delta = chunk.choices[0].delta
        if hasattr(delta, "content") and delta.content:
            yield delta.content
