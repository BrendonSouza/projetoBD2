const textarea = document.querySelector("textarea");
textarea.addEventListener("keydown", function (event) {
    if (event.key === "Tab") {
        event.preventDefault();
        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        textarea.value =
            textarea.value.substring(0, start) +
            "\t" +
            textarea.value.substring(end);
        textarea.selectionStart = start + 1;
        textarea.selectionEnd = start + 1;
    }
});
