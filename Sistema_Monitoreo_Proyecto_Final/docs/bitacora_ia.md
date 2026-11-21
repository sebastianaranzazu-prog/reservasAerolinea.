# BITÁCORA DE USO, AUDITORÍA Y REFACTORIZACIÓN ASISTIDA POR IA

**Proyecto:** Sistema de monitoreo de microservicios con arquitectura en capas y notificaciones basadas en eventos
**Asignatura:** IS294 – Arquitectura Cliente Servidor
**Docente:** ING. Oscar Andrés Sierra Jaramillo
**Integrantes:** Luis Fernando, Sebastian Aranzazu y John Alejandro Berrio
**Repositorio:** `sebastianaranzazu-prog/reservasAerolinea.`
**Rama de trabajo de la actualización:** `actualizacion-sistema-monitoreo`
**Integración final:** rama `main`, mediante el commit de merge `87cdf26`
**Último commit registrado en la entrega:** `11f8805` (incorpora la evidencia final E_43)

---

## 1. Propósito y alcance de la bitácora

Esta bitácora registra cómo se utilizó la Inteligencia Artificial como asistente de análisis y programación durante el mejoramiento del sistema de monitoreo. Su propósito no es atribuirle a la IA la autoría total del proyecto, sino dejar trazabilidad de las consultas, las propuestas evaluadas, los hallazgos técnicos, las decisiones tomadas por el equipo y las verificaciones realizadas.

La IA se utilizó como apoyo para analizar la estructura existente, estudiar alternativas de arquitectura, orientar la aplicación de principios SOLID y patrones GoF, revisar componentes y proponer escenarios de prueba. El equipo mantuvo la responsabilidad de revisar las propuestas, decidir cuáles eran adecuadas, adaptar la implementación y comprobar el resultado.

### Nota sobre la fidelidad de los registros

Los registros de consulta de esta bitácora están redactados como **síntesis fieles de los temas y solicitudes trabajados**, no como transcripciones literales de cada mensaje enviado en las conversaciones anteriores. No se presentan frases reconstruidas como citas textuales. Cuando se disponga de capturas o exportaciones de las conversaciones originales, pueden agregarse como anexo para reforzar la trazabilidad de los prompts.

También se distingue entre:
- **Hallazgo del proyecto original:** problema encontrado al revisar el código que ya existía.
- **Propuesta asistida por IA:** alternativa o explicación recibida durante el trabajo.
- **Decisión del equipo:** cambio que se decidió aplicar después de revisar la propuesta.
- **Validación:** evidencia que permite comprobar el comportamiento de la versión final.

No todos los hallazgos descritos fueron necesariamente errores producidos por la IA. Algunos pertenecían al proyecto heredado y otros fueron limitaciones detectadas durante la revisión crítica de la solución.

---

## 2. Registro de consultas y decisiones

### Registro 1. Análisis del proyecto heredado

**Necesidad consultada a la IA — síntesis, no cita literal:**
Analizar el sistema de monitoreo desarrollado anteriormente, explicar cómo se relacionaban sus componentes y proponer una ruta de mejoramiento que reutilizara el trabajo existente en lugar de iniciar un sistema sin relación con él.

**Apoyo recibido:**
Orientación para revisar la estructura, identificar responsabilidades y separar los elementos que podían conservarse como referencia de los que necesitaban reorganización.

**Auditoría realizada por el equipo:**
Se revisó el contenido de los directorios anteriores: `adapters`, `alerts`, `config`, `facade` y `monitoring`. Se encontró que la solución estaba concentrada en componentes con responsabilidades mezcladas y que la integración de CPU y memoria no tenía una separación suficientemente clara.

**Decisión del equipo:**
Conservar el proyecto previo como referencia, guardar su archivo principal en `docs/main_original.py` y construir la versión mejorada en una estructura nueva.

**Resultado y trazabilidad:**
Se mantuvo el código anterior como evidencia del punto de partida y se creó la organización por capas. La carpeta original y el historial del repositorio permiten comparar la estructura heredada con la versión nueva.

