from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

@dataclass(frozen=True)
class AlertEvent:
    """
    Representa un evento generado cuando una métrica
    supera el umbral permitido.
    """

    service_name: str
    metric: str
    value: float
    threshold: float

    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    occurred_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
