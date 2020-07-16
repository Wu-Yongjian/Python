from db import get_table_metadata,get_all_tables,get_table_data
from flask import Flask, request, flash, url_for, redirect, render_template


app = Flask(__name__)

@app.route('/showtable')
def showtable(tablename=None):
    if tablename==None:
        return render_template('show.html', tabledefine=get_all_tables())


@app.route('/showtable/<tablename>')
def showtabledef(tablename):
    return render_template('show.html', tabledefine=get_table_metadata(tablename),tabledata=get_table_data(tablename))


@app.route('/settable', methods=['GET', 'POST'])
def settable():
    if request.method == 'POST':
        if not request.form['tablename']:
            flash('Please enter all the fields', 'error')
        else:
            gettablename = request.form['tablename']
            print(gettablename)
            return redirect(url_for('showtabledef',tablename=gettablename))
    return render_template('first.html')

if __name__ == '__main__':
    app.run(debug=True)







