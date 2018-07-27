# vim: set ts=4 et sw=4 sts=4 fileencoding=utf-8 :

import user
import index
import tt

urls = (
    ('^/$', index.IndexHandler),
    ('^/login$', user.LoginHandler),
    ('^/TT/test$', tt.IndexHandler),
    ('^/TT/data/upload$', tt.DataUploadHandler),
    ('^/TT/data/init$', tt.DataInitHandler),
    ('^/TT/data/delete$', tt.DataDealHandler),
    ('^/TT/sqllog/deal$', tt.SqlDealHandler),
)
