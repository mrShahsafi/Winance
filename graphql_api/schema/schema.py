# qraphql_api/schema/schema.py

import graphene
from .query import Query

schema = graphene.Schema(query=Query)
