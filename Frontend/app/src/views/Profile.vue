<template>
    <div class="profile">
        <div class="container">
            <div class="row justify-content-center">

                <div class="col col-12 col-lg-4">
                    <div class="text-center card-profile">
                        <div>
                            <svg class="bi bi-people-circle text-white" width="10em" height="10em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path d="M13.468 12.37C12.758 11.226 11.195 10 8 10s-4.757 1.225-5.468 2.37A6.987 6.987 0 008 15a6.987 6.987 0 005.468-2.63z"/>
                                <path fill-rule="evenodd" d="M8 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/>
                                <path fill-rule="evenodd" d="M8 1a7 7 0 100 14A7 7 0 008 1zM0 8a8 8 0 1116 0A8 8 0 010 8z" clip-rule="evenodd"/>
                            </svg>
                        </div>
                        <div>
                            <h3 class="text-center text-white">{{user.userNickname}}</h3>
                            <div class="text-center options-profile">
                                <span v-on:click="changeView(0)">Favoritos</span>
                                <span v-on:click="changeView(1)">Editar perfil</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col col-12 col-lg-8">
                    <div class="container">
                        <div class="row">
                            <div class="col col-12 card-profile-media profile-view" v-if="currentView == 1">
                                <h3 class="text-center">Actualizar contraseña</h3>
                                <hr />
                                <form class="updateprofile">
                                    <input class="form-control" type="password" v-model="User.oldpassword" placeholder="Antigua contraseña">
                                    <input class="form-control" type="password" v-model="User.password" placeholder="Nueva contraseña">
                                    <input class="form-control" type="password" v-model="User.confirmPassword" placeholder="Confirmar contraseña">
                                    <button v-on:click="updatePassword" class="btn btn-danger btn-lg btn-block">Actualizar contraseña</button>
                                </form>
                            </div>

                            <div class="col col-12 card-profile-media profile-movies" v-if="currentView == 0">
                                <h3 class="text-center">Peliculas favoritas</h3>
                                <div v-if="favoritesMovies.length == 0">
                                    <p class="text-center">No has agregado nada aun</p>
                                </div>
                                <div v-if="favoritesMovies.length != 0">
                                    <table class="table table-striped text-white text-center">
                                        <thead>
                                        <tr>
                                            <th>Id</th>
                                            <th>Nombre</th>
                                            <th>Detalles</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <tr v-bind:key="movies.id" v-for="movies in favoritesMovies">
                                            <td>{{movies.id}}</td>
                                            <td>{{movies.nombre}}</td>
                                            <td>
                                                <button v-on:click="seeDetails('/movie/'+movies.id)" class="btn btn-danger">
                                                    <svg class="bi bi-eye-fill" width="1.2em" height="1.2em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                        <path d="M10.5 8a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
                                                        <path fill-rule="evenodd" d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 100-7 3.5 3.5 0 000 7z" clip-rule="evenodd"/>
                                                    </svg>
                                                </button>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div class="col col-12 card-profile-media profile-series" v-if="currentView == 0">
                                <h3 class="text-center">Series favoritas</h3>
                                <hr>
                                <div v-if="favoirtesSeries.length == 0">
                                    <p class="text-center">No has agregado nada aun</p>
                                </div>
                                <div v-if="favoirtesSeries.length != 0">
                                    <table class="table table-striped text-white text-center">
                                        <thead>
                                        <tr>
                                            <th>Id</th>
                                            <th>Nombre</th>
                                            <th>Detalles</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        <tr v-bind:key="series.id" v-for="series in favoirtesSeries">
                                            <td>{{series.id}}</td>
                                            <td>{{series.nombre}}</td>
                                            <td>
                                                <button v-on:click="seeDetails('/serie/'+series.id)" class="btn btn-danger">
                                                    <svg class="bi bi-eye-fill" width="1.2em" height="1.2em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                                        <path d="M10.5 8a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
                                                        <path fill-rule="evenodd" d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 100-7 3.5 3.5 0 000 7z" clip-rule="evenodd"/>
                                                    </svg>
                                                </button>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>  
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import config from '@/config/configproject.js'

