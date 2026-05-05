
class SimplePublisher:
    async def publish(self, topic, event):
        print(f"[FAKE PUBLISH] {topic} → {event}")

def get_publisher():
    return SimplePublisher()

def get_repo():
    return None  # or in-memory stub for now
