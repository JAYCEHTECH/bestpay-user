from django import template

register = template.Library()


@register.filter
def mb_to_gb(value):
    """Converts a string into all lowercase"""
    cut_value = value[:-2]
    if float(cut_value) >= 1000.0:
        return f"{float(cut_value)/1000}GB"
    return f"{cut_value}MB"



