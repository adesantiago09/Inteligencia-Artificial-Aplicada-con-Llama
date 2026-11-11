# Dataset completo: el estilo que debe aprender el asistente

# Cada ejemplo enseña el patrón deseado: respuesta breve, en segunda persona,
# que cita la condición que aplica y no se va por las ramas. El contenido sale de
# la misma política, así que el modelo aprende formato sobre información real.
ejemplos_entrenamiento = [
    # --- Garantía ---
    {"pregunta": "¿Cuánto dura la garantía?",
     "respuesta": "Tu equipo tiene 12 meses de garantía a partir de la fecha de factura. Aplica únicamente para fallas de fábrica."},
    {"pregunta": "Se me cayó agua en la laptop, ¿está cubierta?",
     "respuesta": "Lamentablemente no. La garantía excluye los daños por líquidos, así que la reparación se cotizaría como servicio fuera de garantía."},
    {"pregunta": "Perdí mi factura, ¿puedo usar la garantía?",
     "respuesta": "Necesitas la factura original o tu comprobante de compra digital para hacerla válida. Si compraste en línea, podemos ayudarte a recuperarlo."},
    {"pregunta": "¿La batería tiene la misma garantía que la laptop?",
     "respuesta": "No, la batería y el cargador tienen 6 meses de garantía por tratarse de consumibles."},
    {"pregunta": "Le cambié la memoria RAM yo mismo, ¿pasa algo?",
     "respuesta": "Abrir el equipo o cambiar componentes por cuenta propia anula la garantía de forma inmediata."},
    {"pregunta": "Se me cayó la computadora de la mesa, ¿me la cubren?",
     "respuesta": "Los daños por caídas y golpes no están cubiertos por la garantía. Podemos revisarla y darte un presupuesto de reparación."},
    {"pregunta": "Hubo un apagón y ya no enciende mi PC.",
     "respuesta": "Los daños por sobrecarga eléctrica quedan fuera de la garantía. Llévala a diagnóstico y te entregamos el presupuesto por escrito."},
    {"pregunta": "Compré hace 14 meses, ¿todavía aplica?",
     "respuesta": "La garantía cubre 12 meses desde la fecha de factura, así que tu equipo ya está fuera de ese periodo."},
    {"pregunta": "¿La garantía cubre que se trabe el sistema?",
     "respuesta": "La garantía aplica a fallas de fábrica del equipo. Si es un problema de software, el soporte remoto puede ayudarte a revisarlo."},
    {"pregunta": "¿Qué necesito llevar para hacer válida mi garantía?",
     "respuesta": "Solo necesitas tu factura original o el comprobante de compra digital junto con el equipo."},

    # --- Soporte y horarios ---
    {"pregunta": "¿A qué hora abren?",
     "respuesta": "Atendemos de lunes a viernes de 9:00 a 18:00 horas, y los sábados de 9:00 a 14:00 horas."},
    {"pregunta": "Mandé mi reporte el domingo y no me han contestado.",
     "respuesta": "Los reportes recibidos en fin de semana se atienden el siguiente día hábil, y respondemos dentro de las 24 horas hábiles siguientes."},
    {"pregunta": "¿El soporte tiene costo?",
     "respuesta": "Durante el periodo de garantía el soporte remoto es gratuito. Fuera de garantía tiene un costo de 350 pesos por sesión."},
    {"pregunta": "¿Qué necesito para levantar un reporte?",
     "respuesta": "Solo necesitas el número de serie de tu equipo y una descripción de la falla que presenta."},
    {"pregunta": "¿Cuánto tardan en responderme?",
     "respuesta": "Respondemos tu reporte en un plazo máximo de 24 horas hábiles."},
    {"pregunta": "¿Puedo marcarles un sábado en la tarde?",
     "respuesta": "Los sábados atendemos hasta las 14:00 horas. Después de esa hora puedes dejar tu reporte y lo atendemos el lunes."},
    {"pregunta": "No sé dónde está el número de serie.",
     "respuesta": "Lo encuentras en la etiqueta de la parte inferior del equipo. Lo necesitamos junto con la descripción de la falla para levantar tu reporte."},

    # --- Taller y reparaciones ---
    {"pregunta": "¿Llevo el cargador al taller?",
     "respuesta": "Sí, necesitamos que entregues el equipo con su cargador y sin contraseña de arranque."},
    {"pregunta": "¿Se pierden mis archivos si lo mando a reparar?",
     "respuesta": "Te recomendamos respaldar tu información antes de entregarlo, ya que no nos hacemos responsables de los datos almacenados en el equipo."},
    {"pregunta": "¿Cuánto tardan en diagnosticar?",
     "respuesta": "El diagnóstico toma de 3 a 5 días hábiles y te lo entregamos por escrito junto con el presupuesto."},
    {"pregunta": "¿Empiezan a reparar de una vez?",
     "respuesta": "Si tu equipo está fuera de garantía, primero necesitamos que autorices el presupuesto antes de iniciar cualquier trabajo."},
    {"pregunta": "Se me olvidó recoger mi equipo hace dos meses.",
     "respuesta": "Los equipos no recogidos después de 30 días naturales generan un cargo por almacenaje de 50 pesos diarios. Acércate con nosotros para revisar tu caso."},
    {"pregunta": "¿Puedo dejar mi laptop con contraseña?",
     "respuesta": "Necesitamos que la entregues sin contraseña de arranque para poder hacer el diagnóstico."},
    {"pregunta": "Me entregaron el presupuesto pero no quiero repararla.",
     "respuesta": "No hay problema, la reparación solo inicia con tu autorización. Puedes pasar a recoger tu equipo cuando gustes."},

    # --- Envíos y devoluciones ---
    {"pregunta": "¿El envío me sale gratis?",
     "respuesta": "El envío dentro del país es gratuito en compras mayores a 5,000 pesos, y tarda de 3 a 7 días hábiles."},
    {"pregunta": "¿Hasta cuándo puedo devolver algo?",
     "respuesta": "Puedes devolverlo hasta 30 días después de la compra, con el producto sin uso y en su empaque original."},
    {"pregunta": "Compré un monitor en oferta y no me gustó.",
     "respuesta": "Los productos en oferta o liquidación no admiten devolución, pero sí puedes hacer el cambio por otro modelo."},
    {"pregunta": "Pedí una PC armada a la medida y quiero devolverla.",
     "respuesta": "El equipo armado por pedido especial no admite devolución, salvo que presente una falla de fábrica."},
    {"pregunta": "Ya abrí la caja, ¿todavía puedo devolverlo?",
     "respuesta": "Para la devolución necesitamos que el producto esté sin uso y en su empaque original."},

    # --- Fuera de alcance ---
    {"pregunta": "¿Reparan celulares?",
     "respuesta": "Nuestra política de soporte cubre equipo de cómputo. Para ese caso te recomiendo contactar a un agente, que podrá orientarte mejor."}
]

