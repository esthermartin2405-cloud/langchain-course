from typing import List

from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")