# Jack Dalton's Portfolio Website

A modern, IFP-inspired portfolio website showcasing work in biotechnology, policy, and scientific research.

## 🚀 Local Development

### Quick Start

1. **Start the development server:**
   ```bash
   ./start-server.sh
   ```
   
   Or manually:
   ```bash
   python3 local-server.py
   ```

2. **Open your browser** to `http://localhost:8000`

3. **Make changes** to your files and refresh the browser to see updates

### File Structure

```
├── index.html              # Main homepage
├── stylesheets/
│   └── style.css           # IFP-inspired stylesheet
├── _layouts/
│   └── standard.html       # Jekyll layout template
├── _includes/
│   ├── navbar.html         # Navigation component
│   └── footer.html         # Footer component
├── assets/                 # Images and documents
├── icons/                  # Logo and icon files
├── local-server.py         # Development server script
└── start-server.sh         # Server startup script
```

## 🎨 Design Features

### IFP-Inspired Design
- **Color Palette**: Cream background (#FCFBE8), dark text (#373737)
- **Typography**: Söhne for body text, Lora for headings
- **Layout**: Clean, minimal design with responsive grid system
- **Navigation**: Fixed header with smooth transitions

### Key Components
- **Hero Section**: Purple gradient background with prominent call-to-action
- **Content Sections**: Alternating layout with images and text
- **Responsive Design**: Mobile-first approach with breakpoints
- **Footer**: Dark background with organization logos

## 🛠 Customization

### Colors
Edit the CSS custom properties in `stylesheets/style.css`:
```css
:root {
    --color-accent: #373737;
    --color-body-background: #FCFBE8;
    --color-hero-background: #B17ADA;
}
```

### Content
- Edit `index.html` for homepage content
- Modify `_includes/navbar.html` for navigation links
- Update `_includes/footer.html` for footer content

### Images
- Place images in the `assets/` folder
- Update image paths in HTML files
- Logos go in the `icons/` folder

## 📱 Responsive Breakpoints

- Mobile: < 980px
- Tablet: 980px - 1024px  
- Desktop: > 1024px

## 🔧 Development Tips

1. **Cache**: The development server disables caching for easier development
2. **File Watching**: Manually refresh browser after making changes
3. **Jekyll Variables**: The site uses Jekyll for templating (if deploying with Jekyll)

## 🚀 Deployment

This site is designed to work with:
- GitHub Pages (Jekyll)
- Netlify
- Vercel
- Any static hosting service

## 📝 Notes

- The design is inspired by the Institute for Progress (IFP) website
- Optimized for modern browsers with CSS Grid and Flexbox
- Includes smooth scrolling and hover effects
- All images should have appropriate alt text for accessibility

---

**Built with ❤️ by Jack Dalton**

## Featured projects

The homepage carousel is a native horizontal scroll list in `index.html` with
optional controls from `scripts/project-carousel.js`. Add a sibling
`li.featured-project` for each new project; controls appear automatically when
there is more than one. It never rotates automatically and works without
JavaScript. Keep the app link, source link and image alt text with each entry.

`assets/opentrons-simulate.svg` is a vector figure rendered from the protocol
builder's real `SimulationViewer` and a 24-well Golden Gate example, at step
86. It is not a simulator-validation result; it shows the step visualisation.
The same figure is used on the Scientific Projects page.
