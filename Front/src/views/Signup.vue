<template>
    <b-container class="container-login">
        <b-row class="justify-content-center text-center">
            <b-col cols="12" sm="8" md="6" lg="4">
                <b-form class="backgound-login" @submit="signupUser">    
                    <h3 class="title-login">Crear cuenta</h3>
                    <b-form-input type="text" class="input-login" required size="lg" v-model="Form.Nickname" placeholder="Nombre de usuario"></b-form-input>
                    <b-form-input type="email" class="input-login" required size="lg" v-model="Form.Email" placeholder="Correo electrónico"></b-form-input>
                    <b-form-input type="password" class="input-login" required size="lg" v-model="Form.Password" placeholder="Contraseña"></b-form-input>
                    <b-form-input type="password" class="input-login" required size="lg" v-model="Form.ConfirmPassword" placeholder="Confirmar contraseña"></b-form-input>
                    <b-button type="submit" size="lg" block variant="danger">Crear cuenta</b-button>
                    <hr /> 
                    <p>¿Ya tienes una cuenta?</p>
                    <b-button to="/signin" size="lg" block variant="dark">Iniciar sesión</b-button>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import axios from 'axios'

export default {
    data(){
      return{
        Form: {
          Nickname: "",
          Email: "",
          Password: "",
          ConfirmPassword: ""
        }
      }
    },
    created() {
        this.$store.commit('updateWindow', 'dark')
    },
    methods: {
        signupUser(event){

            event.preventDefault();

            if(this.Form.Nickname == "" || this.Form.Email == "" || this.Form.Password == "" || this.Form.ConfirmPassword == ""){
                
                alert("Datos invalidos")
            }
            else {

                if(this.Form.Password == this.Form.ConfirmPassword){

                    axios.post('http://127.0.0.1:8000/moviereview/user/signup/',{
                        "nickname": this.Form.Nickname,
                        "email": this.Form.Email,
                        "password": this.Form.Password})
                    .then(response => {
                        if(response.data.message == "USER CREATED"){
                            this.$store.dispatch('signupUser', {
                                Nickname: response.data.user.nickname,
                                Email: response.data.user.email,
                                Token: response.data.tokenId
                                });
                            this.$router.push("/profile")
                        }
                        else {
                            alert("El usuario ya existe")
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    })
                }
                else {

                    alert("Las contraseñas no son iguales")
                }
            }
            
        }
    }
}
</script>

<style>
.backgound-login{
    margin: 40px auto;
}

.title-login{
    margin-top: 20px;
    margin-bottom: 20px;
}

.input-login{
    margin-top: 10px;
    margin-bottom: 10px;
}

.container-login{
    margin-top: 10vh;
}
</style>