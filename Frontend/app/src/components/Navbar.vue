<template>
    <nav :class="styles[navbarIndex]">
        <div class="container">
            <a class="navbar-brand" v-on:click="changeView('/')">
                <img center src="../assets/MovieReviewLogo.png"/>
            </a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item"> 
                        <a class="nav-link" v-on:click="changeView('/search/movies')">
                            Películas
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" v-on:click="changeView('/search/series')">
                            Series
                        </a>
                    </li>
                </ul>
                <ul class="navbar-nav ml-auto">
                    <li v-if="user.isLogged == false" class="nav-item">
                        <button v-on:click="changeView('/login/signin')" class="btn btn-danger button-nav">Iniciar sesión</button>
                    </li>
                    <li v-if="user.isLogged == false" class="nav-item">
                        <button v-on:click="changeView('/login/signup')" class="btn btn-danger button-nav">Crear cuenta</button>
                    </li>
                    <li v-if="user.isLogged == true" class="nav-item">
                        <a class="nav-link profile-nav" v-on:click="goProfile()">
                            <svg class="bi bi-people-circle" width="2em" height="2em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 008 15a6.987 6.987 0 005.468-2.63z"/>
                                <path fill-rule="evenodd" d="M8 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/>
                                <path fill-rule="evenodd" d="M8 1a7 7 0 100 14A7 7 0 008 1zM0 8a8 8 0 1116 0A8 8 0 010 8z" clip-rule="evenodd"/>
                            </svg>
                        </a>
                    </li>
                    <li v-if="user.isLogged == true">
                        <button v-on:click="logout()" class="btn btn-danger button-nav">Cerrar sesion</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
    data() {
        return{
            styles: [
                "navbar navbar-expand-lg text-white bg-dark sticky-top",
                "navbar navbar-expand-lg text-white fixed-top",
                "navbar navbar-expand-lg text-white fixed-top bg-dark"]
        }
    },
    created() {
        this.$store.dispatch('checkLogin')
    },
    methods: {
        changeView(url) {
            this.$router.push(url);
        },
        logout() {
            this.$store.dispatch('signoutUser')
            this.$router.push("/")
        },
        goProfile() {
            this.$router.push("/profile")
        }
    },
    computed: {
        ...mapState(['user']),
        ...mapState(['navbarIndex']),
    }

}
</script>

<style>
.button-nav{
    margin: 10px;
}

.nav-link, .navbar-brand{
    cursor: pointer;
}

.profile-nav{
    margin-top: 5px;
}
</style>