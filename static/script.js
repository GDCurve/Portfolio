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

document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const sendButton = document.getElementById("sending");

    fetch("/send-email", {  
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === "ziņa nosūtīta") { 
            sendButton.textContent = "Ziņa nosūtīta";
            sendButton.disabled = true;
        }
    })
    .catch(error => {
        console.error("err:", error);
        alert("err");
    });
});

