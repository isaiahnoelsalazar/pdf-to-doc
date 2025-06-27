function updateLabel(input){
    const label = document.querySelector("label[for='file-upload']");
    if (input.files && input.files.length > 0) {
        label.textContent = input.files[0].name;
    } else {
        label.textContent = "Choose PDF File";
    }
}