# Conjunto de prueba: preguntas que el modelo NUNCA verá durante el entrenamiento.
# Cada una trae la respuesta de referencia, que es contra la que se medirá.
ejemplos_prueba = [
    {"pregunta": "¿Puedo devolver un teclado que compré la semana pasada?",
     "referencia": "Sí, puedes devolverlo dentro de los 30 días posteriores a la compra, siempre que esté sin uso y en su empaque original."},
    {"pregunta": "Mi PC hace un ruido raro, ¿la garantía lo cubre?",
     "referencia": "Si se trata de una falla de fábrica, sí queda cubierta durante los primeros 12 meses. Llévala a diagnóstico para confirmarlo."},
    {"pregunta": "¿Atienden los domingos?",
     "referencia": "No atendemos los domingos. Nuestro horario es de lunes a viernes de 9:00 a 18:00 y sábados de 9:00 a 14:00 horas."},
    {"pregunta": "¿Qué pasa si no recojo mi equipo a tiempo?",
     "referencia": "Después de 30 días naturales se genera un cargo por almacenaje de 50 pesos diarios."},
    {"pregunta": "Se me derramó refresco en el teclado de mi laptop.",
     "referencia": "Los daños por líquidos no están cubiertos por la garantía, así que la reparación se cotizaría como servicio particular."},
    {"pregunta": "¿Cuánto me cobran por soporte si ya venció mi garantía?",
     "referencia": "Fuera de garantía el soporte remoto tiene un costo de 350 pesos por sesión."},
    {"pregunta": "Compré una laptop de 4,000 pesos, ¿pago envío?",
     "referencia": "El envío gratuito aplica en compras mayores a 5,000 pesos, así que tu pedido sí tendría costo de envío."},
    {"pregunta": "¿El cargador tiene garantía de un año?",
     "referencia": "No, el cargador y la batería tienen 6 meses de garantía por tratarse de consumibles."},
    {"pregunta": "¿Instalan cámaras de seguridad?",
     "referencia": "Nuestra política de soporte cubre equipo de cómputo. Te recomiendo contactar a un agente para ese servicio."},
    {"pregunta": "¿Me avisan antes de cobrarme la reparación?",
     "referencia": "Sí, necesitamos que autorices el presupuesto antes de iniciar cualquier trabajo fuera de garantía."}
]

print("Ejemplos de ENTRENAMIENTO:", len(ejemplos_entrenamiento))
print("Ejemplos de PRUEBA (nunca vistos):", len(ejemplos_prueba))

# Verificación explícita de que los conjuntos no se traslapan.
preguntas_train = {e["pregunta"] for e in ejemplos_entrenamiento}
preguntas_test = {e["pregunta"] for e in ejemplos_prueba}
print("Traslape entre conjuntos:", len(preguntas_train & preguntas_test), "(debe ser 0)")