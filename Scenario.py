from __future__ import annotations
import CrossComponents

class Scenario:
    def __init__(self, flow):
        self.components = CrossComponents.components
        self.logger = self.components.get_logger()
        self.flow = flow
        self.FLOW = self.build()

    def build(self):
        x = 5

class Node:
    def __init__(self, body: dict, prev: Node, next: Node):
        self.body = body
        self.prev = prev
        self.next = next

    def build(self) -> Node:
        x = 5

    def do(self):



        # Сохраняем стате каждый раз
        return