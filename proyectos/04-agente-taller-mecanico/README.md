# Agente de WhatsApp para un taller mecánico

**Módulo 2 · Integración entre Llama y WhatsApp**

Primer agente del módulo conectado a WhatsApp de punta a punta. Atiende a los clientes de un taller mecánico: consulta qué horarios hay libres para agendar un servicio y responde las preguntas frecuentes del negocio.

## Qué resuelve

Dos herramientas expuestas al modelo mediante function calling:

**`consultar_disponibilidad`** recibe una fecha en lenguaje natural y devuelve los horarios libres de ese día. Incluye normalización de fechas, porque el cliente escribe *"el martes"*, *"15 de marzo"* o *"mañana"*, no una fecha ISO.

**`buscar_pregunta_frecuente`** resuelve dudas de costos, garantías y servicios a partir de un diccionario de temas, con normalización de acentos para que *"garantía"* y *"garantia"* encuentren lo mismo.

## Piezas de infraestructura

Es donde se arma el andamiaje que después reutiliza FerreBot:

Un **webhook de FastAPI** con dos endpoints, el de verificación que pide Meta y el de recepción de mensajes. La recepción delega a `BackgroundTasks` para responderle a Meta de inmediato, porque si tarda reenvía el mensaje; y guarda el `wamid` de cada mensaje atendido para ignorar los duplicados que llegan de todos modos.

Un **lock por número de teléfono**, para que dos mensajes seguidos del mismo cliente no se procesen en paralelo sobre la misma conversación y dejen el historial inconsistente.

**Memoria por conversación** en Llama Stack, asociando cada número con su `conversation_id`, sin la cual el agente trataría cada mensaje como si fuera el primero.

**Reglas fijas** antes del modelo para saludos y frases de urgencia (*"me quedé varado"*, *"tuve un accidente"*), que tienen una única respuesta correcta y no necesitan pasar por Llama.

**Clasificación de errores** por tipo de falla, distinguiendo un timeout del modelo de una caída de Ollama o de un rechazo de la API de WhatsApp, de modo que cuando algo se rompe se sabe qué fue.

## Stack

Llama 3.1 8B sobre Ollama · Llama Stack · FastAPI · ngrok · WhatsApp Cloud API
