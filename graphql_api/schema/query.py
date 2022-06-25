# graphql_api/schema/query.py

import graphene
from wallet.graphql.schema.query import WalletQuery


class Query(graphene.ObjectType, WalletQuery):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "world"