### Registro 2. Selección y aplicación de arquitectura en capas

**Necesidad consultada a la IA — síntesis, no cita literal:**
Proponer una estructura para separar presentación, coordinación de casos de uso, reglas del dominio e implementaciones técnicas, evitando dependencias cruzadas innecesarias.

**Apoyo recibido:**
Orientación para dividir el sistema en `presentation`, `application`, `domain` e `infrastructure`, y ubicar en cada capa los componentes correspondientes.

**Auditoría realizada por el equipo:**
Se comprobó que el estilo elegido fuera reconocible y que las dependencias siguieran una dirección coherente. Se revisó que el dominio no necesitara importar detalles de presentación o infraestructura.

**Decisión del equipo:**
Adoptar arquitectura en capas como estilo arquitectónico principal. El mecanismo de eventos se mantiene dentro del proceso mediante un despachador en memoria; no se presenta como un broker distribuido.

**Resultado y trazabilidad:**
La estructura final contiene:
- `presentation/`: interfaz de línea de comandos.
- `application/`: servicio, fachada, puertos y despachador.
- `domain/`: modelos y estrategias.
- `infrastructure/`: adaptador, fuente de métricas y observadores concretos.

### Registro 3. Auditoría de la responsabilidad de CPU y memoria

**Necesidad consultada a la IA — síntesis, no cita literal:**
Revisar cómo integrar las métricas de CPU y memoria y mantener la evaluación de ambas dentro de una responsabilidad de monitoreo bien definida.

**Hallazgo comprobado en el proyecto original:**
En la versión heredada, `check_memory` aparecía dentro de `config/monitoring_config.py`, aunque su implementación utilizaba referencias como `self.config`, `self.notify` y lógica de notificación propias del monitor, no de una clase de configuración. Esto mezclaba responsabilidades y ubicaba la operación en una clase que no era su lugar natural.

Además, el monitor anterior concentraba la comprobación de CPU en `MicroserviceMonitor`, mientras que la lógica de memoria no estaba integrada de forma coherente en el servicio de monitoreo.

**Auditoría realizada por el equipo:**
Se identificó que la configuración debía limitarse a almacenar y validar parámetros, mientras que la consulta y evaluación de métricas correspondían al servicio de aplicación.

**Decisión del equipo:**
Separar la configuración en `MonitoringConfig` y llevar la evaluación de CPU y memoria a `MonitoringService`, que utiliza una única operación privada de evaluación para ambas métricas.

**Resultado y trazabilidad:**
`MonitoringService.check_service()` consulta CPU y memoria mediante `MonitoringAPI`; `_evaluate_metric()` aplica la estrategia y publica el evento cuando corresponde. La suite incluye pruebas para el servicio y para la configuración.

### Registro 4. Auditoría y fortalecimiento del Adapter

**Necesidad consultada a la IA — síntesis, no cita literal:**
Adaptar la fuente de métricas heredada al contrato que necesita la nueva aplicación y comprobar que los datos entregados sean válidos.

**Hallazgo comprobado en el proyecto original:**
El adaptador anterior obtenía el diccionario de la API heredada y devolvía directamente `data["cpu_usage_percent"]`. Esa implementación no validaba previamente que la respuesta fuera un diccionario, que la clave existiera, que el dato fuera numérico o que estuviera dentro del rango porcentual esperado. El contrato anterior se enfocaba únicamente en CPU.

**Auditoría realizada por el equipo:**
Se consideró insuficiente trasladar directamente ese valor a la nueva arquitectura, especialmente porque la nueva aplicación también necesita consultar memoria.

**Decisión del equipo:**
Crear el contrato `MonitoringAPI` para CPU y memoria e implementar `LegacyMonitoringAdapter` en infraestructura. El adaptador verifica el tipo de respuesta, la presencia de la métrica, el tipo numérico —rechazando booleanos— y el rango de 0 a 100.

