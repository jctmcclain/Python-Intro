# Navigator

* [Python Introduction](https://github.com/jctmcclain/Python-Intro/blob/main/python-intro.md)
* [Python Files](https://github.com/jctmcclain/Python-Intro/blob/main/FILES/python-files.md)
* [DuckDB - SQL](https://github.com/jctmcclain/Python-Intro/blob/main/SQL/SQL-Starts.md)
----
* [Swimming App](https://github.com/jctmcclain/Python-Intro/blob/main/swimmingapp/README.md)

----
* [Git - Software Code Management Tool](https://github.com/jctmcclain/Python-Intro/blob/main/GIT/GettingGit.md)

---
# Flask Tips


```python
# app.py file
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

```

```shell
# Tell a Flask app to listen on all addresses

flask --app app.py run --host=0.0.0.0

```

## Add in templates

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
   title="Really Cool Flask Website"
   return render_template('index.html',title=title)
```

### Create a directory called templates 
```shell
mkdir templates
```

### Add in the index.html template file 
```html
<!DOCTYPE html>
<html>
<head><title>{{title}}</title></head>
<body>
<h1>{{title}}</h1>
</body>
</html>
```

