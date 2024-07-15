const formContact = document.querySelector("#formContact");

const validarFormulario = (event) => {
    event.preventDefault(); 

    const firstname = document.querySelector("#firstname");
    const lastname = document.querySelector("#lastname");
    const email = document.querySelector("#email");
    let validation = true;

    if(firstname.value.trim() ===""){
        firstname.classList.add("error");
        document.querySelector("#error-firstname").textContent ="Debe completar el campo Nombre";
        validation = false;
    }
    if(lastname.value.trim()===""){
        document.querySelector("#error-lastname").textContent="Debe completar el campo Apellido";
        lastname.classList.add("error");
        validation= false;

    }
    if(email.value.trim()===""){
        // alert("Los campos Nombre, Apellido y Email son obligatorios")
        document.querySelector("#error-email").textContent='Debe completar el campo Email';
        email.classList.add('error')
        validation=false;
    }
    if(validation){
        formContact.submit()
    } else{
        return false;
    }

}
formContact.addEventListener("submit",validarFormulario)
