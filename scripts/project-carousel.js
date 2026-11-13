// Native scrolling keeps the project list usable without JavaScript.
for (const carousel of document.querySelectorAll('[data-project-carousel]')) {
  const track = carousel.querySelector('.project-carousel-track');
  const slides = [...track.children];
  const controls = carousel.querySelector('.project-carousel-controls');
  const previous = carousel.querySelector('[data-project-prev]');
  const next = carousel.querySelector('[data-project-next]');
  const status = carousel.querySelector('[data-project-status]');
  if (slides.length < 2) continue;
  controls.hidden = false;
  let current = 0;
  const update = () => {
    const left = track.getBoundingClientRect().left;
    current = slides.reduce((best, slide, index) =>
      Math.abs(slide.getBoundingClientRect().left - left) < Math.abs(slides[best].getBoundingClientRect().left - left) ? index : best, 0);
    previous.disabled = current === 0;
    next.disabled = current === slides.length - 1;
  };
  const move = (direction) => {
    const target = Math.max(0, Math.min(slides.length - 1, current + direction));
    const offset = slides[target].getBoundingClientRect().left - track.getBoundingClientRect().left;
    track.scrollBy({ left: offset, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    status.textContent = `Project ${target + 1} of ${slides.length}: ${slides[target].querySelector('h3').textContent}`;
  };
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  track.addEventListener('keydown', (event) => {
    if (event.target !== track) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
      event.preventDefault();
      move(event.key === 'ArrowRight' ? 1 : -1);
    }
  });
  track.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
}
