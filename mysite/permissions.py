from graphql import GraphQLError


def is_authenticated(func):
    def wrapper(cls, info, **kwargs):
        if not info.context.user:
            raise GraphQLError(
                message="Unauthorized user!",
                extensions={
                    "error": "You are not authorized user.",
                    "code": "unauthorized"
                }
            )
        return func(cls, info, **kwargs)
    return wrapper


def is_admin_user(func):
    def wrapper(cls, info, **kwargs):
        if not info.context.user:
            raise GraphQLError(
                message="Unauthorized user!",
                extensions={
                    "error": "You are not authorized user.",
                    "code": "unauthorized"
                }
            )
        if not info.context.user.is_admin:
            raise GraphQLError(
                message="User is not permitted.",
                extensions={
                    "error": "You are not authorized to perform operations.",
                    "code": "invalid_permission"
                }
            )
        return func(cls, info, **kwargs)
    return wrapper


def is_client_request(func):
    def wrapper(cls, info, **kwargs):
        try:
            client = info.context.client
        except Exception as e:
            raise GraphQLError(
                message="Unauthorized client!",
                extensions={
                    "error": "You are not authorized client.",
                    "code": "unauthorized"
                }
            )
        return func(cls, info, **kwargs)
    return wrapper

