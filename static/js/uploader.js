/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */

function getImgName( input ) {
    if (input.files && input.files[0]) {
        var fileName = input.files[0].name;
        var infoArea = document.getElementById( 'upload-label')
        infoArea.textContent = fileName;
    }
}
