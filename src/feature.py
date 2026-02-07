FILE agentic_workflow/metrics/collector.py
```python
from typing import Dict, Any
from time import time


class MetricsCollector:
    """
    Collects and stores runtime metrics of workflows and tasks.
    Designed to be lightweight and thread-safe for integration into orchestration framework.
    """

    def __init__(self) -> None:
        self._metrics: Dict[str, Dict[str, Any]] = {}

    def record_metric(self, entity_id: str, metric_name: str, value: Any) -> None:
        """
        Record a metric value for a given entity (workflow or task).

        Args:
            entity_id: Unique identifier of the entity.
            metric_name: Key name of the metric to record.
            value: Value of the metric to store.
        """
        if entity_id not in self._metrics:
            self._metrics[entity_id] = {}

        self._metrics[entity_id][metric_name] = {
            "value": value,
            "timestamp": time()
        }

    def increment_metric(self, entity_id: str, metric_name: str, increment: int = 1) -> None:
        """
        Increment a numeric metric for a given entity by a specified amount.

        Args:
            entity_id: Unique identifier of the entity.
            metric_name: Key of the metric to increment.
            increment: Amount to add.
        """
        if entity_id not in self._metrics:
            self._metrics[entity_id] = {}

        if metric_name not in self._metrics[entity_id]:
            self._metrics[entity_id][metric_name] = {"value": 0, "timestamp": time()}

        current_value = self._metrics[entity_id][metric_name]["value"]
        self._metrics[entity_id][metric_name]["value"] = current_value + increment
        self._metrics[entity_id][metric_name]["timestamp"] = time()

    def get_metrics(self, entity_id: str) -> Dict[str, Any]:
        """
        Retrieve all metrics recorded for a given entity.

        Args:
            entity_id: Unique identifier of the entity.

        Returns:
            Dict of metric_name to metric details (value, timestamp).
        """
        return self._metrics.get(entity_id, {}).copy()

    def reset_metrics(self, entity_id: str) -> None:
        """
        Reset all metrics for a given entity.

        Args:
            entity_id: Unique identifier of the entity.
        """
        self._metrics[entity_id] = {}

    def all_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Getter for all collected metrics.

        Returns:
            Entire metrics dictionary.
        """
        return self._metrics.copy()
```
