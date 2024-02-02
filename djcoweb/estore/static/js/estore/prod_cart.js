$(document).ready(function(){
    //var quantity;

    $('button.modify_cart').click(async function(e){
        //var element = document.getElementById('');
        e.preventDefault();
        var action = this.getAttribute("id").split(" ")[1];
        var prod_id = this.getAttribute("id").split(" ")[0];
        console.log(action, prod_id);
        var form;
        var method = "cart";
        try{
            var form_data = new FormData($(this).parent()[0])
            form = {method:'POST', body: form_data};
        }
        catch(error){
            form = null;
            method = "product";
        }
        console.log(form);
        await fetch("http://127.0.0.1:8000/" + method + "/" + action + '/' + prod_id, form)
            .then(response => response.json())
            .then(data => {
                console.log(data.error);
                if (data.error){
                    var product = this.getAttribute('data-bs-target').split('#')[1];
                    var element = document.getElementById(product);
                    var mod_mess = element.getElementsByClassName('modal-body')[0];
                    console.log(mod_mess);
                    if (mod_mess.innerHTML.trim() == ""){
                        mod_mess.innerHTML += "<div class=''><strong>" + product + ': ' + data.error + "</strong></div>";
                    }
                }
                else{
                    var element = document.getElementById(data.name + 'quantity');
                    console.log(method);
                    if (method != "cart"){
                        $(element).empty();
                        element.innerHTML += "Quantity: " + data.quantity;
                    }
                    else{
                        if (data.quantity == 0){
                            element = document.getElementById(data.name + "card")
                            $(element).remove();
                        }
                        else{
                            $(element).empty();
                            element.innerHTML += data.name + ' ' + data.price + ' x ' + data.quantity;
                        }
                        element = document.getElementById("cart_tot");
                        $(element).empty();
                        element.innerHTML += "Total: " + data.total;
                    }
                }
            })
            .catch(error => {
                console.log(error);
            })
    })
    /*document.getElementsByTagName('select')[0].addEventListener('change', function(){
        quantity[this.id] = this.value;
    })*/
})