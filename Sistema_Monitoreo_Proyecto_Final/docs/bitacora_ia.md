# BITÁCORA DE USO, AUDITORÍA Y REFACTORIZACIÓN ASISTIDA POR IA

**Proyecto:** Sistema de monitoreo de microservicios con arquitectura en capas y notificaciones basadas en eventos  
**Asignatura:** IS294 - Arquitectura Cliente Servidor  
**Docente:** ING. Oscar Andrés Sierra Jaramillo  
**Integrantes:** Luis Fernando, Sebastian Aranzazu y John Alejandro Berrio

## 1. Objetivo de la bitácora

Registrar el uso de la Inteligencia Artificial como herramienta de asistencia durante el análisis, diseño, implementación, revisión y mejoramiento del sistema de monitoreo de microservicios.

La IA se utilizó como apoyo para analizar código, proponer estructuras, explicar patrones de diseño, identificar posibles problemas y orientar la implementación de pruebas.

El equipo mantuvo la responsabilidad de revisar las propuestas, comprender los cambios y verificar los resultados mediante la ejecución del programa y las pruebas automatizadas.

**Nota metodológica:** las solicitudes que aparecen a continuación son resúmenes fieles de las actividades y consultas realizadas durante el desarrollo. No se presentan como transcripciones literales de prompts.

## 2. Registro de consultas y auditorías realizadas

### Registro 1. Análisis del proyecto original

**Solicitud realizada a la IA:** analizar el proyecto de monitoreo existente, comprender su estructura y determinar cómo mejorarlo sin comenzar un sistema completamente diferente.

**Apoyo recibido:** revisión de la organización original y explicación de las responsabilidades de sus componentes.

**Auditoría del equipo:** se identificaron problemas de distribución de responsabilidades, dependencias concretas entre componentes y oportunidades para mejorar la integración de las métricas.

**Decisión tomada:** conservar el proyecto anterior como referencia y guardar su archivo principal como `docs/main_original.py`. Se decidió desarrollar una estructura por capas, manteniendo la trazabilidad del proceso.

**Resultado:** se establecieron las bases de la nueva arquitectura y se conservaron los archivos anteriores para comparar la implementación.

### Registro 2. Selección del estilo arquitectónico

**Solicitud realizada a la IA:** proponer una organización que permitiera separar responsabilidades y mantener límites claros entre los componentes.

**Apoyo recibido:** orientación para estructurar el proyecto en presentación, aplicación, dominio e infraestructura.

**Auditoría del equipo:** se verificó que la organización propuesta correspondiera a un estilo arquitectónico reconocible y que no se mezclaran las responsabilidades de las diferentes capas.

**Decisión tomada:** utilizar arquitectura en capas como estilo arquitectónico principal. Los eventos se manejan dentro del proceso mediante un despachador en memoria; no se incorporó un broker distribuido.

**Resultado:** creación de los directorios `presentation`, `application`, `domain` e `infrastructure`.

### Registro 3. Reorganización de responsabilidades y aplicación de SRP

**Solicitud realizada a la IA:** revisar las responsabilidades de las clases y mejorar la separación entre el monitoreo, la configuración y las notificaciones.

**Apoyo recibido:** recomendaciones de separación de componentes y uso de servicios y abstracciones.

**Auditoría del equipo:** se revisó que el servicio de monitoreo no asumiera directamente las responsabilidades de cada canal de notificación. También se separó la configuración de las reglas de evaluación y de la infraestructura.

**Decisión tomada:** implementar un servicio de aplicación para coordinar el monitoreo, modelos en el dominio y observadores independientes para las notificaciones.

**Resultado:** las responsabilidades quedaron distribuidas en componentes como `MonitoringService`, `MonitoringConfig`, `AlertEvent` y las implementaciones de `AlertObserver`.

### Registro 4. Inversión de dependencias e interfaces

**Solicitud realizada a la IA:** mejorar el desacoplamiento entre el servicio de monitoreo y las implementaciones concretas.

**Apoyo recibido:** propuesta de trabajar con contratos o interfaces para las dependencias principales.

**Auditoría del equipo:** se comprobó que depender directamente de una implementación concreta dificultaría sustituir componentes y probarlos de forma independiente.

**Decisión tomada:** crear las abstracciones `MonitoringAPI`, `AlertObserver` y `EventBus`.

**Resultado:** `MonitoringService` recibe sus dependencias mediante contratos. El despachador y las implementaciones concretas se conectan desde `main.py`.

### Registro 5. Implementación del patrón Adapter

**Solicitud realizada a la IA:** analizar cómo integrar la fuente de métricas anterior con la interfaz requerida por el nuevo servicio.

