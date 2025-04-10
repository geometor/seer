"""Makes 'default' a Python package and potentially exposes its contents."""

# Expose the main workflow class for easier importing
from .workflow import DefaultWorkflow

__all__ = ["DefaultWorkflow"]
