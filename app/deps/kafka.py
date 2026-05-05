from app.core.state import state


def get_publisher():
    return state.kafka_publisher


def get_repo():
    return None  # or in-memory stub for now


