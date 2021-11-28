$(document).ready(function() {

    $(".form").submit( event => {

        let isValid = true;

        const image = $("#image").val().trim();
        if (image == "") {
            $("#image").next().text("This field is required.");
            isValid = false;
        } else {
            $("#image").next().text("");
        }
        $("#image").val(image);  
        
        const name = $("#name").val().trim();
        if (name == "") {
            $("#name").next().text("This field is required.");
            isValid = false;
        } else {
            $("#name").next().text("");
        }
        $("#name").val(name);  

        const position = $("#position").val().trim();
        if (position == "") {
            $("#position").next().text("This field is required.");
            isValid = false;
        } else {
            $("#position").next().text("");
        }
        $("#position").val(position);  

        const team = $("#team").val().trim();
        if (team == "") {
            $("#team").next().text("This field is required.");
            isValid = false;
        } else {
            $("#team").next().text("");
        }
        $("#team").val(team);

        if (isValid == false) {
            event.preventDefault();                
            }
    });

    $(".form2").submit( event => {

        let isValid = true;

        
        const name = $("#name").val().trim();
        if (name == "") {
            $("#name").next().text("This field is required.");
            isValid = false;
        } else {
            $("#name").next().text("");
        }
        $("#name").val(name);  


        if (isValid == false) {
            event.preventDefault();                
            }
    });

});