**Resultado y trazabilidad:**
La fuente heredada se conserva detrás del adaptador. El servicio depende de `MonitoringAPI` y no conoce el formato interno del diccionario legado. El comportamiento se comprueba con `tests/test_legacy_monitoring_adapter.py`.

### Registro 5. Aplicación del patrón Strategy y eliminación de una regla rígida

**Necesidad consultada a la IA — síntesis, no cita literal:**
Permitir que la regla para comparar una métrica con su umbral pueda cambiar sin reescribir el servicio de monitoreo ni acumular condiciones para seleccionar comportamientos.

**Hallazgo comprobado en el proyecto original:**
El monitor anterior contenía directamente la comparación de CPU con el umbral mediante una condición `if cpu_usage > threshold`. La regla estaba incorporada en el propio componente de monitoreo.

**Auditoría realizada por el equipo:**
Se determinó que la condición de comparación podía variar. Además, “mayor que” y “mayor o igual que” producen resultados distintos cuando el valor coincide exactamente con el umbral.

**Decisión del equipo:**
Definir el contrato abstracto `ThresholdStrategy` e implementar:
- `GreaterThanThresholdStrategy`, que evalúa `value > threshold`.
- `GreaterThanOrEqualThresholdStrategy`, que evalúa `value >= threshold`.

La estrategia concreta se selecciona al construir el sistema en `main.py`.

**Resultado y trazabilidad:**
`MonitoringService` invoca `self._strategy.evaluate(value, threshold)` y no incorpora la regla de comparación directamente. Las dos estrategias pueden utilizarse mediante el mismo contrato. Se agregaron pruebas para los comportamientos de ambas.

### Registro 6. Auditoría de Observer y tolerancia a fallos de observadores

**Necesidad consultada a la IA — síntesis, no cita literal:**
Organizar la distribución de alertas para que el servicio de monitoreo no tenga que conocer los detalles de Email, Slack, SMS o Teams, y estudiar cómo evitar que un fallo de un canal detenga toda la notificación.

**Hallazgo comprobado en el proyecto original:**
La implementación anterior mantenía los observadores dentro de `MicroserviceMonitor` y recorría directamente la colección para llamar a `update`. La lógica de monitoreo y el mecanismo de notificación estaban más unidos.

**Auditoría realizada por el equipo:**
Se identificó que convenía separar el contrato de publicación del despachador concreto. También se evaluó el caso en que un observador lance una excepción durante la publicación.

**Decisión del equipo:**
Crear `EventBus` y `AlertObserver` como contratos y `EventDispatcher` como implementación. En `publish()`, el despachador recorre una tupla de los observadores registrados y maneja individualmente las excepciones de cada observador.

**Resultado y trazabilidad:**
El servicio publica `AlertEvent` mediante `EventBus`. El despachador distribuye el evento a los observadores y registra los fallos individuales para continuar con los demás. Las pruebas están en `tests/test_event_dispatcher.py`; la evidencia del escenario de fallo del observador es `E_24_prueba_fallo_observador.png`.

### Registro 7. Inversión de dependencias y sustituibilidad

**Necesidad consultada a la IA — síntesis, no cita literal:**
Comprobar si el servicio principal depende de implementaciones concretas o de contratos y diseñar una prueba que demuestre que puede utilizar otra implementación compatible.

**Auditoría realizada por el equipo:**
Se revisó el constructor de `MonitoringService`, que recibe `MonitoringAPI`, `ThresholdStrategy`, `MonitoringConfig` y `EventBus`. También se comprobó que la fachada utiliza la abstracción `EventBus` para administrar observadores.

**Decisión del equipo:**
Mantener la creación de implementaciones concretas en el punto de composición (`main.py`) e incorporar una implementación alternativa de bus de eventos en las pruebas.

**Resultado y trazabilidad:**
La prueba `test_service_accepts_alternative_event_bus` verifica que el servicio admite un bus alternativo que cumple el contrato. Esta prueba respalda la aplicación de DIP y la posibilidad de sustituir la implementación. No se afirma que todas las dependencias del proyecto sean interfaces: `MonitoringFacade` recibe `MonitoringService` como dependencia concreta de la misma capa de aplicación.

