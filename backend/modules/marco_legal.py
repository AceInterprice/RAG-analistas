from backend.rag.retriever import buscar_contexto
from backend.rag.llm import responder


def consultar_marco_legal(
    consulta: str
) -> str:
    """
    Consulta el marco legal aplicable a una situación
    descrita por el usuario.
    """

    if not consulta:
        return ""

    contexto = buscar_contexto(
        consulta,
        tipo="ley"
    )

    contexto_unido = "\n\n".join(
        contexto
    ) if contexto else ""

    prompt = f"""
SITUACIÓN ANALIZADA:

{consulta}

CONTEXTO LEGAL RECUPERADO:

{contexto_unido if contexto_unido else "No se encontró contexto legal relacionado."}

TAREA:

Analiza la situación planteada y determina el posible marco legal aplicable.

OBJETIVO:

Brindar apoyo a un operador analista de seguridad pública para identificar
la normatividad relacionada con los hechos descritos.

RESTRICCIÓN ABSOLUTA:

ÚNICAMENTE puedes utilizar artículos que aparezcan literalmente
en el apartado "CONTEXTO LEGAL RECUPERADO".

Está prohibido:

- Inventar artículos.
- Inventar leyes.
- Inventar reglamentos.
- Inventar códigos penales.
- Utilizar legislación de otros países.
- Utilizar conocimiento propio fuera del contexto.
- Mencionar artículos que no aparezcan en el contexto.

Si no existe fundamento legal suficiente responde únicamente:

NO SE ENCONTRÓ FUNDAMENTO LEGAL SUFICIENTE EN LA BASE DE CONOCIMIENTO.

REGLAS ADICIONALES:

1. No inventes hechos.
2. Basa el análisis únicamente en la situación descrita.
3. Explica únicamente relaciones observables entre los hechos y los artículos recuperados.
4. No redactes informes policiales.
5. No emitas conclusiones judiciales.
6. Mantén un lenguaje técnico para personal analista.

FORMATO DE RESPUESTA:

CLASIFICACIÓN PRELIMINAR

Indica únicamente conductas que puedan relacionarse con los artículos encontrados.

Si no existe relación clara indica:

"No se pudo determinar clasificación con la información disponible."

ARTÍCULOS RELACIONADOS

Enumera únicamente artículos presentes en el contexto recuperado.

FUNDAMENTACIÓN

Explica por qué los artículos encontrados podrían relacionarse con los hechos descritos.

OBSERVACIONES PARA EL ANALISTA

Indica información adicional que debería verificarse para determinar con mayor precisión la situación jurídica.
"""

    return responder(
        prompt
    )