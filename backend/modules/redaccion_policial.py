from backend.rag.hybrid_search import hybrid_search
from backend.rag.llm import responder
from backend.core.historico_repository import guardar_reporte


def redactar_reporte(
    solicitud: str,
    estado_caso: str
) -> str:
    """
    Genera redacción policial basada en la narrativa del usuario.
    La narrativa es la fuente principal.
    El contexto solo se usa para apoyo legal y documental.
    """

    if not solicitud:
        return ""

    contexto = hybrid_search(
        solicitud
    )

    contexto_unido = "\n\n".join(
        contexto
    ) if contexto else ""

    prompt = f"""
NARRATIVA DEL CASO (FUENTE OFICIAL):

{solicitud}

CONTEXTO RECUPERADO (SOLO REFERENCIA LEGAL Y DOCUMENTAL):

{contexto_unido if contexto_unido else "No hay contexto relacionado disponible."}

ESTADO DEL CASO:

{estado_caso}

TAREA:

Convertir la narrativa en un informe policial formal.

REGLAS OBLIGATORIAS:

1. La narrativa es la única fuente oficial de hechos.

2. El contexto solo puede utilizarse para:
   - identificar artículos aplicables
   - fundamentación legal
   - terminología policial
   - estructura documental

3. Está prohibido inventar información.

4. Está prohibido agregar:
   - nombres
   - apodos
   - edades
   - domicilios
   - placas
   - expedientes
   - folios
   - números de oficio
   - fechas
   - horas
   - autoridades
   - testigos

   si dichos datos no aparecen expresamente en la narrativa.

5. No copiar personas, domicilios o datos personales del contexto recuperado.

6. Solo citar artículos que tengan relación directa con los hechos narrados.

7. Si no existe fundamento legal aplicable en el contexto recuperado, escribir:

   "No se encontró fundamento legal aplicable."

8. Si algún dato requerido no está presente en la narrativa, escribir:

   "No especificado en la narrativa."

9. No realizar suposiciones.

10. No completar información faltante.

ESTRUCTURA DEL INFORME:

1. Encabezado
2. Hechos
3. Intervención realizada
4. Observaciones
5. Clasificación preliminar del hecho
6. Fundamento legal
7. Conclusión operativa

IMPORTANTE:

Transforma únicamente la narrativa proporcionada.
No agregues hechos nuevos.
No inventes información.
No utilices datos de otros casos.
"""

    reporte = responder(
        prompt
    )

    try:

        guardar_reporte(
            modulo="Redacción Policial",
            narrativa=solicitud,
            reporte=reporte,
            estado_caso=estado_caso
        )

    except Exception as e:

        print(
            f"Error guardando histórico: {e}"
        )

    return reporte