<template>
    <div class="container login">
        <div class="row justify-content-center text-center">
            <div class="col col-sm-8 col-md-6 col-lg-4">
                <div class="form-login" v-if="currentView == 'signin'">
                    <form>
                        <h3 class="title-login">Iniciar sesión</h3>
                        <input class="form-control form-control-lg input-login" type="email" v-model="Form.Email" placeholder="Correo electrónico">
                        <input class="form-control form-control-lg input-login" type="password" v-model="Form.Password" placeholder="Contraseña">
                        <button class="btn btn-danger btn-lg btn-block" v-on:click="signinUser">Iniciar sesión</button>
                        <hr /> 
                        <p>¿Aún no tienes cuenta?</p>
                        <button class="btn btn-dark btn-lg btn-block" v-on:click="changeView">Crear cuenta</button>
                    </form>
                </div>
                <div class="form-login" v-if="currentView == 'signup'">
                    <form>
                        <h3 class="title-login">Crear cuenta</h3>
                        <input class="form-control form-control-lg input-login" type="text" v-model="Form.Nickname" placeholder="Nombre de usuario">
                        <input class="form-control form-control-lg input-login" type="email" v-model="Form.Email" placeholder="Correo electrónico">
                        <input class="form-control form-control-lg input-login" type="password" v-model="Form.Password" placeholder="Contraseña">
                        <input class="form-control form-control-lg input-login" type="password" v-model="Form.ConfirmPassword" placeholder="Confirmar contraseña">
                        <button class="btn btn-danger btn-lg btn-block" v-on:click="signupUser">Crear cuenta</button>
                        <hr /> 
                        <p>¿Ya tienes una cuenta?</p>
                        <button class="btn btn-dark btn-lg btn-block" v-on:click="changeView">Iniciar sesión</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/configproject.js'

export default {
    props: ["currentView"],
    data () {
        return{
            View: this.$props.currentView,
            Form: {
                Nickname: "",
                Email: "",
                Password: "",
                ConfirmPassword: ""
            },
            URL_BACKEND: config.URL_BACKEND
        }
    },
    created() {
        window.scrollTo(0, 0);
        this.$store.commit('updateNavbarIndex', 0);
    },
    updated() {
        if(this.View != this.$props.currentView){
            this.resetData();
        }
    },
    methods:{
        resetData() {
            this.View = this.$props.currentView
            this.Form = {
                Nickname: "",
                Email: "",
                Password: "",
                ConfirmPassword: ""
            }
        },
        signinUser(event) {
            event.preventDefault();

            if(this.checkSignin()){

                axios.post(this.URL_BACKEND + 'user/signin',{
                    "email": this.Form.Email,
                    "password": this.Form.Password})
                .then(response => {

                    if(response.data.signinCorrect == true){
                        this.$store.dispatch('signinUser', {
                            Nickname: response.data.user.nickname,
                            Email: response.data.user.email
                        });
                        this.$router.push("/");
                    }
                    else {
                        alert("El usuario no existe")
                    }
                    
                })
                .catch(error => {
                    console.log(error);
                })
            }
            else {
                alert("Ingrese datos validos");
            }
        },
        signupUser(event) {
            event.preventDefault();
            
            if(this.checkSignup()){

                axios.post(this.URL_BACKEND + 'user/signup',{
                    "nickname": this.Form.Nickname,
                    "email": this.Form.Email,
                    "password": this.Form.Password})
                .then(response => {
                    
                    if(response.data.signupCorrect == true){
                        this.$store.dispatch('signupUser', {
                            Nickname: response.data.user.nickname,
                            Email: response.data.user.email
                        });
                        this.$router.push("/")
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
                alert("Ingrese datos validos");
            }
        },
        changeView(event){

            event.preventDefault();

            this.Form.Nickname = "";
            this.Form.Email = "";
            this.Form.Password = "";
            this.Form.ConfirmPassword = "";

            if(this.$props.currentView == 'signin'){
                this.$router.push("/login/signup");
            }
            else {
                this.$router.push("/login/signin");
            }
        },
        checkSignin() {
             if(this.Form.Email == "" || this.Form.Password == ""){
                
                return false;
            }
            else {

                return true;
            }
        },
        checkSignup() {
            if(this.Form.Nickname == "" || this.Form.Email == "" || this.Form.Password == "" || this.Form.ConfirmPassword == ""){

                return false;
            }
            else {
                
                if(this.Form.Password == this.Form.ConfirmPassword) {

                    return true;
                }
                else {

                    return false;
                }
            }
        }
    }
}
</script>

<style>
.login{
    margin-top: 20px;
}

.title-login{
    margin-top: 20px;
    margin-bottom: 20px;
}

.input-login{
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>