# """
# We want to create an object with methods for various HTML elements: div, p, span and h1 for the sake of this Kata.

# These methods will wrap the passed-in string in the tag associated with each.

# Format.div("foo"); # returns "<div>foo</div>"
# Format.p("bar"); # returns "<p>bar</p>"
# Format.span("fiz"); # returns "<span>fiz</span>"
# Format.h1("buz"); # returns "<h1>buz</h1>"

# We also want to be able to add additional formatting by chaining our methods together.

# Format.div.h1("FooBar");
# # "<div><h1>FooBar</h1><div>"

# Format.div.p.span("FizBuz");
# # "<div><p><span>FizBuz</span></p></div>"
# and so on, as deep as we care to use.

# Multiple arguments should be concatenated and wrapped in the correct HTML formatting.

# Format.div.h1("Foo", "Bar");
# # "<div><h1>FooBar</h1></div>"
# We should be able to store the created methods and reuse them.

# wrapInDiv = Format.div;
# wrapInDiv("Foo");   # "<div>Foo</div>"
# wrapInDiv.p("Bar"); # "<div><p>Bar</p></div>"

# wrapInDivH1 = Format.div.h1;
# wrapInDivH1("Far"); # "<div><h1>Far</h1></div>"
# wrapInDivH1.span("Bar"); # "<div><h1><span>Bar</span></h1></div>"
# And finally, we should be able to nest Format calls.

# Format.div(
#   Format.h1("Title"), 
#   Format.p(f"Paragraph with a {Format.span('span')}.")
# )
# # returns "<div><h1>Title</h1><p>Paragraph with a <span>span</span>.</p></div>"
# """


class Format:
    def __init__(self):
        self.wrapper = None
        pass

    # def __repr__(self):
    #     return something

    # meta wrapper function that uses method called and text
    # don't know how to do that
    # getattr?
    # def wrapper(method, text):
    #     return f"<{method}>{text}</{method}>"

    # chaining - implemented by ensuring that all chainable methods return self

    def div(txt):
        self.wrapper += f'<div>{txt}</div>'
        return f"<div>{txt}</div>"

    def p(txt):
        return f"<p>{txt}</p>"

    def span(txt):
        return f"<span>{txt}</span>"

    def h1(txt):
        return f"<h1>{txt}</h1>"

    def __add__(self, other):
        self.wrapper = self.wrapper + other.wrapper
        return self.wrapper

# class Format:

#     def __init__(self):
#         pass

#     def div(self, txt):
#         return f"something {txt} another thing"
