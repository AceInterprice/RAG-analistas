from backend.core.ollama_client import ask_llm
from backend.rag.prompts import SYSTEM_PROMPT


def responder(
    narrativa: str
) -> str:
    """
    Genera respuesta usando RAG.
    
    Espera recibir un prompt que ya contiene:
    - La narrativa del caso (información principal)
    - El contexto enriquecedor (información complementaria)
    
    La narrativa siempre es lo principal, el contexto es solo complementario.
    """

    if not narrativa:
        return ""

    prompt_completo = f"""
{SYSTEM_PROMPT}

=== SOLICITUD PARA PROCESAMIENTO ===

{narrativa}
"""

    respuesta = ask_llm(prompt_completo)

    return respuesta