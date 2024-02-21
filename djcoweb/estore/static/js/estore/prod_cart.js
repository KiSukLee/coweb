$(document).ready(function(){
    $('button').click(function(event){
        event.preventDefault();
    })
    
    const myModal = document.getElementsByClassName('modal')[0];
    const modal = new bootstrap.Modal(myModal);

    myModal.addEventListener('show.bs.modal', function(event){
        var button = event.relatedTarget;
        var product = button.getAttribute('data-bs-product')
        console.log(product);
        var action = button.getAttribute("id").split(" ")[1];
        var prod_id = button.getAttribute("id").split(" ")[0];
        var form;
        var method = "cart";
        try{
            var form_data = new FormData($(button).parent()[0])
            form = {method:'POST', body: form_data};
        }
        catch(error){
            form = null;
            method = "product";
        }
        fetch_data(method, action, product, prod_id, form);

    })

    async function fetch_data(method, action, product, prod_id, form){
        var response =  await fetch("http://127.0.0.1:8000/" + method + "/" + action + '/' + prod_id, form)
        var data = await response.json();
        var element = document.getElementsByClassName('modal')[0];
        var mod_mess = element.getElementsByClassName('modal-body')[0];
        try{
            if (data.error){
                if (mod_mess.innerHTML.trim() == "" || mod_mess.innerHTML != data.error){
                    $(mod_mess).empty();
                    mod_mess.innerHTML += "<div class=''><strong>" + product + ': ' + data.error + "</strong></div>";
                }
                
            }
            else{
                var element = document.getElementById(data.name + 'quantity');
                console.log(method);
                $(mod_mess).empty();
                if (action == 'add'){
                    mod_mess.innerHTML += "<div class=''><strong>" + product + ': Successfully added to cart</strong></div>';
                }
                else{
                    mod_mess.innerHTML += "<div class=''><strong>" + product + ': Successfully removed from cart</strong></div>';
                }
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
        }catch(error){
            $(mod_mess).empty();
            mod_mess.innerHTML += "<div class=''><strong> Please select amount to add to/remove from cart </strong></div>";
        }
    }
})