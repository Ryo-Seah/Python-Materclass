class HTML:
    """Here's an example of a simple HTML document:

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<HTML>
   <HEAD>
      <TITLE>My first HTML document</TITLE>
   </HEAD>
   <BODY>
      <P>Hello world!
   </BODY>
</HTML>"""


class Tag:
    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DocType has no end tag


class Head(Tag):
    def __init__(self,title=None):
        super(Head, self).__init__('HEAD', title=None)
        if title:
            new_title = Tag('title', title)
            self.contents = str(new_title)


class Body(Tag):
    def __init__(self):
        super(Body, self).__init__('Body', '')  # contents built up separately below
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
            
        super().display(file=file)


class HtmlDoc:

    def __init__(self,doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):  # encapsulation - same name method but delegate to body class
        self._body.add_tag(name, contents)

    def display(self,file=None):
        self._doc_type.display(file=file)
        print('<HTML>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</HTML>',file=file)


if __name__ == '__main__':
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances "
                          "of objects to build up another object")
    new_body.add_tag('p', "The combined object doesn't actually own the object it consists of, "
                          "if its destroyed, the objects still exist")
    new_head = Head('Aggregation')
    new_doc_type = DocType()
    new_page = HtmlDoc(new_doc_type, new_head, new_body)
    with open('test2.html', 'w') as test_doc:
        new_page.display(file=test_doc)
