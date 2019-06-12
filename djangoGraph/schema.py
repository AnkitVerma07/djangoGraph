import graphene

import apps.accounts.schema


class Query(apps.accounts.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
