import importlib
import pkgutil
import tools
from core.base_tool import BaseTool


def discover_tools() -> list[BaseTool]:
    discovered = []
    for module_info in pkgutil.iter_modules(tools.__path__):
        try:
            ui_module = importlib.import_module(f"tools.{module_info.name}.ui")
        except ModuleNotFoundError:
            continue
        for attr in vars(ui_module).values():
            if (
                isinstance(attr, type)
                and issubclass(attr, BaseTool)
                and attr is not BaseTool
            ):
                discovered.append(attr())
                break
    return sorted(discovered, key=lambda t: (t.category, t.name))
