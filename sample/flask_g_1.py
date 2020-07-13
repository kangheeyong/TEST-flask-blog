from flask import Flask, g
app = Flask(__name__)


with app.app_context():
    print('in app context, before first request context')
    print('setting g.foo to abc')
    g.foo = 'abc'
    print('g.foo should be abc, is: {0}'.format(g.foo))

    with app.test_request_context():
        print('in first request context')
        print('g.foo should be abc, is: {0}'.format(g.foo))
        print('setting g.foo to xyz')
        g.foo = 'xyz'
        print('g.foo should be xyz, is: {0}'.format(g.foo))

    print('in app context, after first request context')
    print('g.foo should be abc, is: {0}'.format(g.foo))

    with app.test_request_context():
        print('in second request context')
        print('g.foo should be abc, is: {0}'.format(g.foo))
        print('setting g.foo to pqr')
        g.foo = 'pqr'
        print('g.foo should be pqr, is: {0}'.format(g.foo))

    print('in app context, after second request context')
    print('g.foo should be abc, is: {0}'.format(g.foo))




