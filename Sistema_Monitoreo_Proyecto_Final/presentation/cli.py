def run(facade):
    """
    Interfaz de consola para ejecutar el monitoreo.
    """
    
    print("\n======================================")
    print(" SISTEMA DE MONITOREO DE MICROSERVICIOS")
    print("======================================")

    service_name = input(
        "\nIngrese el nombre del microservicio "
        "[payments-service]: "
    ).strip()

    if not service_name:
        service_name = "payments-service"

    print("\nIniciando monitoreo...\n")

    events = facade.monitor_service(service_name)

    print("\n======================================")
    print(" RESULTADO DEL MONITOREO")
    print("======================================")

    print(f"Servicio evaluado: {service_name}")
    print(f"Alertas generadas: {len(events)}")
