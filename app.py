import json
from random import random
from collections import OrderedDict
from flask import Flask, render_template, request, jsonify, redirect

from forms import SlickEditableForm

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret_key"

#jdata=json.dumps(data)

@app.route('/slick_editable', methods=["GET", "POST"])
def slick_editable():
	form = SlickEditableForm()

	columns = [
		{"id": "title", "name": "Title", "field": "title", "width": 120, "cssClass": "cell-title", "editor": "Slick.Editors.Text", "validator": "requiredFieldValidator"},
		{"id": "desc", "name": "Description", "field": "description", "width": 100, "editor": "Slick.Editors.LongText"},
		{"id": "duration", "name": "Duration", "field": "duration", "editor": "Slick.Editors.Text"},
		{"id": "%", "name": "% Complete", "field": "percentComplete", "width": 80, "resizable": False, "formatter": "Slick.Formatters.PercentCompleteBar", "editor": "Slick.Editors.PercentComplete"},
		{"id": "start", "name": "Start", "field": "start", "minwidth": 60, "editor": "Slick.Editors.Date"},
		{"id": "finish", "name": "Finish", "field": "finish", "minwidth": 60, "editor": "Slick.Editors.Date"},
		{"id": "effort-driven", "name": "Effort Driven", "width": 80, "minwidth": 20, "maxwidth": 80, "cssClass": "cell-effort-driven", "field": "effortDriven", "formatter": "Slick.Formatters.Checkmark", "editor": "Slick.Editors.Checkbox"}
	]
	data = []
	options = {
		"editable": True,
		"enableAddRow": True,
		"enableCellNavigation": True,
		"asyncEditorLoading": False,
		"autoEdit": False
	}

	for i in range(30):
		d = OrderedDict()
		d["title"] = "Task %d" % i;
		d["description"] = "This is a sample task description.\n  It can be multiline";
		d["duration"] = "5 days";
		d["percentComplete"] = int(random() * 100)
		d["start"] = "01/01/2009";
		d["finish"] = "01/05/2009";
		d["effortDriven"] = (i % 5 == 0);
		data.append(d)

	if request.method == "POST":
		print(form.data.data)
		#print(request.json)
		#return jsonify(success=True)
		return render_template("slick_editable.html", form = form, id = "myGrid", url_for = "slick_editable", columns = columns, data = data, options = options)
		#print(form.myGrid.data)

	return render_template("slick_editable.html", form = form, id = "myGrid", url_for = "slick_editable", columns = columns, data = data, options = options)


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=8059)
