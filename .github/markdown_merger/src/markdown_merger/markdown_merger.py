class MarkdownMerger:
    def __init__(self):
        self.content: list[str] = []
        return
    
    def feed(self, markdown: str):
        self.content.append(markdown)
    
    def out(self) -> str:
        return "\n".join(self.content)
