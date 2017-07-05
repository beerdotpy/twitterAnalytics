from django import template
from datetime import date,datetime,timedelta

register = template.Library()

from django import template
register = template.Library()

@register.filter()
def as_table(model):
    ret = ""
    print model
    for name in model._meta.get_all_field_names():
        try:
            field = str(getattr(model, name))
            if field:
                ret += '<tr><td class="name">'+name+'</td><td class="field">'+field+'</td></td>'
        except AttributeError:
            pass
    return ret