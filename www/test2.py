from datetime import datetime
import time
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)





def init(**kw):
    env = {}
    filters = kw.get('filters', None)
    print(filters)
    print(filters.items())
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
init(filters=dict(datetime=datetime_filter))

# print(type(filters))
# print(filters)