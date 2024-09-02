import datetime
import tempfile

import pytest

import komis.main


def test_read_komis_file():
    with tempfile.TemporaryDirectory() as wdir:
        message = f"test + {datetime.datetime.now()}"
        with open(f"{wdir}/test.komis", "w") as f:
            f.write(message)
        assert komis.main.read_komis_file(f"{wdir}/test.komis") == message


def test_read_komis_file_with_a_frame():
    with tempfile.TemporaryDirectory() as wdir:
        message = (
            "KOMIS-FILE\tSTART\nBEGIN-FRAME\nTYPE\t"
            + "SIMPLE-TEXT\nARGUMENT\tTEXT\tHello world!\nKOMIS-FILE\tEND"
        )
        with open(f"{wdir}/test.komis", "w") as f:
            f.write(message)
        message_read = komis.main.read_komis_file(f"{wdir}/test.komis")
        assert message_read == message
        p = list(komis.main.parse_komis_file(message_read))
        assert len(p) == 1
        for frame in p:
            assert frame
            assert set(frame.keys()) == {"args", "type"}
            assert set(frame["args"].keys()) == {"TEXT"}
            assert frame["type"] == "SIMPLE-TEXT"
            assert frame["args"]["TEXT"] == "Hello world!"


@pytest.mark.parametrize(
    "engine", ["DIALOGUE", "DIALOGUE-REVERSE", "SIMPLE-TEXT", "GAY", "DRAW-LOGO"]
)
def test_builtin_engines_exist(engine: str):
    assert engine in komis.main.engines.keys()