**Apoyo recibido:** orientación para implementar un adaptador entre la API heredada y el contrato de monitoreo.

**Auditoría del equipo:** se verificó que la fuente anterior entregaba los datos mediante una estructura diferente de la requerida por el servicio. También se revisó la necesidad de validar los valores recibidos.

**Decisión tomada:** implementar `LegacyMonitoringAdapter` para adaptar los datos y validar su estructura, sus claves y sus valores numéricos.

**Resultado:** el servicio puede trabajar mediante `MonitoringAPI` sin depender de los detalles internos de la fuente anterior.

### Registro 6. Implementación del patrón Observer

**Solicitud realizada a la IA:** diseñar un mecanismo de notificación que permitiera distribuir alertas a diferentes canales sin acoplarlos al servicio de monitoreo.

**Apoyo recibido:** propuesta de utilizar un despachador de eventos y observadores que compartieran un contrato.

**Auditoría del equipo:** se revisó que los observadores pudieran registrarse y retirarse, que no se duplicaran las suscripciones y que un fallo individual no detuviera necesariamente las demás notificaciones.

**Decisión tomada:** implementar `EventDispatcher`, `EventBus` y `AlertObserver`, junto con los observadores Email, Slack, SMS y Teams.

**Resultado:** los eventos se distribuyen a los observadores registrados. El despachador utiliza una copia de la colección durante la publicación y maneja las excepciones de cada observador de forma individual.

**Limitación identificada:** los canales muestran notificaciones simuladas en consola y no realizan envíos reales a servicios externos.

### Registro 7. Implementación del patrón Strategy

**Solicitud realizada a la IA:** permitir que el sistema utilizara diferentes reglas para comparar los valores de las métricas con sus umbrales.

**Apoyo recibido:** orientación para utilizar una estrategia abstracta y distintas implementaciones concretas.

**Auditoría del equipo:** se revisó que una comparación de mayor que no es equivalente a una comparación de mayor o igual que. Se consideró importante representar ambas reglas de forma independiente.

**Decisión tomada:** crear `ThresholdStrategy`, `GreaterThanThresholdStrategy` y `GreaterThanOrEqualThresholdStrategy`.

**Resultado:** el servicio puede utilizar diferentes reglas mediante el mismo contrato, sin incorporar un bloque condicional grande para seleccionar el comportamiento.

### Registro 8. Implementación del patrón Facade

**Solicitud realizada a la IA:** simplificar el acceso a las funcionalidades internas del sistema.

**Apoyo recibido:** propuesta de utilizar una fachada para coordinar las operaciones principales.

**Auditoría del equipo:** se verificó que la fachada facilitara el uso del sistema sin sustituir las responsabilidades del servicio de monitoreo ni del despachador.

**Decisión tomada:** implementar `MonitoringFacade`, que facilita la administración de observadores y la ejecución del monitoreo.

**Resultado:** se dispone de una interfaz de aplicación simplificada para utilizar los componentes internos.

**Observación técnica:** la fachada utiliza `MonitoringService` como dependencia concreta de la capa de aplicación y trabaja con la abstracción `EventBus`. El equipo decidió mantener esta coordinación sin crear una interfaz artificial adicional.

### Registro 9. Validación y pruebas automatizadas

**Solicitud realizada a la IA:** revisar los comportamientos de los componentes y orientar la construcción de pruebas automatizadas.

**Apoyo recibido:** sugerencias de escenarios de prueba para configuración, adaptador, eventos, estrategias, monitoreo e inversión de dependencias.

**Auditoría del equipo:** se revisaron los escenarios para comprobar no solamente la ejecución normal, sino también validaciones incorrectas, condiciones de umbral y fallos individuales de observadores.

**Decisión tomada:** implementar pruebas con `unittest` y ejecutar la suite completa después de las modificaciones.

**Resultado:** se alcanzó una suite final de 22 pruebas automatizadas ejecutadas correctamente.

**Evidencia:** `evidencias/E_41_suite_completa_22_pruebas.png`.

### Registro 10. Auditoría de la inversión de dependencias

**Solicitud realizada a la IA:** analizar si el servicio de monitoreo dependía de abstracciones y si podía utilizar una implementación alternativa del bus de eventos.

**Apoyo recibido:** orientación para comprobar la sustituibilidad de la dependencia mediante una implementación de prueba.

**Auditoría del equipo:** se comprobó que la dependencia debía aceptar otro componente que cumpliera el contrato `EventBus`, sin requerir un `EventDispatcher` concreto.

**Decisión tomada:** implementar una prueba con `RecordingEventBus`.

