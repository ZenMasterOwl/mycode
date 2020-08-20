import pytest
import os

def supercool():
    return "this is super cool"
    
def test_supercool():
    assert supercool() == "this is super cool"

#def test_supercool_fail():
    #assert supercool() == "this is super lame"

def test_file_existion():
    assert os.path.isfile("/home/student/") or os.path.isdir("/home/student/")
CONTENT = "kewl :#3"
def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    p2 = d / "goobye.txt"
    p2.write_text("goodbye")
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 2
    assert p2.read_text() == "goobye"
    assert 0
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    p2 = tmpdir.mkdir("sub").join("goodbye.txt")
    p2.write("no content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 2
    #used to see details of test that would otherwise pass
    assert 0
