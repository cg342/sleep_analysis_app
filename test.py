import flask

def ind():
    d =  ''
    return flask.render_template('weather.html', display = d)

def show():
    forward_message = flask.Request.form.to_dict()
    forward_message = forward_message['inputpath']
    # forward_message = "new message!"
    return flask.render_template('weather.html', display=forward_message)