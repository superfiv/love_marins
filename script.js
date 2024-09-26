const ctaBtn = document.querySelector('.cta-btn');
const productsSection = document.querySelector('.products');

ctaBtn.addEventListener('click', () => {
  productsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
});
