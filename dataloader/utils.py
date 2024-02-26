from pandas import DataFrame
from typedframe import TypedDataFrame


def validateDF(df: DataFrame, tdf: type[TypedDataFrame]) -> bool:
    """
    Given a DataFrame object and a TypedDataFrame defintion
    (an uninstantiated class), verify that the DataFrame object complies with
    the TypedDataFrame defined schema.
    """
    try:
        tdf(df=df)
    except AssertionError:
        return False
    else:
        return True
