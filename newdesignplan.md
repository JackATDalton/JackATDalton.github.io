Plan to implement                                                                                                                                       │
│                                                                                                                                                         │
│ Redesign Plan: JackATDalton.github.io                                                                                                                   │
│                                                                                                                                                         │
│ Context                                                                                                                                                 │
│                                                                                                                                                         │
│ Complete visual redesign toward a monospace + serif hybrid aesthetic. Inspired by:                                                                      │
│ - Brian Hie / Steinberger personal sites (narrow reading column, monospace, colored links)                                                              │
│ - EngBio conference site (monospace labels, bordered metadata)                                                                                          │
│ - Works in Progress / Centre for British Progress (editorial, horizontal rule dividers)                                                                 │
│                                                                                                                                                         │
│ User wants: reduced content, detailed bio (placeholder only), Book Meeting button, spelled-out email, recent publications + recent writing sections on  │
│ homepage, Science and Policy links. Community page already deleted.                                                                                     │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ Files Modified                                                                                                                                          │
│                                                                                                                                                         │
│ 1. stylesheets/style.css — complete rewrite                                                                                                             │
│ 2. index.html — structural redesign                                                                                                                     │
│ 3. scientific-projects.html — redesign (same system)                                                                                                    │
│ 4. policy-and-progress.html — redesign (same system)                                                                                                    │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ CSS Rewrite (style.css)                                                                                                                                 │
│                                                                                                                                                         │
│ Replace entirely. Key decisions:                                                                                                                        │
│                                                                                                                                                         │
│ Fonts (add to Google Fonts link on all pages):                                                                                                          │
│ - IBM Plex Mono — nav, labels, dates, email, section divider text, metadata                                                                             │
│ - Lora — headings (h1–h3), body text (already loaded)                                                                                                   │
│                                                                                                                                                         │
│ Layout:                                                                                                                                                 │
│ - Narrow centered reading column: max-width: 700px; margin: 0 auto; padding: 0 1.5rem                                                                   │
│ - No full-width hero block                                                                                                                              │
│ - body font: IBM Plex Mono at 0.95rem for nav/meta elements; Lora for prose                                                                             │
│                                                                                                                                                         │
│ Color palette (new — departure from current scheme):                                                                                                    │
│ - Background: #f5f0e8 (warm linen)                                                                                                                      │
│ - Text: #1e2d1e (deep forest green — warm, technical, distinctive)                                                                                      │
│ - Links/accent: #b85c2c (terracotta/rust — warm, editorial, Roots-of-Progress feel)                                                                     │
│ - Nav border: #1e2d1e at 30% opacity                                                                                                                    │
│ - Monospace labels: #1e2d1e at 70% opacity                                                                                                              │
│ - CSS variables updated: --color-bg, --color-text, --color-link                                                                                         │
│                                                                                                                                                         │
│ Nav:                                                                                                                                                    │
│ - Keep fixed, 70px height, cream background, bottom border                                                                                              │
│ - Switch to IBM Plex Mono, lowercase, smaller font size (~0.875rem)                                                                                     │
│ - Left: text links (home / cv / blog / science / policy)                                                                                                │
│ - Right: icon links (github, linkedin, orcid, scholar) — keep existing icon markup                                                                      │
│                                                                                                                                                         │
│ Section dividers:                                                                                                                                       │
│ - CSS class .section-label — monospace text + flex ::after pseudo-element filling remaining width with a thin border line                               │
│ - Matches the recent publications ──────── pattern from the mockup                                                                                      │
│ - Implemented via: display: flex; align-items: center; gap: 1rem + ::after { content: ''; flex: 1; border-top: 1px solid #373737; }                     │
│                                                                                                                                                         │
│ Homepage-specific:                                                                                                                                      │
│ - .bio-section — Lora body text, generous line-height, max 65ch                                                                                         │
│ - .contact-row — flexbox row: [Book a meeting] button + monospace email text                                                                            │
│ - Button: minimal, bordered, no fill; border: 1px solid #373737; padding: 8px 16px; font-family: IBM Plex Mono                                          │
│                                                                                                                                                         │
│ Section pages (Policy, Science):                                                                                                                        │
│ - .project-entry — replaces .project-item; no card/border/shadow; just heading + paragraph + link                                                       │
│ - .timeline-row — flex row: monospace year label (min-width: 4ch) + Lora content                                                                        │
│ - Project links: plain color: #01796b; text-decoration: underline text links, not pill buttons                                                          │
│ - Remove all border-radius, box-shadow, transform: translateY hover effects on content items                                                            │
│                                                                                                                                                         │
│ Footer: Keep as-is (org logo row). Just update border-top to use --color-accent.                                                                        │
│                                                                                                                                                         │
│ Cards (.card-grid / .work-card):                                                                                                                        │
│ - 2-column grid on desktop, 1-column on mobile                                                                                                          │
│ - .card-img-placeholder — fixed-height grey box (background: #d4cfc7; height: 180px) for image slots; user swaps in <img> later                         │
│ - .card-body — padding, monospace .card-meta label (year · venue), Lora <h3> title as link, small description <p>                                       │
│ - Border: 1px solid rgba(30,45,30,0.2), no border-radius, no hover lift effect                                                                          │
│                                                                                                                                                         │
│ Remove: .hero, .gallery-grid, .gallery-title, .content-item, .progress-grid, .progress-item, .progress-metric, .metric-number, .cta-section,            │
│ .button--outline, .subsection, .text, .image — all unused after redesign.                                                                               │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ index.html Redesign                                                                                                                                     │
│                                                                                                                                                         │
│ Structure:                                                                                                                                              │
│ <nav> — same links, remove "Community", keep social icons                                                                                               │
│                                                                                                                                                         │
│ <main>                                                                                                                                                  │
│   <section class="intro">                                                                                                                               │
│     <h1>Jack Dalton</h1>                                                                                                                                │
│     <p class="tagline">Engineering Biology for Planetary Health</p>                                                                                     │
│                                                                                                                                                         │
│     <!-- Bio: leave placeholder comment, no invented copy -->                                                                                           │
│     <div class="bio">                                                                                                                                   │
│       <!-- Add bio copy here -->                                                                                                                        │
│     </div>                                                                                                                                              │
│                                                                                                                                                         │
│     <div class="contact-row">                                                                                                                           │
│       <a href="https://calendly.com/jackdalton83/30min" class="button">Book a meeting</a>                                                               │
│       <span class="email">jack AT daltons DOT net</span>                                                                                                │
│     </div>                                                                                                                                              │
│   </section>                                                                                                                                            │
│                                                                                                                                                         │
│   <section class="index-section">                                                                                                                       │
│     <h2 class="section-label">recent publications</h2>                                                                                                  │
│     <div class="card-grid">                                                                                                                             │
│       <!-- Card with image placeholder -->                                                                                                              │
│       <div class="work-card">                                                                                                                           │
│         <div class="card-img-placeholder"></div>  <!-- user adds image later -->                                                                        │
│         <div class="card-body">                                                                                                                         │
│           <span class="card-meta">2023 · Protein Science</span>                                                                                         │
│           <h3><a href="https://doi.org/...">Applying ProteinMPNN, RFDiffusion & ColabFold...</a></h3>                                                   │
│           <p>J Kaczmarski, H Ashley, J Dalton et al.</p>                                                                                                │
│         </div>                                                                                                                                          │
│       </div>                                                                                                                                            │
│     </div>                                                                                                                                              │
│   </section>                                                                                                                                            │
│                                                                                                                                                         │
│   <section class="index-section">                                                                                                                       │
│     <h2 class="section-label">recent writing</h2>                                                                                                       │
│     <div class="card-grid">                                                                                                                             │
│       <div class="work-card">                                                                                                                           │
│         <div class="card-img-placeholder"></div>                                                                                                        │
│         <div class="card-body">                                                                                                                         │
│           <span class="card-meta">Substack</span>                                                                                                       │
│           <h3><a href="https://alivingfuture.substack.com/">Our Living Future →</a></h3>                                                                │
│           <p>Writing on human progress, biotechnology, and the future.</p>                                                                              │
│         </div>                                                                                                                                          │
│       </div>                                                                                                                                            │
│     </div>                                                                                                                                              │
│   </section>                                                                                                                                            │
│                                                                                                                                                         │
│   <section class="index-section">                                                                                                                       │
│     <h2 class="section-label">work</h2>                                                                                                                 │
│     <ul class="work-links">                                                                                                                             │
│       <li><a href="/scientific-projects.html">Scientific Projects →</a></li>                                                                            │
│       <li><a href="/policy-and-progress.html">Policy & Progress →</a></li>                                                                              │
│     </ul>                                                                                                                                               │
│   </section>                                                                                                                                            │
│ </main>                                                                                                                                                 │
│                                                                                                                                                         │
│ <footer> — unchanged                                                                                                                                    │
│                                                                                                                                                         │
│ Remove from index.html: .hero section entirely, .work-gallery section entirely.                                                                         │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ scientific-projects.html Redesign                                                                                                                       │
│                                                                                                                                                         │
│ - Remove teal hero, replace with plain <h1> + tagline in the content column                                                                             │
│ - "Research Focus Areas" grid → plain prose paragraphs or remove entirely (redundant with project descriptions)                                         │
│ - "Current Research Projects" → .project-list of .project-entry items (heading + short paragraph + plain text link)                                     │
│ - "Research Output" metrics grid → remove (2 publications / 6 talks feels thin as a stat block; mention in prose if needed)                             │
│ - "Previous Projects" timeline → .timeline-row entries: [year]  title  ›                                                                                │
│ - Remove Community link from nav                                                                                                                        │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ policy-and-progress.html Redesign                                                                                                                       │
│                                                                                                                                                         │
│ - Remove teal hero, replace with plain <h1> + tagline                                                                                                   │
│ - "Policy Focus Areas" grid → remove (redundant with the work items below)                                                                              │
│ - "Previous Work" → clean .project-entry list; group government work under a monospace sub-label (e.g., Australian Government)                          │
│ - Remove Community link from nav                                                                                                                        │
│                                                                                                                                                         │
│ ---                                                                                                                                                     │
│ Verification                                                                                                                                            │
│                                                                                                                                                         │
│ 1. Run ./start-server.sh and open http://localhost:8000                                                                                                 │
│ 2. Check: narrow centered column, IBM Plex Mono nav, Lora headings, teal links, no teal hero                                                            │
│ 3. Check: index has bio placeholder, Book Meeting button, email spelled out, publications, writing, work sections                                       │
│ 4. Check: Science + Policy pages render cleanly without card styles                                                                                     │
│ 5. Check: Community link gone from all navs                                                                                                             │
│ 6. Check: footer org logos still present                                                                                                                │
│ 7. Resize to mobile — column should stack cleanly 