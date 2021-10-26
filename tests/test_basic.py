import astroid

import pylint_aiida


def test_basic():
    ast = astroid.parse(
        """
    class MyClass:
        @classproperty
        def my_property(cls) -> AnnotatedType:
            return cls.my_value
    """
    )
    assert isinstance(ast.body[0], astroid.ClassDef)
