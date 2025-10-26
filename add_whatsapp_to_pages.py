import re
import os

files = [
    "pineapple-sliced.html",
    "pineapple-long-strip.html",
    "aseptic-pineapple-pulp.html",
    "sulphited-pineapple-pulp.html",
    "sulfited-fiber-rich-pineapple-pulp.html",
    "gi-tagged-pineapple.html",
    "about.html",
    "blog.html",
    "blog-detail.html",
    "blog-listview.html",
    "cart.html",
    "checkout.html",
    "compare.html",
    "faq.html",
    "login-register.html",
    "my-account.html",
    "shop.html",
    "shop-grid-fullwidth.html",
    "shop-list-fullwidth.html",
    "shop-list-left-sidebar.html",
    "shop-list-right-sidebar.html",
    "shop-right-sidebar.html",
    "single-product.html",
    "single-product-affiliate.html",
    "single-product-group.html",
    "single-product-sale.html",
    "single-product-sticky.html",
    "single-product-variable.html",
    "wishlist.html",
    "404.html",
    "index-2.html"
]

for file in files:
    if not os.path.exists(file):
        print(f"⚠ Skipping {file} - file not found")
        continue
        
    print(f"Processing {file}...")
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add CSS link if not present
        if 'whatsapp-float.css' not in content:
            content = content.replace(
                '<!-- Style CSS -->\n    <link rel="stylesheet" href="assets/css/style.css">\n\n</head>',
                '<!-- Style CSS -->\n    <link rel="stylesheet" href="assets/css/style.css">\n\n    <!-- WhatsApp Float CSS -->\n    <link rel="stylesheet" href="assets/css/whatsapp-float.css">\n\n</head>'
            )
        
        # Add WhatsApp HTML if not present
        whatsapp_html = '''        <!-- Floating WhatsApp Icon -->
        <a href="https://wa.me/916282069204" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
            <i class="fa fa-whatsapp"></i>
        </a>

'''
        
        if whatsapp_html not in content:
            # Look for scroll-to-top end pattern
            pattern = r'(<!-- Scroll To Top End Here -->)\s*(</div>)'
            replacement = r'\1\n\n' + whatsapp_html + r'\2'
            content = re.sub(pattern, replacement, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file} updated")
    except Exception as e:
        print(f"✗ Error processing {file}: {e}")

print("\nAll files processed!")
