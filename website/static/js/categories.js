function changeCategory() {
    let lang = "Education"
    selected = document.getElementById('categoryFilter').value;
    console.log(selected)
    window.location.replace("/blogs/" + selected);

}

// 

function selectedCategory () {
    let cat = window.location.pathname.split("/").pop();
    var category = document.getElementById('categoryFilter');
    for(var i, j = 0; i = category.options[j]; j++) {
        if(i.value == cat) {
            category.selectedIndex = j;
            break;
        }
    }
    if (cat == "all"){
        category.selectedIndex = 0;
    }
}

selectedCategory()