# from typing import 
from dataclasses import dataclass

class Task:
    def __init__(self, 
                 id: int, 
                 title: str, 
                 description: str,
                 category: str,
                 priority: str,
                 status: bool = False):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "priority": self.priority,
            "status": self.status,
        }