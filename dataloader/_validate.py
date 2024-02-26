from typing import Any

from typedframe import TypedDataFrame


class GenericValidationTF(TypedDataFrame):
    schema: dict = {
        "class_": Any,
    }
