from .context import swarmclientpy

def test_add():
    assert swarmclientpy.loop.add(1, 3) == 4
