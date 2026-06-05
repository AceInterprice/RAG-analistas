import ollama
from backend.core.config import MODEL_NAME


def ask_llm(prompt: str) -> str:
    """
    Envía prompt a Ollama y devuelve respuesta.
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]