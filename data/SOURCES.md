# Fuentes de datos

## Fuente principal

Ministerio de Desarrollo Agrario y Riego del Perú (MIDAGRI) / Sistema Integrado de Estadística Agraria (SIEA).

Colección utilizada: anuarios de Producción Agrícola correspondientes a 2017–2023.

Página institucional de referencia:
https://www.gob.pe/institucion/midagri/informes-publicaciones/2730325-compendio-anual-de-produccion-agricola

## Variables utilizadas

Para cacao se integraron principalmente:

- región;
- año y mes;
- producción mensual en toneladas;
- precio en chacra cuando la tabla anual permitió su extracción consistente;
- total anual como control de consistencia;
- archivo y hoja de procedencia.

## Decisiones de integración

1. Los archivos fuente no se sobrescriben.
2. Se conserva `region_raw` y se utiliza `region` como etiqueta canónica.
3. La selección de series activas se define únicamente con 2017–2021.
4. 2022 se reserva para validación preliminar.
5. 2023 permanece fuera de muestra para el test final preliminar.
6. Los totales mensuales se contrastan con los totales anuales como control de integración.

## Licencia y atribución

Los datos originales mantienen las condiciones de la fuente oficial. Los CSV de este repositorio son derivados para fines académicos y deben citar a MIDAGRI/SIEA.
