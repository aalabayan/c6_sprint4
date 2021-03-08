from bs4 import BeautifulSoup

def generate_html():
	return """
		<html>
			<head></head>
			<body>
				<a href="/a.html">A</a>
				<a href="/b.html">B</a>
				<a href="/c.html">C</a>
				<a href="/d.html">D</a>
				<a href="/e.html">E</a>
				
				<script>
					var hello = "yoh";
					alert(hello);
				</script>
			</body>
		</html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, 'html.parser')
	soup.find(id="var hello")
	
if __name__ == "__main__":
	main()
