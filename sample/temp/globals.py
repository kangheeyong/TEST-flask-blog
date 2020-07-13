print('globals')


g = [{'globals':'g'}]
session = [{'globals':'session'}]


class LocalStack(object):
    def __init__(self):
        self._local = []

    def push(self, obj):
        self._local.append(obj)
        return self._local

    def pop(self):
        stack = self._local
        if stack is None:
            return None
        elif len(stack) == 1:
            return stack[-1]
        else:
            return stack.pop()

    @property
    def top(self):
        try:
            return self._local[-1]
        except:
            return None


