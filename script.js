// filepath: d:\Learning\learning_ai\portfolio_site\script.js
document.addEventListener('DOMContentLoaded',function(){
  const navToggle = document.getElementById('navToggle');
  const siteNav = document.getElementById('siteNav');
  navToggle.addEventListener('click',()=>siteNav.classList.toggle('show'));
});
