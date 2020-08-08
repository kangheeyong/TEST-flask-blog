from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

s = Serializer('secret', 30)
token = s.dumps({'user_id': 1}).decode('utf-8')
token
s.loads(token)

breakpoint()


