class ToolError(Exception):
    """Base for anything a tool wants to surface to the user."""


class ToolAPIError(ToolError):
    """External API call failed or returned something unparseable."""
