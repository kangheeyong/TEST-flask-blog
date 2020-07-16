import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Department as DepartmentModel
from models import Role as RoleModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class DepartmentCon(relay.Connection):
    class Meta:
        node = Department


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class RoleCon(relay.Connection):
    class Meta:
        node = Role


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    role = graphene.List(Role, role_id=graphene.Int(required=True))

    def resolve_role(self, info, **kwargs):
        role_query = Role.get_query(info)
        return role_query.filter(RoleModel.role_id.contains(kwargs.get('role_id')))

    all_roles = SQLAlchemyConnectionField(RoleCon)

    all_departments = SQLAlchemyConnectionField(DepartmentCon, sort=None)


schema = graphene.Schema(query=Query, types=[Department, Role])