### Registro 8. Responsabilidad de la Facade y composición de dependencias

**Necesidad consultada a la IA — síntesis, no cita literal:**
Simplificar el uso del sistema y separar la creación de componentes de la operación que solicita el monitoreo.

**Hallazgo comprobado en el proyecto original:**
La fachada anterior creaba directamente `MicroserviceMonitor`, los observadores y la API heredada, y también construía el adaptador. Esto concentraba en la fachada la creación y coordinación de muchos detalles concretos.

**Auditoría realizada por el equipo:**
Se concluyó que la composición de implementaciones debía quedar en el punto de entrada, mientras la fachada debía exponer una interfaz de uso más sencilla.

**Decisión del equipo:**
Construir las dependencias concretas en `main.py`, dentro de `build_facade()`. La fachada recibe `MonitoringService` y `EventBus`, ofrece operaciones para agregar o retirar observadores y delega el monitoreo al servicio.

**Resultado y trazabilidad:**
`main.py` funciona como raíz de composición. `MonitoringFacade` simplifica el acceso sin duplicar la lógica de monitoreo ni sustituir al servicio.

### Registro 9. Validación del comportamiento mediante pruebas

**Necesidad consultada a la IA — síntesis, no cita literal:**
Identificar escenarios de prueba para comprobar tanto el funcionamiento normal como los casos límite de configuración, adaptación, publicación de eventos y evaluación de umbrales.

**Auditoría realizada por el equipo:**
Se revisó que las pruebas no se limitaran a comprobar que el programa arrancara. Se incluyeron validaciones de datos, suscripciones, eliminación de observadores, errores individuales y sustitución del bus de eventos.

**Decisión del equipo:**
Implementar pruebas automatizadas con `unittest` y ejecutar la suite después de integrar los cambios.

**Resultado y trazabilidad:**
La suite final contiene 22 pruebas y terminó con `OK`. La evidencia es `evidencias/E_41_suite_completa_22_pruebas.png`. Las pruebas están distribuidas en:
- `test_event_dispatcher.py`
- `test_legacy_monitoring_adapter.py`
- `test_monitoring_config.py`
- `test_monitoring_service.py`
- `test_dependency_inversion.py`

La ejecución comprobada fue:

```text
Ran 22 tests
OK
```

### Registro 10. Auditoría del diagrama UML

**Necesidad consultada a la IA — síntesis, no cita literal:**
Revisar que el diagrama UML representara las clases, interfaces, capas y patrones de la implementación real.

**Hallazgo de revisión:**
El diagrama debía representar de forma explícita las dos estrategias concretas que estaban implementadas, no solamente la abstracción.

**Decisión del equipo:**
Actualizar `docs/uml.md` para incluir `GreaterThanThresholdStrategy` y `GreaterThanOrEqualThresholdStrategy`, junto con sus relaciones con `ThresholdStrategy` y los demás componentes.

**Resultado y trazabilidad:**
El diagrama actualizado se visualizó en Visual Studio Code y se guardó como `evidencias/E_42_diagrama_uml_actualizado.png`.

### Registro 11. Detección de una limitación no corregida: intervalo de monitoreo

**Necesidad de auditoría:**
Comprobar si `monitoring_interval = 60` representaba una ejecución periódica real o si solamente estaba definido en la configuración.

**Auditoría realizada por el equipo:**
Se buscaron las referencias a `monitoring_interval`, `sleep`, ciclos de repetición y llamadas al servicio. Se encontró que el parámetro se define y valida en `MonitoringConfig`, pero no se utiliza para programar una ejecución periódica. La interfaz actual solicita el nombre del servicio y ejecuta una comprobación por invocación.

