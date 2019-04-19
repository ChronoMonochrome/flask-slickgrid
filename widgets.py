from wtforms.validators import Required, Length, EqualTo
from wtforms import Field
from wtforms.widgets import html_params
from flask import Markup

# https://stackoverflow.com/questions/14510630/wtforms-creating-a-custom-widget
class SlickGridWidget(object):
	html_params = staticmethod(html_params)

	def __init__(self, style):
		self.style = style

	def __call__(self, field, **kwargs):
		kwargs.setdefault('id', field.id)
		style_str = ""
		#print(self.style)
		for k, v in self.style.items():
			style_str += "{k}: {v};".format(k = k, v = v)

		kwargs.setdefault('style', style_str)
		if 'value' not in kwargs:
			kwargs['value'] = field._value()
		return Markup('<div %s></div>' % (self.html_params(name=field.name, **kwargs)))


class SlickGrid(Field):
	def __init__(self, label=None, validators=None, style={"width": "100%", "height": "500px"}, **kwargs):
		self.widget = SlickGridWidget(style)
		super(SlickGrid, self).__init__(label, validators, widget = self.widget, **kwargs)

	def _value(self):
		if self.data:
			return u''.join(self.data)
		else:
			return u''
