import pytest

"""
Program: {{cookiecutter.project_name}}
"""


def {{cookiecutter.project_slug}}():
    pass


def test_{{cookiecutter.project_slug}}():
    pass


if __name__ == "__main__":
    pytest.main(['-svv', __file__])
    {{cookiecutter.project_slug}}()
