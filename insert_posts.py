from main import db
from main import Posts
from datetime import datetime

posts = [
    {
        "title": "Rust: The Power of Safety and Performance",
        "tagline": "A systems programming language focused on safety, speed, and concurrency.",
        "subtitle": "Why Rust is Revolutionizing Modern Software Development",
        "slug": "rust-modern-development",
        "content": "Rust is a high-performance, memory-safe programming language developed by Mozilla, designed to prevent common bugs like null pointer dereferences and data races. Its unique ownership model and strong type system ensure memory safety without a garbage collector, making it ideal for system-level programming, web assembly, and embedded systems.",
        "img_file": "rust.png",
    },
    {
        "title": "Generative AI: The Future of Intelligent Content Creation",
        "tagline": "AI-driven models that generate human-like text, images, and more.",
        "subtitle": "How Generative AI is Transforming Creativity and Automation",
        "slug": "generative-ai-content-creation",
        "content": "Generative AI refers to machine learning models that can create new content, including text, images, music, and even code. Based on deep learning techniques like transformers and GANs, these models power AI tools such as ChatGPT, Midjourney, and DALL·E.",
        "img_file": "ai.png",
    },
    {
        "title": "Artificial Intelligence: The Backbone of Smart Technologies",
        "tagline": "Machines that learn, adapt, and make intelligent decisions.",
        "subtitle": "Why AI is Shaping the Future of Technology",
        "slug": "artificial-intelligence-future-tech",
        "content": "Artificial Intelligence (AI) is a broad field of computer science focused on building machines capable of performing tasks that require human intelligence. AI includes machine learning, deep learning, natural language processing, and computer vision.",
        "img_file": "ai-tech.png",
    },
    {
        "title": "Flask: The Lightweight Web Framework for Python",
        "tagline": "A micro web framework designed for simplicity and flexibility.",
        "subtitle": "Why Flask is a Popular Choice for Python Web Development",
        "slug": "flask-python-web-framework",
        "content": "Flask is a minimalistic and lightweight web framework for Python that provides developers with full control over application design. It is based on Werkzeug and Jinja2, offering a simple yet powerful structure for building web applications and APIs.",
        "img_file": "flask.png",
    },
    {
        "title": "Django: The High-Level Web Framework for Rapid Development",
        "tagline": "A full-featured framework for secure and scalable web applications.",
        "subtitle": "Why Django is the Go-To Framework for Web Development",
        "slug": "django-web-development-framework",
        "content": "Django is a high-level Python web framework that follows the 'batteries-included' philosophy, providing built-in tools for authentication, database management, and security.",
        "img_file": "django.png",
    },
]

# Insert posts into database
for post in posts:
    new_post = Posts(
        title=post["title"],
        tagline=post["tagline"],
        subtitle=post["subtitle"],
        slug=post["slug"],
        content=post["content"],
        img_file=post["img_file"],
        date=datetime.utcnow(),
    )
    db.session.add(new_post)

db.session.commit()

print("Posts added successfully!")
