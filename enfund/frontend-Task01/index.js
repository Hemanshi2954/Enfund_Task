document.getElementById('toggleMenu').addEventListener('click', function() {
    const leftMenu = document.getElementById('leftMenu');
    const maincontainer = document.getElementById('mainContainer');
    const RightMenu = document.getElementById('rightPanel');
    leftMenu.classList.toggle('collapsed');
    maincontainer.classList.toggle('expanded');
    RightMenu.classList.togglr('same');
});

function adjustPageWidth() {
    const width = window.innerWidth;
    const body = document.body;

    if (width >= 992 && width <= 1600) {
        body.style.transform = 'scale(0.9)';
        body.style.transformOrigin = 'top left';
    } else if (width >= 700 && width < 992) {
        body.style.transform = 'scale(0.8)';
        body.style.transformOrigin = 'top left';
    } else if (width >= 600 && width < 700) {
        body.style.transform = 'scale(0.75)';
        body.style.transformOrigin = 'top left';
    } else if (width <= 600) {
        body.style.transform = 'scale(0.5)';
        body.style.transformOrigin = 'top left';
    } else {
        body.style.transform = 'none'; 
    }
}


window.onload('load', adjustPageWidth);
window.onresize('resize', adjustPageWidth);