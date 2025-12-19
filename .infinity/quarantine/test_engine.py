from echo_luminea.engine import EchoEngine

def test_engine_starts(capsys):
    engine = EchoEngine()
    engine.start()
    captured = capsys.readouterr()
    assert "Echo Luminea Engine" in captured.out
