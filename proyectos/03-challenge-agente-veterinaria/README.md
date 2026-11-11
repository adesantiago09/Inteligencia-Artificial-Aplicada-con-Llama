# Agente conversacional para una clínica veterinaria

**Módulo 2 · Challenge de Diseño de Agentes Conversacionales**

Agente que atiende a los dueños de mascotas de una clínica veterinaria: agenda citas, resuelve dudas sobre servicios y vacunas, y escala a una persona cuando el caso lo amerita.

## El enfoque

El challenge está centrado en el **diseño conversacional** más que en la infraestructura: qué debe resolver el agente por su cuenta, qué debe preguntar antes de actuar y en qué momento debe apartarse y llamar a un humano.

Eso se traduce en tres decisiones concretas:

**Detección de urgencias.** Un mensaje sobre una mascota que no respira o que fue atropellada no es una consulta de agenda. Esas frases se detectan antes de que el modelo intervenga y disparan una respuesta inmediata de escalamiento, porque en ese momento la latencia del modelo es el problema, no la respuesta.

**Reglas fijas para lo predecible.** Saludos y despedidas se resuelven con coincidencia exacta sobre el mensaje completo, no por subcadena, de modo que *"gracias"* se atiende con la regla fija pero *"gracias, ¿y cuánto cuesta la vacuna?"* sigue su camino hacia el modelo.

**Límites explícitos.** El agente informa y agenda, pero no diagnostica. El system prompt lo delimita y cualquier consulta clínica se deriva al veterinario.

## Stack

Llama 3.1 8B sobre Ollama · Llama Stack · FastAPI · WhatsApp Cloud API
