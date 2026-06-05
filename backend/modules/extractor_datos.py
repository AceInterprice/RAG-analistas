from backend.rag.llm import responder


def extraer_datos(
    narrativa: str
) -> str:
    """
    Extrae información relevante de una narrativa policial.

    No utiliza RAG.
    Trabaja únicamente sobre el texto recibido.
    """

    if not narrativa:
        return ""

    prompt = f"""
NARRATIVA:

{narrativa}

TAREA:

Analiza la narrativa y extrae únicamente los datos relevantes.

IDENTIFICA:

1. Personas mencionadas.
2. Alias.
3. Vehículos.
4. Placas.
5. Objetos robados.
6. Objetos recuperados.
7. Domicilios o ubicaciones.
8. Teléfonos.
9. Cantidades de dinero.
10. Fechas y horas.

REGLAS:

- No inventes información.
- Si un dato no aparece, coloca "No identificado".
- No redactes informes.
- No hagas análisis jurídico.
- No hagas conclusiones.
- Solo organiza la información encontrada.

FORMATO:

PERSONAS:

ALIAS:

VEHÍCULOS:

PLACAS:

OBJETOS ROBADOS:

OBJETOS RECUPERADOS:

DOMICILIOS / UBICACIONES:

TELÉFONOS:

MONTOS DE DINERO:

FECHAS Y HORAS:
"""

    return responder(prompt)