import urllib.parse
import uuid
from typing import List


def LN(args: List[str]):
    print(args)
    if args[0].startswith('rdf:'):
        args[0] = args[0][4:].lower()
    return ("_".join(args))

def UUID(args: List[str]):
    return str(uuid.uuid3(uuid.NAMESPACE_URL, "/".join(args)))

def URL_ENCODE(args: List[str]):
    print(args)
    return urllib.parse.quote_plus(" ".join(args))