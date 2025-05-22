"""Makes 'incremental' a Python package and potentially exposes its contents."""

# Expose the main workflow class for easier importing
from geometor.seer.workflows.incremental.workflow import IncrementalWorkflow # Changed class name

__all__ = ["IncrementalWorkflow"] # Changed class name
