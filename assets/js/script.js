var enviar = document.getElementById("btn_enviar");
enviar.addEventListener("click", function() {
    error = false
    if($("#nombre_input").val()==""){
        error = true
        $(".modal-header").addClass("alert-danger")
        $("#nombre_input").addClass("is-invalid")
    }else{
        $(".modal-header").removeClass("alert-danger")
        $("#nombre_input").removeClass("is-invalid");
    }
    if($("#asunto_input").val()==""){
        error = true
        $(".modal-header").addClass("alert-danger")
        $("#asunto_input").addClass("is-invalid")
    }else{
        $(".modal-header").removeClass("alert-danger")
        $("#asunto_input").removeClass("is-invalid");
    }
    if($("#mensaje_textarea").val()==""){
        error = true
        $(".modal-header").addClass("alert-danger")
        $("#mensaje_textarea").addClass("is-invalid")
    }else{
        $(".modal-header").removeClass("alert-danger")
        $("#mensaje_textarea").removeClass("is-invalid");
    }
    if(error){
        $("#mensaje_modal").html("Complete los campos vacios..");
        $("#alertCorreo").modal("show");
    }else{
        $(".modal-header").addClass("alert-success");    
        $("#mensaje_modal").html("<strong>"+$("#nombre_input").val()+"</strong> Tu Mensaje fue enviado correctamente<br><strong>Asunto: </strong>"+$("#asunto_input").val()+"<br><strong>Mensaje: </strong>"+$("#mensaje_textarea").val());
        $("#alertCorreo").modal("show");
        $("#nombre_input").val("");
        $("#asunto_input").val("");
        $("#mensaje_textarea").val("");
    }
});
