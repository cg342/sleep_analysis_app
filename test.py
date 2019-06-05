import flask

def ind():
    # d =  'aaa'
    return flask.render_template('frontpage.html')

def show():
    message = flask.Request.args.get('inputpath')
    message = 'ddd'
    # forward_message = forward_message['inputpath']
    # forward_message = "new message!"
    return flask.render_template('endresult.html', display=message)

def show_result():

    return flask.render_template('my-form.html')