**Decisión del equipo:**
No afirmar que el sistema monitorea automáticamente cada 60 segundos. Se conserva el parámetro como configuración validada y se documenta esta limitación. No se añadió un ciclo infinito de ejecución porque habría cambiado el alcance y requeriría pruebas adicionales.

**Resultado:**
Se evitó presentar una funcionalidad no implementada como si estuviera activa. Esta decisión constituye una evidencia de revisión crítica y de reconocimiento de límites.

---

## 3. Matriz consolidada de auditoría técnica

| Componente o aspecto | Hallazgo de la versión anterior / riesgo revisado | Decisión aplicada en la versión mejorada | Evidencia |
|---|---|---|---|
| Arquitectura | Responsabilidades distribuidas en carpetas antiguas sin límites de capas suficientemente claros | Separación en presentación, aplicación, dominio e infraestructura | Estructura del proyecto y `docs/uml.md` |
| Memoria | `check_memory` estaba en la clase de configuración y utilizaba responsabilidades del monitor | Mover evaluación de CPU y memoria a `MonitoringService` | `monitoring_service.py`, pruebas del servicio |
| Adapter | Acceso directo a una clave del diccionario, sin validaciones completas y orientado a CPU | Validar estructura, clave, tipo y rango; adaptar CPU y memoria | `legacy_monitoring_adapter.py`, `test_legacy_monitoring_adapter.py` |
| Strategy | Regla de comparación integrada directamente en el monitor | Contrato abstracto y dos estrategias concretas | `threshold_strategy.py`, pruebas de estrategia |
| Observer | Publicación ligada al monitor y sin aislamiento suficiente de fallos individuales | `EventBus`, `AlertObserver` y `EventDispatcher` con manejo individual de excepciones | `event_dispatcher.py`, `E_24`, pruebas del despachador |
| DIP | Creación y uso de clases concretas en componentes de lógica | Inyección de contratos en `MonitoringService`; composición en `main.py` | `test_dependency_inversion.py`, `E_40` |
| Facade | La fachada anterior construía directamente varios componentes concretos | La fachada recibe servicio y bus; `main.py` compone implementaciones | `monitoring_facade.py`, `main.py` |
| UML | Faltaba representar explícitamente las dos estrategias concretas | Actualizar el diagrama para reflejar la implementación | `E_42_diagrama_uml_actualizado.png` |
| Intervalo | `monitoring_interval` estaba definido, pero no controlaba una repetición periódica | Reconocer y documentar la limitación; no afirmar ejecución automática | Búsqueda del parámetro y código actual |
| Pruebas | Se necesitaba comprobar la integración y los casos de error | Suite automatizada final de 22 pruebas | `E_41_suite_completa_22_pruebas.png` |

---

## 4. Qué se aceptó, qué se ajustó y qué no se implementó

### Propuestas o enfoques aceptados

- Separar el sistema en cuatro capas.
- Utilizar contratos para monitoreo, publicación de eventos y observadores.
- Aplicar Adapter para mantener la compatibilidad con la fuente heredada.
- Aplicar Strategy para intercambiar reglas de evaluación.
- Aplicar Observer para distribuir las alertas.
- Utilizar Facade para simplificar el acceso al caso de uso.
- Probar la sustituibilidad de `EventBus` mediante una implementación alternativa.

### Propuestas o enfoques ajustados tras la revisión

- La integración de memoria se reorganizó para que no quedara en la clase de configuración.
- El adaptador se amplió para validar los datos y cubrir CPU y memoria.
- La comparación de umbrales se separó en dos estrategias porque `>` y `>=` no significan lo mismo.
- La distribución de eventos se reforzó para aislar los errores individuales de los observadores.
- La fachada dejó de crear directamente todo el conjunto de componentes; la composición se trasladó a `main.py`.

### Funcionalidades que no se deben afirmar

- No se implementó Factory Method.
- No se utiliza RabbitMQ, Kafka ni un broker distribuido.
- Las métricas no proceden de servidores reales: son simuladas.
- Email, Slack, SMS y Teams no realizan envíos reales: muestran notificaciones en consola.
- `monitoring_interval` no implementa una ejecución periódica.

