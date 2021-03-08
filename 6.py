import bs4
from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
	return """
		<html>
			<head></head>
			<body>
				<div id="target">Hello world</div>
			</body>
		</html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, 'html.parser')
	target = soup.find(id='target')
	
	print(target.get_text())

if __name__ == "__main__":
	main()