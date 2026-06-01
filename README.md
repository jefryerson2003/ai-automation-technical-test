# Prueba Técnica - Analista de Inteligencia Artificial

## Descripción General

Este repositorio contiene el desarrollo de los retos técnicos propuestos para el cargo de Analista de Inteligencia Artificial.

El objetivo principal es demostrar habilidades relacionadas con:

* Diseño de agentes conversacionales
* Automatización de procesos
* Integración de servicios empresariales
* Orquestación mediante Microsoft Copilot Studio y Power Automate
* Desarrollo de scripts en Python
* Procesamiento y limpieza de datos
* Manejo robusto de excepciones
* Control de versiones y documentación técnica

---

# Estructura del Proyecto

```bash
├── data/                  # Archivos de entrada y salida del procesamiento
├── diagrams/              # Diagramas de arquitectura y flujos conversacionales
├── scripts/               # Scripts Python desarrollados
├── README.md              # Documentación principal del proyecto
└── requirements.txt       # Dependencias del entorno Python
```

---

# Reto 1 - Lógica y Orquestación de Agentes

## Objetivo

Diseñar la arquitectura de un agente conversacional capaz de automatizar solicitudes repetitivas relacionadas con certificados laborales.

La solución fue diseñada utilizando una arquitectura por capas para separar responsabilidades y facilitar escalabilidad, validaciones y manejo de errores.

---

# Arquitectura Diseñada

La solución fue dividida en cinco capas principales:

1. Usuario
2. Microsoft Copilot Studio
3. Validaciones y Control
4. Power Automate
5. Sistemas Corporativos

---

# Funcionalidades Implementadas

* Reconocimiento de intención mediante frases desencadenantes
* Solicitud y validación de número de documento
* Solicitud y validación de área o dependencia
* Validación de empleado activo
* Validación cruzada entre área ingresada y registro corporativo
* Generación automatizada del certificado laboral
* Envío del documento PDF al usuario
* Manejo de errores y fallback
* Escalamiento a agente humano
* Control de reintentos para evitar ciclos infinitos

---

# Diagramas del Reto 1

## Archivos incluidos

```bash
diagrams/reto1_arquitectura_agente_certificado_laboral.drawio
diagrams/reto1_arquitectura_agente_certificado_laboral.png
```

---

# Reto 2 - Automatización y Procesamiento de Tickets

## Objetivo

Desarrollar un flujo automatizado en Python capaz de:

1. Leer información desde un archivo CSV
2. Limpiar y normalizar datos
3. Validar estructura y columnas críticas
4. Filtrar tickets críticos pendientes
5. Exportar resultados estructurados
6. Generar un resumen consumible por un agente conversacional

---

# Scripts Implementados

## 1. reto2_ticket_automation.py

Script principal encargado del procesamiento de tickets.

### Funcionalidades

* Lectura de archivos CSV
* Validación robusta de columnas requeridas
* Normalización de cabeceras
* Limpieza de datos
* Eliminación de duplicados
* Filtrado de tickets:

  * Estado = Pendiente
  * Prioridad = Alta
* Exportación a CSV
* Exportación estructurada a JSON
* Manejo avanzado de excepciones

---

## 2. ticket_summary.py

Script encargado de consumir el JSON generado y construir un resumen dinámico para un agente conversacional.

### Funcionalidades

* Lectura del archivo JSON
* Validación de estructura
* Manejo de errores de lectura
* Generación de resumen automático
* Preparación de respuesta para Copilot Studio o Power Automate

Ejemplo de respuesta generada:

```text
Actualmente tienes 6 tickets críticos pendientes por resolver.
```

---

# Archivos de Datos

## Dataset Original

```bash
data/tickets.csv
```

Archivo fuente utilizado para el procesamiento inicial.

---

## Dataset Limpio

```bash
data/tickets_clean.csv
```

Archivo generado tras el proceso de limpieza y normalización.

---

## Tickets Filtrados

```bash
data/critical_tickets.csv
```

Contiene únicamente tickets:

* Pendientes
* Prioridad Alta

---

## Salida JSON

```bash
data/critical_tickets.json
```

Archivo estructurado listo para ser consumido por agentes conversacionales, APIs o flujos automatizados.

Incluye:

* Fecha de generación
* Total de tickets críticos
* Lista completa de tickets filtrados

---

# Diagrama Conversacional - Agente de Soporte TI

## Objetivo

Simular un agente conversacional que:

1. Recibe la solicitud del usuario
2. Reconoce la intención
3. Consume información desde JSON
4. Procesa el total de tickets críticos
5. Entrega una respuesta dinámica al usuario
6. Maneja errores y fallbacks

---

# Diagramas del Reto 2

## Archivos incluidos

```bash
diagrams/reto2_agente_soporte_ti.drawio
diagrams/reto2_agente_soporte_ti.png
```

