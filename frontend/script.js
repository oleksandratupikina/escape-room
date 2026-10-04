const btn = document.getElementById('btn-start');
const showPage = (pageId) => {
    const pages = document.getElementsByClassName('page');
    for (var i = 0; i < pages.length; i++) {
        pages[i].classList.remove('active'); 
    }
    const page = document.getElementById(pageId);
    page.classList.add('active');
}
btn.addEventListener('click', () => showPage('game-screen'));