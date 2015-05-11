from flask.ext.cache import cache

cache = cache(app)

@cache.cached(timeout=60)
@app.route()
def index():
	recent_var = some sql query;
	return render_template('index.html', var = recent_var)

