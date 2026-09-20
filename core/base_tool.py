from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str = "Unnamed tool"
    icon: str = ":materials/cog:"
    category: str = "General"

    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError
