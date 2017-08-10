# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import user
import index

urls = (
    ('^/$', index.IndexHandler),
    ('^/login$', user.LoginHandler),
)
