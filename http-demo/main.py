#!/usr/bin/env python

from flask import Flask, render_template, request

# This is a tinkertoy web app. Please enjoy.

# Here we make our application; we'll use this to set routes, among other
# things.
app = Flask(__name__)
# For now we're manually turning on `debug`; we like this for a few
# reasons. Chief among them: much better logging; "hot reloading," in which
# changes to our code will show up without having to stop and restart the
# server.
app.debug = True


# This is a "route" -- it tells the http server what URLs it can respond to
# (technically, we're defining "resources"). This route responds to "/", which
# is the "root" of our website. "/" is what you get implicitly if you go to,
# say "www.google.com" -- google.com is the "host", and with nothing else
# specified you get "/".
@app.route('/')
def main():
    return "We're up!"


# Another resource; this one can take a parameter. Notice that while our first
# route responds with plain text (not even HTML), this route responds be
# rendering a template.
@app.route('/helloworld')
@app.route('/helloworld/<name>')
def hello(name=None):
    return render_template("hello.html", name=name)


# These next two routes demonstrate a "request" -- that is, the form in `form`
# will make a POST to the URL in `yousaid`, which will then unpack the request
# and respond by rendering a template.
@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/yousaid', methods=['POST'])
def yousaid():
    if 'bev' in request.form.keys():
        choice = request.form['bev']
    else:
        choice = None
    return render_template("bevchoice.html", bev=choice)


if __name__ == '__main__':
    app.run()
