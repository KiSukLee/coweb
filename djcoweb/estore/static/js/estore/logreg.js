$(document).ready(function(){

    $('form').submit(async function(e){
        
        //Problem w/ initial approach
            // with await/async form is submitted regardless of what v is when returned
                //since the function is asynchronous, the form is submitted by default before the return value
            // without, vice versa
                //since the fetch method is asynchronous but not the function, the value that has been assigned
                //during its declaration is returned before the method catches an error
            
            //return v
        
        //Solution
            //adding .preventDefault() at the beginning prevents the form from being submitted
            //unless it is manually submitted at the end after validation
        
        e.preventDefault();
        var v = false;
        var d = {};
        var form = new FormData(this);
        await fetch("http://127.0.0.1:8000/logreg/validate", {method:'POST', body:form})
            .then(response => response.json())
            .then(data => {
                console.log(data)
                d = data;
            })
            .catch(error =>{
                if (error){
                    console.log(error);
                    v = true;
                }
            })
        console.log(v);

        // Manually submit the form if v is true
        if (v) {
            this.submit();
        }
        else{
            
            for (var key in d){
                console.log(key, d[key]);
                
                //Form Validation
                //var element = document.getElementById(key);
                //if (element.getElementsByClassName("invalid-feedback").length < 1){
                //    element.innerHTML += "<div id='" + key + "'" + "class='invalid-feedback'>" + d[key] + "</div>";
                
                //Modal
                //var element = document.getElementsByClassName("modal-body")[0];
                //error = document.querySelector('#m' + key);            
                //if (error == null){
                //    element.innerHTML += "<div id='m" + key + "'>" + d[key] + "</div>";
                //}
            }
            //$(this).addClass('was-validated');
        }
    })

})
        