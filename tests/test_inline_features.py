import sys
import os
import unittest

# Add the parent directory to the path so we can import MarkupPy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MarkupPy import markup

class TestInlineFeatures(unittest.TestCase):
    
    def test_style_content_string(self):
        """Test that style_content works with a string value"""
        page = markup.page()
        style_content = "body { background-color: #f0f0f0; }"
        page.init(title="Test", style_content=style_content)
        
        html = str(page)
        # Verify the style tag with content is in the HTML
        self.assertIn("<style>body { background-color: #f0f0f0; }</style>", html)
    
    def test_style_content_list(self):
        """Test that style_content works with a list of styles"""
        page = markup.page()
        style_list = [
            "body { background-color: #f0f0f0; }",
            "h1 { color: blue; }"
        ]
        page.init(title="Test", style_content=style_list)
        
        html = str(page)
        # Verify both style tags are in the HTML
        self.assertIn("<style>body { background-color: #f0f0f0; }</style>", html)
        self.assertIn("<style>h1 { color: blue; }</style>", html)
    
    def test_script_content_string(self):
        """Test that script_content works with a string value"""
        page = markup.page()
        script_content = "function greet() { alert('Hello!'); }"
        page.init(title="Test", script_content=script_content)
        
        html = str(page)
        # Verify the script tag with content is in the HTML
        self.assertIn('<script type="text/javascript">function greet() { alert(\'Hello!\'); }</script>', html)
    
    def test_script_content_list(self):
        """Test that script_content works with a list of scripts"""
        page = markup.page()
        script_list = [
            "function greet() { alert('Hello!'); }",
            "function goodbye() { alert('Goodbye!'); }"
        ]
        page.init(title="Test", script_content=script_list)
        
        html = str(page)
        # Verify both script tags are in the HTML
        self.assertIn('<script type="text/javascript">function greet() { alert(\'Hello!\'); }</script>', html)
        self.assertIn('<script type="text/javascript">function goodbye() { alert(\'Goodbye!\'); }</script>', html)
    
    def test_combined_features(self):
        """Test that style_content and script_content work together"""
        page = markup.page()
        style_content = "body { background-color: #f0f0f0; }"
        script_content = "function greet() { alert('Hello!'); }"
        page.init(title="Test", style_content=style_content, script_content=script_content)
        
        html = str(page)
        # Verify both style and script tags are in the HTML
        self.assertIn("<style>body { background-color: #f0f0f0; }</style>", html)
        self.assertIn('<script type="text/javascript">function greet() { alert(\'Hello!\'); }</script>', html)

if __name__ == "__main__":
    unittest.main() 