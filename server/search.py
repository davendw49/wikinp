"""
elasticsearch

"""

from elasticsearch import Elasticsearch

es = Elasticsearch()


def search(query: str):
    dsl = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["bookname", "author", "zh_bookname", "zh_author"]
            }
        },
        "highlight": {
            "fields": {
                "bookname": {},
                "author": {},
                "zh_bookname": {},
                "zh_author": {}
            }
        }
    }

    result = es.search(index='wsm', docvalue_fields=['books'], body=dsl, size=10)
    return result
