from pydantic import BaseModel, Field # type: ignore
from typing import List

class Requirement(BaseModel):
    intent: str
    kpis: List[str]
    dimensions: List[str]
    filters: List[str]
    time_range: str
    aggregation: str
    chart_hint: str