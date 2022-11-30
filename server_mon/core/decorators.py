

def static__init__(cls):
    if getattr(cls, static__init__.__name__, None):
        cls.static__init__()
    return cls
