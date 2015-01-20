# Dommert - Flask Cache 
# Example of Caching with Flask
# will query new results to cache every 120 seconds
from flask.ext.cache import cache


cache = cache(app)

@cache.cached(timeout=120)
@app.route()
def index():
	recent_var = some sql query;
	return render_template('index.html', var = recent_var)

