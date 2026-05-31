# Prueba Técnica - Analista de Inteligencia Artificial

## Descripción General

Este repositorio contiene el desarrollo de los retos técnicos propuestos para el cargo de Analista de Inteligencia Artificial.

El objetivo principal es demostrar habilidades relacionadas con:

* Diseño de agentes conversacionales
* Automatización de procesos
* Integración de servicios empresariales
* Orquestación mediante Microsoft Copilot Studio y Power Automate
* Desarrollo de scripts en Python
* Control de versiones y documentación técnica

---

# Estructura del Proyecto

```bash
├── data/                  # Archivos de entrada o datasets utilizados
├── diagrams/              # Diagramas y arquitectura de soluciones
├── scripts/               # Scripts desarrollados para los retos
├── README.md              # Documentación principal del proyecto
└── requirements.txt       # Dependencias del entorno Python
```

---

# Reto 1 - Lógica y Orquestación de Agentes

## Objetivo

Diseñar la arquitectura de un agente conversacional capaz de automatizar solicitudes repetitivas relacionadas con certificados laborales.

El agente fue modelado utilizando una arquitectura por capas para separar responsabilidades y facilitar la escalabilidad del flujo conversacional.

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
* Envío del documento al usuario
* Manejo de errores y fallback
* Escalamiento a agente humano
* Control de reintentos para evitar ciclos infinitos

---

# Diagrama del Reto 1

Ubicación:

```bash
diagrams/reto1_arquitectura_agente_certificado_laboral.png
```

---

# Tecnologías Utilizadas

* Microsoft Copilot Studio
* Power Automate
* Draw.io
* Git y GitHub
* Python

---

# Estado del Proyecto

* [x] Reto 1 - Arquitectura conversacional
* [ ] Reto 2
* [ ] Reto 3

---

# Autor

Desarrollado como parte de prueba técnica para proceso de selección de Analista de Inteligencia Artificial.
