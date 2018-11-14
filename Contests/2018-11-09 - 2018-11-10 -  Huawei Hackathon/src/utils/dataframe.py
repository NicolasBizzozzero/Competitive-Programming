import pandas as pd
import numpy as np

from src.utils.list import removes_indexes


def swap_columns(df, column1, column2, inplace=True):
    """ Swap two dataframe columns' position passed either by name or by index.
    :param df: The pandas DataFrame to swap columns from.
    :param column1: The first column to swap. Can be an index or a column name.
    :param column2: The second column to swap. Can be an index or a column
    name.
    """
    columns_name = list(df)

    # Change the parameters to index if they are column name
    if isinstance(column1, str):
        column1 = columns_name.index(column1)
    if isinstance(column2, str):
        column2 = columns_name.index(column2)

    # Swap the columns and reindex the dataframe
    columns_name[column2], columns_name[column1] = \
        columns_name[column1], columns_name[column2]
    return df.reindex(columns=columns_name)


def insert_column(df, column, index, inplace=True):
    """ Insert an existing pandas DataFrame column into a DataFrame.
    :param df: The pandas DataFrame to insert column to.
    :param column: The column to insert. If can be an index or a column name.
    :param index: The index to insert the column to.
    """
    columns_name = list(df)

    if isinstance(column, str):
        column = columns_name.index(column)

    if isinstance(column, int):
        column_name = columns_name.pop(column)
        columns_name.insert(index, column_name)
        return df.reindex(columns=columns_name)


def drop_columns(df, columns, inplace=True):
    """ Drop multiple columns from a pandas DataFrame, either passed by name
    or by index.
    :param df: The pandas DataFrame to drop columns from.
    :param columns: The columns to drop from the DataFrame. Can be passed by
    index or by name.
    """
    columns_name = list(df)

    # Retrieve the index of all columns to drop
    columns_to_drop = []
    for column in columns:
        if isinstance(column, str):
            column = columns_name.index(column)
        columns_to_drop.append(column)

    # Drop the corresponding columns
    columns_name = removes_indexes(columns_name, columns_to_drop)
    return df.reindex(columns=columns_name)


def categorical_string_to_int(df, column, inplace=True):
    """ Transform a categorical column of a pandas DataFrame from a string
    type to an integer.
    :param df: The pandas DataFrame to transform the column from.
    :param columns: The column to transform from the DataFrame. Can be passed
    by index or by name.
    """
    if inplace:
        df[column] = (df[column].astype('category')).cat.codes
    else:
        df = df.copy(deep=True)
        df[column] = (df[column].astype('category')).cat.codes
        return df


def splitting_date(df, datetime_column, convert_to_datetime=False,
                   datetime_format=None, parsing_error='coerce',
                   drop_column=True, inplace=True, date=False, time=False,
                   year=False, month=False, day=False, hour=False,
                   minute=False, second=False, microsecond=False,
                   nanosecond=False, week=False, weekofyear=False,
                   dayofweek=False, weekday=False, dayofyear=False,
                   quarter=False, is_month_start=False, is_month_end=False,
                   is_quarter_start=False, is_quarted_end=False,
                   is_year_start=False, is_year_end=False, is_leap_year=False,
                   days_in_month=False):
    """ Split a pandas DataFrame DateTime column into separate columns for
    each data it contains.
    Each new column need to be specified as a parameter. All possible
    parameters are listed here :
    https://pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-properties

    :param df: The pandas DataFrame to split the column from.
    :param datetime_column: The column to split.
    :param convert_to_datetime: Convert the column to the DateTime type. If
    `True`, you also need to specify the `datetime_format` parameter.
    :param datetime_format: Format of the datetime column during its
    conversion to the DateTime type. Follow the python format for the
    `stfrtime` method. They are described here:
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    :param parsing_error: Behavior to adopt in case of a parsing error during
    the column conversion. Possible parameters are described here:
    https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html
    :param drop_column: Drop the datetime column after the split has occured.
    """
    # Convert the column to the datetime type if necessary
    datetime_column = df[datetime_column]
    if convert_to_datetime:
        datetime_column = pd.to_datetime(datetime_column,
                                         errors=parsing_error,
                                         format=datetime_format)

    # Iterativaly filling a dictionary containing all asked columns
    columns = dict()
    if date:
        columns["date"] = datetime_column.dt.date
    if time:
        columns["time"] = datetime_column.dt.time
    if year:
        columns["year"] = datetime_column.dt.year
    if month:
        columns["month"] = datetime_column.dt.month
    if day:
        columns["day"] = datetime_column.dt.day
    if hour:
        columns["hour"] = datetime_column.dt.hour
    if minute:
        columns["minute"] = datetime_column.dt.minute
    if second:
        columns["second"] = datetime_column.dt.second
    if microsecond:
        columns["microsecond"] = datetime_column.dt.microsecond
    if nanosecond:
        columns["nanosecond"] = datetime_column.dt.nanosecond
    if week:
        columns["week"] = datetime_column.dt.week
    if weekofyear:
        columns["weekofyear"] = datetime_column.dt.weekofyear
    if dayofweek:
        columns["dayofweek"] = datetime_column.dt.dayofweek
    if weekday:
        columns["weekday"] = datetime_column.dt.weekday
    if dayofyear:
        columns["dayofyear"] = datetime_column.dt.dayofyear
    if quarter:
        columns["quarter"] = datetime_column.dt.quarter
    if is_month_start:
        columns["is_month_start"] = datetime_column.dt.is_month_start
    if is_month_end:
        columns["is_month_end"] = datetime_column.dt.is_month_end
    if is_quarter_start:
        columns["is_quarter_start"] = datetime_column.dt.is_quarter_start
    if is_quarted_end:
        columns["is_quarted_end"] = datetime_column.dt.is_quarted_end
    if is_year_start:
        columns["is_year_start"] = datetime_column.dt.is_year_start
    if is_year_end:
        columns["is_year_end"] = datetime_column.dt.is_year_end
    if is_leap_year:
        columns["is_leap_year"] = datetime_column.dt.is_leap_year
    if days_in_month:
        columns["days_in_month"] = datetime_column.dt.days_in_month

    df = df.assign(**columns, inplace=inplace)
    if drop_column:
        return drop_columns(df, [datetime_column], inplace=inplace)
    elif not inplace:
        return df


def memory_usage(df):
    """ Return the Memory usage of a pandas DataFrame. """
    columns_usage = df.memory_usage(index=True, deep=True)
    total_usage = pd.Series({
        "total": df.memory_usage(index=True, deep=True).sum()
    })
    return columns_usage.append(total_usage)


def one_hot_encoding(df, column, drop_column=True, prefix="is_"):
    """ Encode a column into the one-hot format, eg: with one new boolean
    column per unique value of the column.
    """
    columns_name = list(df)

    # Change the parameter to index if it is a column name
    if isinstance(column, str):
        column = columns_name.index(column)

    new_columns = df.iloc[:, column].str.get_dummies().astype(np.int8)

    # Renaming columns with the prefix
    new_columns.columns = [prefix + col for col in new_columns.columns]

    if drop_column:
        df = drop_columns(df, [column], inplace=False)

    return pd.concat([df, new_columns], axis=1)


def one_hot_decoding(df, new_column_name):
    """ Decode multiples columns from the one-hot format to a simple
    categorical column.
    """
    decoded_column = pd.Series(df.columns[np.where(df != 0)[1]])
    decoded_column.name = new_column_name
    return decoded_column.to_frame()


if __name__ == '__main__':
    pass
