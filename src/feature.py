FILE agentic_workflow/domain/models.py
```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum, auto
from datetime import datetime


class WorkflowStatus(Enum):
    """Enumeration of possible statuses for a workflow."""
    PENDING = auto()
    RUNNING = auto()
    COMPLETED = auto()
    FAILED = auto()
    CANCELLED = auto()


@dataclass(frozen=True)
class Task:
    """
    Represents a single task in a workflow.

    Attributes:
        id: Unique identifier for the task.
        name: Human-readable name of the task.
        inputs: Inputs required for task execution.
        outputs: Outputs produced by task after execution.
        status: Current status of the task.
        created_at: Timestamp when the task was created.
        started_at: Timestamp when the task execution started.
        finished_at: Timestamp when the task finished execution.
    """
    id: str
    name: str
    inputs: Dict[str, Any] = field(default_factory=dict)
    outputs: Dict[str, Any] = field(default_factory=dict)
    status: WorkflowStatus = WorkflowStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None


@dataclass(frozen=True)
class Workflow:
    """
    Represents a workflow consisting of multiple tasks.

    Attributes:
        id: Unique identifier for the workflow.
        name: Human-readable name of the workflow.
        tasks: List of tasks in the workflow, ordered by execution sequence.
        status: Current status of the workflow.
        created_at: Timestamp when the workflow was created.
        started_at: Timestamp when the workflow execution started.
        finished_at: Timestamp when the workflow finished execution.
        metadata: Optional additional metadata for extensibility.
    """
    id: str
    name: str
    tasks: List[Task] = field(default_factory=list)
    status: WorkflowStatus = WorkflowStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
```
