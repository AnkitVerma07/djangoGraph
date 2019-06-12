import graphene

from graphene_django.types import DjangoObjectType

from apps.accounts.models import Users


class UserType(DjangoObjectType):
    class Meta:
        model = Users


class Query(object):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info, **kwargs):
        return Users.objects.all()
