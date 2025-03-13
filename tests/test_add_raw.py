import sys
import os
import unittest

# Add the parent directory to the path so we can import MarkupPy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MarkupPy import markup

class TestAddRaw(unittest.TestCase):
    
    def test_add_vs_add_raw(self):
        """Test the difference between add and add_raw methods"""
        # Rather than comparing, let's document the actual behavior
        # Create a page with add method
        page = markup.page(separator="|SEP|")  # Use a very distinct separator
        page.init()
        page.pre.open()
        page.add("A")
        page.add("B")
        page.pre.close()
        
        html = str(page)
        
        # The separator gets added between the content items
        self.assertIn("A|SEP|B", html)
        
        # Now test with add_raw
        page = markup.page(separator="|SEP|")
        page.init()
        page.pre.open()
        page.add_raw("A")
        page.add_raw("B")
        page.pre.close()
        
        html = str(page)
        
        # With add_raw, there's no separator
        self.assertIn("<pre>AB", html)
        self.assertNotIn("A|SEP|B", html)
    
    def test_add_raw_content_control(self):
        """Test that add_raw gives exact control over the content"""
        page = markup.page()
        page.init()
        page.pre.open()
        
        # With add_raw we have exact control over what goes in
        page.add_raw("ABC")  # No newlines
        
        page.pre.close()
        
        html = str(page)
        content = html.split("<pre>")[1].split("</pre>")[0].strip()
        
        # The content should be exactly "ABC" with nothing added
        self.assertEqual("ABC", content)
    
    def test_add_raw_appending(self):
        """Test that add_raw correctly appends to the last content item"""
        page = markup.page()
        page.init()
        page.pre.open()
        
        # First add creates a new content item
        page.add_raw("First")
        
        # Second add should append to the same content item
        page.add_raw(" Second")
        
        # Third add should also append
        page.add_raw(" Third")
        
        page.pre.close()
        
        html = str(page)
        
        # All content should be in one item without separators
        self.assertTrue("<pre>First Second Third" in html)
        
        # Extract content between pre tags
        content = html.split("<pre>")[1].split("</pre>")[0]
        
        # Check the exact content
        self.assertEqual("First Second Third", content.strip())
    
    def test_table_example(self):
        """Test the table example from the GitHub issue"""
        page = markup.page()
        page.init()
        
        # Simulate the table lines
        lines = [
            "+------------------+",
            "| Header           |",
            "+------------------+",
            "| Row 1            |",
            "| Row 2            |",
            "+------------------+",
            ""  # Empty line to end the table
        ]
        
        in_table = False
        
        for line in lines:
            if not in_table and line.startswith('+--'):
                in_table = True
                page.pre.open()
                page.add_raw(line + "\n")
                continue
                
            if in_table:
                if not line.strip():
                    # Don't add the empty line
                    page.pre.close()
                    in_table = False
                else:
                    page.add_raw(line + "\n")
                continue
        
        html = str(page)
        
        # Extract content between pre tags
        content = html.split("<pre>")[1].split("</pre>")[0].strip()
        
        # Check the exact content
        expected_content = """+------------------+
| Header           |
+------------------+
| Row 1            |
| Row 2            |
+------------------+""".strip()
        
        self.assertEqual(expected_content, content)

if __name__ == "__main__":
    unittest.main() 