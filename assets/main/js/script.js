const wrapper = document.querySelector(".wrapper"),
      qrInput = wrapper.querySelector(".form input"),
      generateBtn = wrapper.querySelector(".form button"),
      qrImg = wrapper.querySelector(".qr-code img"),
      downloadBtn = wrapper.querySelector(".download-btn");

let preValue;

// Hide the download button initially
downloadBtn.style.display = "none";

generateBtn.addEventListener("click", async () => {
    let qrValue = qrInput.value.trim();
    if (!qrValue || preValue === qrValue) return;
    preValue = qrValue;
    generateBtn.innerText = "Generating QR Code...";
    const qrCodeURL = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${qrValue}`;
    qrImg.src = qrCodeURL;

    qrImg.addEventListener("load", () => {
        wrapper.classList.add("active");
        generateBtn.innerText = "Generate QR Code";
        downloadBtn.style.display = "inline-block"; // Show the download button
    });
});

downloadBtn.addEventListener("click", async () => {
    const qrCodeURL = qrImg.src;
    if (!qrCodeURL) return alert("Generate a QR Code first!");

    // Fetch the QR code image as a Blob
    const response = await fetch(qrCodeURL);
    const blob = await response.blob();

    // Create a link element and trigger a download
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `QR_Code.png`;
    document.body.appendChild(link);
    link.click();
    link.remove();
});