---

## 5. Evidencias y trazabilidad del trabajo

Las siguientes evidencias permiten relacionar las decisiones técnicas con el desarrollo:

| Evidencia | Qué demuestra |
|---|---|
| `E_01_programa_original.png` | Punto de partida del proyecto |
| `E_14_fuente_metricas.png` | Fuente de métricas |
| `E_18_fuente_metricas_cpu_memoria.png` | Integración de las dos métricas |
| `E_19_integracion_cpu_memoria_cuatro_canales.png` | Distribución de eventos de CPU y memoria |
| `E_24_prueba_fallo_observador.png` | Manejo de fallo individual de un observador |
| `E_36_prueba_dos_estrategias.png` | Diferencia entre las estrategias |
| `E_40_prueba_dip_lsp.png` | Prueba de dependencia y sustituibilidad |
| `E_41_suite_completa_22_pruebas.png` | Resultado final de pruebas |
| `E_42_diagrama_uml_actualizado.png` | UML actualizado |
| `E_43_suite_final_22_pruebas.png` | Captura final de la suite de 22 pruebas, incorporada a `main` en el commit `11f8805` |

Además, el proyecto conserva `docs/main_original.py` como referencia de la versión anterior y `docs/uml.md` como fuente del diagrama.

---

## 6. Participación y responsabilidad del equipo

La IA fue utilizada como apoyo, no como sustituto de la comprensión del equipo. Las decisiones de arquitectura, la selección de patrones, la revisión de componentes, la integración de cambios y la comprobación de resultados fueron responsabilidad de los integrantes.

Durante la defensa, los integrantes deben poder explicar:
- Por qué se eligió arquitectura en capas.
- Qué responsabilidad tiene cada componente.
- Cómo se aplican los principios SOLID.
- Qué problema resuelve cada patrón GoF.
- Qué limitaciones fueron detectadas.
- Qué pruebas demuestran el comportamiento implementado.

---

## 7. Conclusión de la auditoría

El uso de Inteligencia Artificial permitió acelerar el análisis y la exploración de alternativas, pero las propuestas no se aceptaron sin revisión. El equipo contrastó la organización del código con el estilo arquitectónico elegido, identificó responsabilidades mal ubicadas en la versión heredada, fortaleció la validación del adaptador, separó las reglas de umbral mediante Strategy, desacopló la publicación de eventos mediante contratos y añadió pruebas automatizadas.

La auditoría también permitió reconocer una limitación real: el parámetro `monitoring_interval` no controla una ejecución periódica. En lugar de afirmar una capacidad inexistente, el equipo decidió documentarla como limitación.

La evidencia de 22 pruebas aprobadas, el diagrama UML actualizado, el código organizado en capas y la conservación de la versión original permiten demostrar el proceso de mejoramiento. La responsabilidad final sobre el código y su defensa corresponde a los integrantes del equipo.

---

## 8. Anexo recomendado: prompts originales

Esta bitácora contiene síntesis de las solicitudes y no transcripciones literales. Para fortalecer el criterio de “bitácora detallada de prompts”, se pueden anexar capturas auténticas de los mensajes originales de las conversaciones de desarrollo, si todavía están disponibles.

Las capturas deben mostrar el mensaje del estudiante y, cuando sea útil, la respuesta de IA que se sometió a revisión. No deben editarse para aparentar que una síntesis es una cita literal.

La evidencia `E_43_suite_final_22_pruebas.png` ya está asignada a la captura final de la suite de pruebas; por tanto, no debe reutilizarse su nombre para capturas de prompts. Si se recuperan conversaciones originales y se decide capturarlas, deben recibir identificadores nuevos y consecutivos a partir de la última evidencia existente, verificando primero el inventario real.

**Importante:** no se deben crear capturas ficticias ni afirmar que se guardaron si no existen. La ausencia de capturas originales debe declararse con transparencia; las síntesis de esta bitácora no sustituyen los prompts literales.
