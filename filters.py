import datetime
import re
from jinja2 import evalcontextfilter, Markup, escape

def ts2readable(ts):
    if ts:
        dt = datetime.datetime.fromtimestamp(int(ts))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return None

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n')
                          for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
