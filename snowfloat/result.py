"""Task results."""

class Result(object):
    """Task result.

    Attributes:
        uuid (str): UUID.

        uri (str): URI.

        tag: Tag data.

        date_created (str): Creation date in ISO format.

        date_modified (str): Modification date in ISO format.
    """
    uuid = None
    uri = None
    date_created = None
    date_modified = None
    tag = None

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            getattr(self, key)
            setattr(self, key, val)

def parse_results(results):
    """Convert results dictionaries to Result objects.

    Args:
        results (list): List of result dictionaries.

    Returns:
        list: List of Result objects.
    """
    return [Result(uuid=r['uuid'],
                   uri=r['uri'],
                   tag=r['tag'],
                   date_created=r['date_created'],
                   date_modified=r['date_modified']) for r in results]
