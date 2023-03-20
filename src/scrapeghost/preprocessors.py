import lxml.html


class Preprocessor:
    """
    Preprocessor interface: given a node, returns a list of nodes.
    """

    def __call__(self, node: lxml.html.HtmlElement) -> list[lxml.html.HtmlElement]:
        raise NotImplementedError


class CleanHTML(Preprocessor):
    """
    Given HTML, return a cleaned HTML string.

    Uses lxml.html.clean.Cleaner.
    """

    def __init__(self, **kwargs):
        self.cleaner = lxml.html.clean.Cleaner(**kwargs)

    def __str__(self) -> str:
        return "CleanHTML"

    def __call__(self, html: str) -> str:
        return lxml.html.clean.Cleaner().clean_html(html)


class XPath(Preprocessor):
    """
    Given an XPath selector, return a list of nodes.
    """

    def __init__(self, xpath: str):
        self.xpath = xpath

    def __str__(self) -> str:
        return f"XPath({self.xpath})"

    def __call__(self, node: lxml.html.HtmlElement) -> list[lxml.html.HtmlElement]:
        return node.xpath(self.xpath)


class CSS(Preprocessor):
    """
    Given a CSS selector, return a list of nodes.
    """

    def __init__(self, css: str):
        self.css = css

    def __str__(self) -> str:
        return f"CSS({self.css})"

    def __call__(self, node: lxml.html.HtmlElement) -> list[lxml.html.HtmlElement]:
        return node.cssselect(self.css)
