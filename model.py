# from typing import 


class Task:
    def __init__(self, 
                 id: int, 
                 title: str, 
                 description: str,
                 category: str,
                 priority: str,
                 status: bool):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = status