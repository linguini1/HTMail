# HTML object class
__author__ = "Matteo Golin"

# Imports
from bs4 import BeautifulSoup

# Constants
PARSER: str = 'html.parser'


# Class
class HTMLObject:

    __resources_dir = "./resources"

    """Represents the HTML and CSS files required for the HTML email."""

    def __init__(self, file_name: str):
        self.html_file = f"{self.__resources_dir}/{file_name}.html"
        self.css_file = f"{self.__resources_dir}/{file_name}.css"
        self.html_string = self.__get_html()

    def __get_styles(self) -> BeautifulSoup:

        """Returns the CSS styling as a string representation of a style HTML tag."""

        with open(self.css_file, 'r') as styles:
            style = f"<style>{styles.read()}</style>"

        return BeautifulSoup(style, features=PARSER)

    def __get_html(self) -> str:

        """Adds the style inline to the HTML file."""

        with open(self.html_file, 'r') as html:
            soup = BeautifulSoup(html, features=PARSER)

        header = soup.select_one('head')
        styles = self.__get_styles()
        header.append(styles)

        return str(soup)
