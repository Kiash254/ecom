var updateBtn = document.getElementsByClassName('update-btn');

for (var i = 0; i < updateBtn.length; i++) {
updateBtn[i].addEventListener('click', function(e) {
var productId = this.dataset.product
var actions = this.dataset.action
console.log(" productid",productId,"actions", actions)
});

}