export default {
    data() {
        return {
            User: {
                oldpassword: "", 
                password: "",
                confirmPassword: "",
            },
            currentView: 0,
            favoritesMovies: [],
            favoirtesSeries: [],
            API_KEY_THEMOVIEDB: config.API_KEY_THEMOVIEDB,
            URL_BACKEND: config.URL_BACKEND,
            apiUrl: ""
        }
    },
    created() {

        window.scrollTo(0, 0);
        this.$store.commit('updateNavbarIndex', 0);

        axios.post(this.URL_BACKEND+'user/fav/movies/list/',{
            "emailuser": this.user.userEmail
        })
        .then(response => {
            (response.data.movies).forEach(movie => {

            axios.get('https://api.themoviedb.org/3/movie/'+ movie.movie +'?api_key=' + this.API_KEY_THEMOVIEDB +'&language=es-ES')
                .then(response => {
                    this.favoritesMovies.push({
                    "id": movie.movie,
                    "nombre": response.data.title})
                })
                .catch(function (error) {
                    console.log(error);
                })

            })
        })
        .catch(error => {
            console.error(error)
        })

        axios.post(this.URL_BACKEND+'user/fav/series/list/',{
            "emailuser": this.user.userEmail
        })
        .then(response => {
            (response.data.series).forEach(serie => {

            axios.get('https://api.themoviedb.org/3/tv/'+ serie.serie +'?api_key=' + this.API_KEY_THEMOVIEDB +'&language=es-ES')
                .then(response => {
                    this.favoirtesSeries.push({
                    "id": serie.serie,
                    "nombre": response.data.name})
                })
                .catch(function (error) {
                    console.log(error);
                })

            })
        })
        .catch(error => {
            console.error(error)
        })
    },
    methods: {
        updatePassword(event) {
            event.preventDefault()
            
            if (this.User.oldpassword == "" || this.User.password == "" || this.User.confirmPassword == ""){
                alert("Ingresa datos validos");
            }
            else{
                if (this.User.password != this.User.confirmPassword){
                    alert("Las contraseñas no coinciden");
                }
                else {
                    axios.put(this.URL_BACKEND+'user/update/password/',{
                        "email": this.user.userEmail,
                        "password": this.User.oldpassword,
                        "newpassword": this.User.confirmPassword})
                    .then(response => {
                        if(response.data.passwordUpdate == true){
                            this.currentView = 0;
                            this.User = {
                                oldpassword: "", 
                                password: "",
                                confirmPassword: "",
                            };
                            alert('Contraseña actualizada');
                        }
                        else {
                            alert('Contraseña erronea');
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    })
                }
            }
        },
        changeView(number) {
            this.currentView = number;
        },
        seeDetails(url){
            this.$router.push(url);
        }
    },
    computed: {
        ...mapState(['user'])
    }
  
}
</script>

<style>
.profile{
    margin-top: 20px;
}

.card-profile{
  background: #343a40;
  padding-top: 30px;
  padding-bottom: 30px;
  border: opx;
  border-radius: 10px;
  color: white;
  width: 100%;
  margin-bottom: 20px;
}

.options-profile{
  margin-top: 10px;
}

.options-profile span{
  display: block;
  margin-top: 0px;
  margin-bottom: 0px;
  padding-top: 15px;
  padding-bottom: 15px;
  cursor: pointer;
}

.options-profile span:hover{
  background: white;
  color: #343a40;
}

.card-profile-media{
  background: #343a40;
  padding-top: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  color: white;
}

.updateprofile{
  width: 50%;
  margin: 0 auto;
  margin-top: 30px;
}

.updateprofile input{
  margin-top: 15px;
}

.updateprofile button{
  margin-top: 15px;
  margin-bottom: 20px;
}
</style>