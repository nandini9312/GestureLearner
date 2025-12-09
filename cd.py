products = [
    {"title": "Women Kurta Set", "price": "₹499", "meta": "Free Delivery", "img": ""},
    {"title": "Smartwatch Series X", "price": "₹1,299", "meta": "4.2 ★ 3k+ ratings", "img": ""},
    {"title": "Men Sneakers", "price": "₹799", "meta": "Best Seller", "img": ""},
    {"title": "Kids Backpack", "price": "₹349", "meta": "Cash on Delivery", "img": ""},
    {"title": "Makeup Kit", "price": "₹599", "meta": "Trending", "img": ""},
    {"title": "Bedsheet Set", "price": "₹699", "meta": "Top Quality", "img": ""},
    {"title": "Wireless Earbuds", "price": "₹1,099", "meta": "Popular", "img": ""},
    {"title": "Necklace Set", "price": "₹449", "meta": "New Arrival", "img": ""},
]

html_output = '<div id="productGrid">\n'

for p in products:
    card = f"""
    <div class="card">
        <div class="img">Product image</div>
        <div class="info">
            <div class="title">{p['title']}</div>
            <div class="price">{p['price']}</div>
            <div class="meta">{p['meta']}</div>
        </div>
        <button class="add">Add to cart</button>
    </div>
    """
    html_output += card

html_output += "\n</div>"

# Save to file
with open("products.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("HTML file generated: products.html")
