from abc import ABC, abstractmethod
from typing import List, Any, Dict, Callable

class Client(ABC):
    """
    Abstract base class for LLM clients.
    """

    @abstractmethod
    def generate_content(self, prompt: List[str], tools: List[Callable] = None) -> Any:
        """
        Generates content from the LLM based on the provided prompt.

        Parameters
        ----------
        prompt : List[str]
            The prompt to send to the model.
        tools : List[Callable], optional
            Optional tools or functions the model can use.

        Returns
        -------
        Any
            The model's response.
        """
        pass
