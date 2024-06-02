from typing import List

from llama_index.core import QueryBundle
from llama_index.core.base.base_retriever import BaseRetriever
from llama_index.core.schema import NodeWithScore
import requests


class SolrRetriever(BaseRetriever):
    def __init__(self, url: str, collection: str):
        self.url = url
        self.collection = collection

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        # there is a Solr cluster running on self.url
        # and the collection is self.collection
        # we want to connect to it and retrieve documents related to query_bundle

        params = {"indent": "true", "q.op": "OR", "q": query_bundle.query_str}
        response = requests.get(f"{self.url}/{self.collection}/select", params=params)

        # Process JSON response
        results = response.json()

        # Access data within the response structure
        num_found = results["response"]["numFound"]
        print(num_found)
        docs = results["response"]["docs"]
        print(docs)
