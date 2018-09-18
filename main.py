from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
	<head>
		<style>
			form {
				background-color: #eee;
				padding: 20px;
				margin: 0 auto;
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;
			}
			textarea {
				margin: 10px 0;
				width: 540px;
				height: 120px;
			}
		</style>
	</head>
	<body>
		<form method="post">
			<label for="rotate-by">Rotate by</label>
			<input id="rotate-by" type="text" name="rot"/>
			<label for="random-textarea"></label>
			<textarea id="random-textarea" name="text"></textarea>
			<input type="submit" name="Submit Query" />
		</form>
	</body>
</html>
"""

@app.route("/")
def index():
	return form

app.run()