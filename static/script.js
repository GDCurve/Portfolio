document.getElementById("uzApaksu").addEventListener("click", function() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });
});

function onRecaptchaSuccess() {
    document.getElementById("sending").disabled = false;
}

function newTab(url) {
    window.open(url);
}

