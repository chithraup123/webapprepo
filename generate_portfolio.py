import re
from pathlib import Path
try:
    from PyPDF2 import PdfReader
except Exception:
    raise SystemExit("Install PyPDF2: pip install PyPDF2")

HERE = Path(__file__).resolve().parent
PDF = HERE.parent / "Profile.pdf"
OUT_HTML = HERE / "index.html"
OUT_CSS = HERE / "style.css"
OUT_JS = HERE / "script.js"

def extract_text(path):
    if not path.exists(): 
        return ""
    r = PdfReader(str(path))
    return "\n\n".join(p.extract_text() or "" for p in r.pages).strip()

def first_line(text):
    for l in text.splitlines():
        if l.strip():
            return l.strip()
    return "Your Name"

def find_email(text):
    m = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return m.group(0) if m else "you@example.com"

txt = extract_text(PDF)
name = first_line(txt)
email = find_email(txt)
about = ("\n\n".join([p.strip() for p in txt.split("\n\n")][:4]) or "About section not found in Profile.pdf").replace("\n"," ")

HTML = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{name} — Portfolio</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <div class="brand">
        <h1>{name}</h1>
        <p class="tagline">Portfolio</p>
      </div>
      <nav id="siteNav" class="site-nav">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
      </nav>
      <button id="navToggle" class="nav-toggle" aria-label="Toggle navigation">☰</button>
    </div>
  </header>

  <main class="container">
    <section id="about" class="section">
      <h2>About</h2>
      <p>{about}</p>
    </section>

    <section id="projects" class="section">
      <h2>Projects</h2>
      <div class="projects-grid">
        <article class="project-card">
          <h3>Project 1</h3>
          <p>Summary — edit to add real projects from Profile.pdf.</p>
        </article>
        <article class="project-card">
          <h3>Project 2</h3>
          <p>Summary — edit to add real projects from Profile.pdf.</p>
        </article>
      </div>
    </section>

    <section id="contact" class="section">
      <h2>Contact</h2>
      <p>Email: <a href="mailto:{email}">{email}</a></p>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; {name}</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""

CSS = """/* filepath: d:\\Learning\\learning_ai\\portfolio_site\\style.css */
*{box-sizing:border-box}
body{font-family:Inter,system-ui,Segoe UI,Arial;line-height:1.5;color:#222;margin:0;background:#f7fafc}
.container{width:92%;max-width:1100px;margin:0 auto}
.site-header{background:linear-gradient(90deg,#0f172a,#0b1220);color:#fff;position:sticky;top:0;z-index:10}
.header-inner{display:flex;align-items:center;justify-content:space-between;padding:.8rem 0}
.brand h1{margin:0;font-size:1.25rem}
.brand .tagline{margin:0;font-size:0.85rem;color:#aab3c4}
.site-nav a{color:#e6eef8;text-decoration:none;margin-left:1.25rem;font-weight:600}
.nav-toggle{display:none;background:none;border:none;color:#fff;font-size:1.4rem}
.section{padding:2rem 0;border-bottom:1px solid #eef2f7;background:transparent}
.projects-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin-top:1rem}
.project-card{padding:1rem;border-radius:8px;background:#fff;box-shadow:0 6px 18px rgba(12,20,30,.06)}
.site-footer{background:#071226;color:#9fb0c8;text-align:center;padding:1rem 0;margin-top:2rem}

/* Responsive */
@media (max-width:900px){
  .site-nav{display:none;width:100%;flex-direction:column;margin-top:.6rem}
  .site-nav.show{display:flex}
  .nav-toggle{display:block}
  .projects-grid{grid-template-columns:1fr}
}
"""

JS = """// filepath: d:\\Learning\\learning_ai\\portfolio_site\\script.js
document.addEventListener('DOMContentLoaded',function(){
  const navToggle = document.getElementById('navToggle');
  const siteNav = document.getElementById('siteNav');
  navToggle.addEventListener('click',()=>siteNav.classList.toggle('show'));
});
"""

OUT_HTML.write_text(HTML, encoding="utf-8")
OUT_CSS.write_text(CSS, encoding="utf-8")
OUT_JS.write_text(JS, encoding="utf-8")
print("Generated:", OUT_HTML)