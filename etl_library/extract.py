def extract_data(source: str) -> list:
    """
    Extracts data from a given source.

    Args:
        source (str): Path to data source (e.g., S3, local, database).

    Returns:
        list: Extracted data.

    Example:
        >>> extract_data("s3://my-bucket/data.parquet")
        [{"col1": "value1", "col2": "value2"}]
    """
    return []