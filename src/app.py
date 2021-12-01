import json
from flask import Flask, render_template, jsonify
from data_request import TurbineData

app = Flask(__name__)

@app.route('/')
@app.route('/turbine/<name>')
def html_table(name=None):
    tb = TurbineData()
    if tb.error:
        return  render_template("turbine_list.html", error=tb.error)
    else:
        if name:
            df = tb.data.loc[tb.data['turbine'] == name]
        else:    
            df = tb.formatted_data
        # link_column is the column that I want to add a button to
        return render_template("turbine_list.html", column_names=list(df.columns.values), row_data=list(df.values.tolist()),
                                link_column="Name", zip=zip, name=name, error=tb.error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
