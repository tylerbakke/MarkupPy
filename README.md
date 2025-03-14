## MarkupPy
This is MarkupPy - a Python module that attempts to make it easier to generate HTML/XML from a Python program in an intuitive, lightweight, customizable and pythonic way. It works with both python 2 and 3.

<b>Installation:</b>
    
    pip install MarkupPy

Documentation and further info is at https://tylerbakke.github.io/MarkupPy/

Please send bug reports, feature requests, enhancement ideas or questions to tylerbakke@gmail.com.

The Python Package can be found at https://pypi.python.org/pypi/MarkupPy.

The code is in the public domain. Version: 1.17 as of March 12 2024.

## Usage Examples

### Basic Example

```python
from MarkupPy import markup

# Create an HTML page
page = markup.page()
page.init(title="My Title")
page.p("Hello, World!")
page.p.close()

# Print the HTML
print(page)
```

### Inline Styles and Scripts (v1.16+)

You can now add inline CSS and JavaScript directly in the `init` method:

```python
page = markup.page()
page.init(
    title="My Styled Page",
    style_content="body { background-color: #f0f0f0; } h1 { color: blue; }",
    script_content="function greet() { alert('Hello!'); }"
)
```

You can also pass multiple styles/scripts as a list:

```python
page.init(
    title="My Styled Page",
    style_content=[
        "body { background-color: #f0f0f0; }",
        "h1 { color: blue; }"
    ],
    script_content=[
        "function greet() { alert('Hello!'); }",
        "function goodbye() { alert('Goodbye!'); }"
    ]
)
```

### Avoiding Extra Newlines in Pre Tags (v1.17+)

When adding content to `<pre>` elements, you might want to avoid extra newlines. The `add_raw` method helps with this:

```python
page = markup.page()
page.init()
page.pre.open()

# Standard add method (inserts extra newlines between each addition)
page.add("Line 1")
page.add("Line 2")  # This will create extra space between lines

# Better approach with add_raw (no extra newlines)
page.add_raw("Line 3\n")
page.add_raw("Line 4\n")  # Only the explicit newlines are included

page.pre.close()
```

For pre-formatted text with tables or code samples, `add_raw` preserves the exact formatting you specify.

## Running Tests

The package includes tests for all features. To run the tests:

```bash
# Navigate to the MarkupPy directory
cd MarkupPy

# Run all tests
python tests/run_tests.py

# Run specific test modules
python tests/test_inline_features.py
python tests/test_add_raw.py
```

The tests verify that:
1. Inline styles and scripts work correctly in the `init` method
2. The `add_raw` method properly handles pre-formatted content without adding unwanted newlines
