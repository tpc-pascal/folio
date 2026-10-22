function selectBook(f) {
    var el = document.querySelector('#hf-hidden input') || document.querySelector('#hf-hidden textarea');
    if (!el) return;
    el.value = f;
    el.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
    var shelf = document.querySelector('#shelf-col');
    var reader = document.querySelector('#reader-col');
    if (shelf) shelf.style.display = 'none';
    if (reader) reader.style.display = 'flex';
}
document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
        var b = document.querySelector('#pg-prev button');
        if (b) b.click();
    } else if (e.key === 'ArrowRight') {
        var b = document.querySelector('#pg-next button');
        if (b) b.click();
    } else if (e.key === 'Escape') {
        if (document.fullscreenElement) return;
        var s = document.querySelector('#shelf-col');
        var r = document.querySelector('#reader-col');
        if (s) s.style.display = '';
        if (r) r.style.display = 'none';
        var b = document.querySelector('#reader-back button');
        if (b) b.click();
    } else if (e.key === 'f' || e.key === 'F') {
        var b = document.querySelector('#fullscreen-btn button');
        if (b) b.click();
    }
});
document.addEventListener('click', function(e) {
    if (e.target.closest('#reader-back, #reader-back button')) {
        var s = document.querySelector('#shelf-col');
        var r = document.querySelector('#reader-col');
        if (s) s.style.display = '';
        if (r) r.style.display = 'none';
    }
    if (e.target.closest('#fullscreen-btn, #fullscreen-btn button')) {
        var el = document.querySelector('#reader-view');
        if (!document.fullscreenElement) {
            (el.requestFullscreen || el.webkitRequestFullscreen || el.msRequestFullscreen)?.call(el);
        } else {
            (document.exitFullscreen || document.webkitExitFullscreen || document.msExitFullscreen)?.call(document);
        }
    }
});
function setupPageOverlay() {
    var rv = document.querySelector('#reader-view');
    if (!rv) return;
    if (!rv.querySelector('#fs-page-overlay')) {
        var ov = document.createElement('div');
        ov.id = 'fs-page-overlay';
        ov.innerHTML = '<span id="fs-page-text">0 / 0</span>';
        rv.appendChild(ov);
    }
}
function syncPageOverlay() {
    var src = document.querySelector('#reader-page-info p');
    var dst = document.querySelector('#fs-page-text');
    if (src && dst) dst.textContent = src.textContent;
}
setupPageOverlay();
syncPageOverlay();
setInterval(syncPageOverlay, 500);
document.addEventListener('click', function(e) {
    if (e.target.closest('[onclick*="selectBook"]')) {
        setTimeout(setupPageOverlay, 50);
        setTimeout(syncPageOverlay, 100);
    }
});
