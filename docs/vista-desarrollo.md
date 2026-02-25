---
layout: default
title: Vista de Desarrollo
nav_order: 5
---

# Vista de Desarrollo

Esta sección describe los estándares técnicos y procesos de colaboración del equipo.

## Branching Strategy
Utilizamos **GitHub Flow**:
- `main`: Rama protegida que contiene código estable y listo para despliegue.
- `feat/`, `fix/`, `docs/`, `chore/`: Ramas para desarrollo de funcionalidades, correcciones o documentación.
- Todos los cambios se integran mediante **Pull Requests** hacia `main`.

## Code Review Requirements
- Al menos **1 aprobación** de un par antes de integrar a `main`.
- Superar todos los checks de los pipelines de CI (Documentation, Unit Tests, K8s).
- Comentarios constructivos y resolución de hilos de discusión.

## Commit Message Conventions
Seguimos el estándar de **Conventional Commits**:
- `feat`: Nueva funcionalidad.
- `fix`: Corrección de errores.
- `docs`: Cambios en la documentación.
- `chore`: Tareas de mantenimiento o configuración.
- `ci`: Cambios en archivos de configuración de pipelines.
- `refactor`: Cambios en el código que no corrigen errores ni añaden funcionalidades.

## Definition of Done (DoD)
Una tarea se considera finalizada cuando:
1. El código cumple con las guías de estilo (Linting).
2. Se han implementado pruebas unitarias con una cobertura >= 70%.
3. La documentación técnica ha sido actualizada (`/docs`).
4. Los manifiestos de Kubernetes han sido actualizados (`/k8s`).
5. El Pull Request ha sido aprobado y mergeado.

![Vista de desarrollo](./diagrams/components.png "Vista de desarrollo")