**Resultado:** la prueba `test_service_accepts_alternative_event_bus` verifica que el servicio puede utilizar una implementación alternativa del contrato.

**Evidencia:** `evidencias/E_40_prueba_dip_lsp.png` y `evidencias/E_41_suite_completa_22_pruebas.png`.

### Registro 11. Actualización del diagrama UML

**Solicitud realizada a la IA:** revisar el diagrama UML para que representara fielmente la arquitectura y las clases finales.

**Apoyo recibido:** orientación para representar las interfaces, implementaciones y relaciones entre los componentes.

**Auditoría del equipo:** se detectó la necesidad de incluir explícitamente las dos estrategias concretas en el diagrama para que coincidiera con el código implementado.

**Decisión tomada:** actualizar `docs/uml.md` incorporando `GreaterThanThresholdStrategy` y `GreaterThanOrEqualThresholdStrategy`, además de las relaciones entre las capas y los patrones.

**Resultado:** diagrama actualizado y visualizado correctamente en Visual Studio Code.

**Evidencia:** `evidencias/E_42_diagrama_uml_actualizado.png`.

### Registro 12. Revisión crítica del intervalo de monitoreo

**Solicitud realizada a la IA:** comprobar si el parámetro `monitoring_interval` controlaba una ejecución periódica del monitoreo.

**Apoyo recibido:** orientación para buscar las referencias del parámetro, los mecanismos de espera y los ciclos de repetición en el proyecto.

**Auditoría del equipo:** se ejecutó una búsqueda en todos los archivos Python. Se comprobó que `monitoring_interval` aparece en la configuración de dominio, en la configuración anterior y en las pruebas, pero no se utiliza para repetir el monitoreo.

**Decisión tomada:** no presentar el intervalo de 60 segundos como funcionalidad activa. Se conserva como parámetro validado y se documenta que la ejecución actual realiza una revisión por invocación.

**Resultado:** se identificó una limitación real del sistema, evitando afirmar una funcionalidad que no está implementada.

## 3. Resumen de las decisiones técnicas del equipo

| Aspecto auditado | Decisión del equipo |
|---|---|
| Estilo arquitectónico | Mantener arquitectura en capas |
| Responsabilidades | Separar presentación, aplicación, dominio e infraestructura |
| Dependencias | Utilizar interfaces y contratos |
| Métricas | Integrar CPU y memoria mediante una interfaz |
| Compatibilidad | Utilizar Adapter para la fuente anterior |
| Notificaciones | Distribuir eventos mediante Observer |
| Umbrales | Aplicar Strategy con dos reglas |
| Acceso al sistema | Simplificar operaciones mediante Facade |
| Fallos de observadores | Manejar errores individualmente |
| Pruebas | Validar los componentes con unittest |
| UML | Actualizarlo para coincidir con las clases finales |
| Intervalo | Documentarlo como parámetro validado, no como ejecución periódica |

## 4. Alcance y limitaciones reconocidas

El equipo reconoce que el sistema utiliza valores simulados de CPU y memoria. Los canales Email, Slack, SMS y Teams muestran notificaciones en consola, sin integraciones externas reales.

También se reconoce que el despachador de eventos opera en memoria, dentro del proceso, y que el parámetro `monitoring_interval` no controla actualmente una ejecución periódica.

Estas limitaciones fueron consideradas para evitar presentar capacidades que no forman parte de la implementación entregada.

## 5. Evidencias relacionadas

- `docs/main_original.py`: referencia del código anterior.
- `docs/uml.md`: definición del diagrama UML actualizado.
- `evidencias/E_40_prueba_dip_lsp.png`: evidencia de la prueba de inversión de dependencias.
- `evidencias/E_41_suite_completa_22_pruebas.png`: resultado de la suite final.
- `evidencias/E_42_diagrama_uml_actualizado.png`: diagrama UML actualizado.
- `tests/`: pruebas automatizadas de los componentes.

## 6. Conclusión de la auditoría

La Inteligencia Artificial se utilizó como herramienta de apoyo durante el desarrollo, pero las decisiones de diseño y la aceptación de los cambios se realizaron mediante revisión técnica del equipo.

El proceso incluyó análisis del código existente, reorganización de responsabilidades, implementación de abstracciones, aplicación de patrones de diseño, revisión de dependencias, elaboración de pruebas y actualización del diagrama UML.

El equipo no asumió que todas las propuestas fueran correctas por defecto. Se evaluaron los resultados, se conservaron las limitaciones identificadas y se verificó el comportamiento mediante pruebas automatizadas.

La responsabilidad final sobre la comprensión, integración y defensa del proyecto corresponde a los integrantes.