# Ajuste de tono con LoRA

**Módulo 1 · Challenge de Fine-tuning y Evaluación de Modelos**

Fine-tuning de un modelo ligero para que responda en el tono de una empresa de soporte técnico, sin reentrenar el modelo completo.

## El problema

Un modelo base responde correcto pero genérico: se extiende, divaga y no cita la condición que aplica. Lo que la empresa necesita es otra cosa — respuestas breves, en segunda persona, que mencionen la condición concreta de la política y no se vayan por las ramas.

Eso no es conocimiento, es **estilo**, y el estilo no se arregla con RAG ni alargando el prompt: se enseña con ejemplos.

## El dataset

[`dataset_entrenamiento.py`](dataset_entrenamiento.py) contiene los pares pregunta–respuesta que enseñan el patrón. Cubren garantía, daños por líquidos, caídas, batería, componentes cambiados por el usuario y pérdida de factura.

La decisión de diseño es que **el contenido sale de la misma política interna** que usa el asistente de soporte. Así el modelo aprende formato sobre información real y no memoriza datos falsos que después contradigan a la fuente de verdad.

## Por qué LoRA

LoRA agrega matrices pequeñas entrenables sin tocar los pesos originales del modelo. Eso permite que el ajuste corra en minutos sobre la GPU gratuita de Colab, y que el resultado sea un adaptador de unos pocos megabytes en lugar de una copia completa del modelo.

El entrenamiento se hizo sobre TinyLlama 1.1B, que es la variante ligera; el notebook deja indicada la equivalencia con `meta-llama/Llama-3.2-1B-Instruct` para correrlo con el modelo oficial de Meta.

## Stack

TinyLlama 1.1B · PEFT / LoRA · TRL · Transformers · Hugging Face Hub
