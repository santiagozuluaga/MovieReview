<template>
    <b-container class="container-login">
        <b-row class="justify-content-center text-center">
            <b-col cols="12" sm="8" md="6" lg="4">
                <b-form class="backgound-login" @submit="signinUser">    
                    <h3 class="title-login">Iniciar sesión</h3>
                    <b-form-input type="email" class="input-login" required size="lg" v-model="Form.Email" placeholder="Correo electrónico"></b-form-input>
                    <b-form-input type="password" class="input-login" required size="lg" v-model="Form.Password" placeholder="Contraseña"></b-form-input>
                    <b-button type="submit" size="lg" block variant="danger">Iniciar sesión</b-button>
                    <hr /> 
                    <p>¿Aún no tienes cuenta?</p>
                    <b-button to="signup" size="lg" block variant="dark">Crear cuenta</b-button>
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
          Email: "",
          Password: ""
        }
      }
    },
    created() {
        this.$store.commit('updateWindow', 'dark')
    },
    methods: {
        signinUser(event){
            event.preventDefault();

            if(this.Form.Email == "" || this.Form.Password == ""){
                
                alert("Datos invalidos")
            }
            else {
                
                axios.post('http://127.0.0.1:8000/moviereview/user/signin/',{
                    "email": this.Form.Email,
                    "password": this.Form.Password})
                .then(response => {
                    if(response.data.message == "USER FOUND"){
                        this.$store.dispatch('signinUser', {
                            Nickname: response.data.user.nickname,
                            Email: response.data.user.email,
                            Token: response.data.tokenId
                            });
                        this.$router.push("/profile")
                    }
                    else {
                        alert("El usuario no existe")
                    }
                })
                .catch(error => {
                    console.log(error);
                })
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
    margin-top: 15px;
    margin-bottom: 15px;
}

.container-login{
    margin-top: 10vh;
}
</style>