class Tracer:
def start_span(self, name):
return _NoOpSpan()


class _NoOpSpan:
def __enter__(self):
return self
def __exit__(self, exc_type, exc, tb):
pass