/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */

function readImg( input ) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        var imgArea = document.getElementById("imageResult")

        reader.onload = function (e) {
            var dataUri = e.target.result
            imgArea.src = dataUri;
        };

        reader.readAsDataURL(input.files[0]);
        
        var fileName = input.files[0].name;
        var infoArea = document.getElementById( 'upload-label')
        infoArea.textContent = fileName;
    }
}
