from flask import Flask, render_template, url_for, request, send_from_directory
app = Flask(__name__)

""" url_for('static', filename='style.css')

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name) """

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run()