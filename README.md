### Gutentag!

This is a flask app for discussing HTTP servers! Enjoy.

### Setup

1. Make sure you have sqlite3 installed (`brew install sqlite3` is a good bet)
2. Copy settings.cfg.template to settings.cfg; update the sqlite url as needed.
3. `mkvirtualenv http-demo --python=python3`
4. `pip install -r requirements.txt`

### Running it

There's pretty much only one way to do this:

```shell
workon http-demo
python http-demo
```

You'll probably want to put this URL in your browser early on to make sure the DB works: `http://localhost:5000/admin/bootstrap`

Ding!
