function changeLanguage() {
    selected = document.getElementById('langId').value;
    document.cookie = "lang=" + selected + "; domain=;path=/"
    location.reload()
}

function setLanguage() {
    let lang = getLang()
    if (lang == '') {
        changeLanguage()
    }
    var language = document.getElementById('langId');
    for(var i, j = 0; i = language.options[j]; j++) {
        if(i.value == lang) {
            language.selectedIndex = j;
            break;
        }
    }
}

function getLang() {
    let name = "lang=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }

    return "";
}

setLanguage()