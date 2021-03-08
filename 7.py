from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
	return """
		<html>
			<head></head>
			<body>
				<div>A</div>
				<div>B</div>
				<div>C</div>
				<div>D</div>
			</body>
		</html>
	"""

def main():
	html_doc = generate_html()
	soup = BeautifulSoup(html_doc, 'html.parser')
    
    div_elements = soup.find_all('div')
    
    for div_element in div_elements:
        print(div_element.get_text())
	
if __name__ == "__main__":
	main()