---

# Reto 3 - Integración y Orquestación de Agentes

## Objetivo

Diseñar un flujo principal de orquestación capaz de unificar los procesos desarrollados en el:

* Reto 1 → Agente de Recursos Humanos
* Reto 2 → Agente de Soporte TI

La arquitectura propuesta centraliza toda la interacción en un único canal conversacional utilizando Microsoft Copilot Studio como orquestador principal.

---

# Arquitectura del Orquestador

La solución fue diseñada siguiendo un patrón:

```text
Orquestador Central → Sub-flujos Especializados
```

El agente principal actúa como punto único de entrada y utiliza reconocimiento de intención (NLU) para enrutar automáticamente las solicitudes hacia el flujo especializado correspondiente.

---

# 1. Configuración del Saludo Inicial

En Microsoft Copilot Studio, el saludo inicial se implementa mediante el:

```text
System Topic → Conversation Start
```

Este Topic se ejecuta automáticamente al iniciar la conversación y permite establecer el contexto general del asistente.

Ejemplo implementado:

```text
"¡Hola! Soy tu Asistente Corporativo Integrado.
Puedo ayudarte con solicitudes de Recursos Humanos
(como certificados laborales) o incidencias de Soporte TI.
¿En qué te puedo ayudar hoy?"
```

---

# 2. Reconocimiento de Intenciones (Intent Recognition)

El reconocimiento de intención se diseñó utilizando Topics personalizados dentro de Microsoft Copilot Studio.

El modelo de lenguaje natural (NLU) analiza automáticamente el mensaje escrito por el usuario y determina qué flujo debe ejecutarse.

---

## Topic 1 - Recursos Humanos

### Trigger Phrases utilizadas

```text
"Necesito certificado laboral"
"Carta laboral"
"Constancia de trabajo"
"Descargar certificado"
```

### Acción ejecutada

El orquestador redirige automáticamente al:

```text
Flujo del Reto 1 → Certificados Laborales
```

---

## Topic 2 - Soporte TI

### Trigger Phrases utilizadas

```text
"Mis tickets"
"Tickets críticos"
"Estado de soporte"
"Casos pendientes"
```

### Acción ejecutada

El orquestador redirige automáticamente al:

```text
Flujo del Reto 2 → Soporte Técnico
```

---

# Lógica de Enrutamiento

Cuando el usuario responde al saludo inicial:

1. El mensaje es enviado al motor NLU de Copilot Studio
2. El modelo analiza intención y contexto
3. Se calcula un nivel de confianza (confidence score)
4. El orquestador selecciona automáticamente el Topic más probable
5. Se ejecuta el sub-flujo correspondiente

Si no existe suficiente confianza en la intención detectada:

* Se activa el fallback global
* El bot solicita reformular la pregunta
* Opcionalmente se transfiere a un agente humano

---

# Ventajas de la Arquitectura Unificada

La arquitectura basada en:

```text
Orquestador → Sub-flujos Especializados
```

presenta múltiples ventajas frente a mantener bots separados:

* Centraliza la experiencia del usuario en un único canal
* Reduce duplicación de lógica conversacional
* Facilita mantenimiento y escalabilidad
* Permite reutilizar componentes y flujos
* Mejora el control de fallback y manejo de errores
* Simplifica futuras integraciones empresariales
* Facilita agregar nuevos dominios o áreas sin rediseñar el sistema completo

Además, cada sub-flujo puede evolucionar de forma independiente sin afectar el comportamiento general del orquestador.

---

# Diagramas del Reto 3

## Archivos incluidos

```bash
diagrams/reto3_orquestador_copilot.drawio
diagrams/reto3_orquestador_copilot.png
```

---


# Tecnologías Utilizadas

* Python 3
* Pandas
* JSON
* Microsoft Copilot Studio
* Power Automate
* Draw.io
* Git
* GitHub
* Visual Studio Code

---

# Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

---

## 2. Crear entorno virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución de Scripts

## Procesamiento principal de tickets

```bash
python scripts/reto2_ticket_automation.py
```

---

## Generar resumen del agente

```bash
python scripts/ticket_summary.py
```

---

# Manejo de Excepciones

El proyecto implementa manejo robusto de errores para escenarios como:

* Archivo inexistente
* CSV vacío
* Estructura corrupta
* JSON inválido
* Columnas faltantes
* Datos inconsistentes
* Fallos de lectura

---

# Estado del Proyecto

* [x] Reto 1 - Arquitectura conversacional
* [x] Reto 2 - Automatización y procesamiento de tickets
* [x] Reto 3 - Integración y orquestación de agentes

---

# Autor
Jefferson Sneyder Anaya Manrique 
Desarrollado como parte de prueba técnica para proceso de selección de Analista de Inteligencia Artificial.
