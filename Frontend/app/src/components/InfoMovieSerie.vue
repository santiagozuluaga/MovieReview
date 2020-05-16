<template>
    <div class="information-movieserie bg-danger text-white">
        <div class="container container-info">
            <div class="row justify-content-center">
                <div class="col col-12 col-lg-3 text-center margin-movieserie">
                    <div class="container-poster">
                        <img class="image-poster" :src="posterUrl+MovieSerie.poster_path" alt="">
                    </div>
                    <div v-if="user.isLogged == true" class="container-stars-islogged">
                        <div v-if="scoreUser == false">
                            <div v-bind:key="n" v-for="n in 5">
                                <svg 
                                    v-if="stars[n-1] == 'star-fill'"
                                    @mouseover="changeIcon(n, 'star-fill')"
                                    @mouseleave="changeIcon(n, 'star')"
                                    @click="clickStar(n)" class="bi bi-star-fill" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.283.95l-3.523 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                </svg>
                                <svg 
                                    v-if="stars[n-1] == 'star'"
                                    @mouseover="changeIcon(n, 'star-fill')"
                                    @mouseleave="changeIcon(n, 'star')"
                                    @click="clickStar(n)" class="bi bi-star" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.523-3.356c.329-.314.158-.888-.283-.95l-4.898-.696L8.465.792a.513.513 0 00-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767l-3.686 1.894.694-3.957a.565.565 0 00-.163-.505L1.71 6.745l4.052-.576a.525.525 0 00.393-.288l1.847-3.658 1.846 3.658a.525.525 0 00.393.288l4.052.575-2.906 2.77a.564.564 0 00-.163.506l.694 3.957-3.686-1.894a.503.503 0 00-.461 0z" clip-rule="evenodd"/>
                                </svg>
                            </div>
                        </div>
                        <div v-if="scoreUser == true">
                            <span><strong>Gracias por puntuar!</strong></span>
                        </div>                     
                    </div>
                    <div v-if="user.isLogged == false" class="container-stars-isntlogged">
                        <span><strong>¡Inicia sesión para puntuar las películas!</strong></span>
                    </div>
                    <div class="container-score bg-dark">
                        <h3 class="text-center">{{totalScore}}</h3>
                        <div class="score">
                            <div v-bind:key="n" v-for="n in 5">
                                <svg v-if="starsScore[n-1] == 'star-fill'" class="bi bi-star-fill" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.283.95l-3.523 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                </svg>
                                <svg v-if="starsScore[n-1] == 'star'" class="bi bi-star" width="1.5em" height="1.5em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.523-3.356c.329-.314.158-.888-.283-.95l-4.898-.696L8.465.792a.513.513 0 00-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767l-3.686 1.894.694-3.957a.565.565 0 00-.163-.505L1.71 6.745l4.052-.576a.525.525 0 00.393-.288l1.847-3.658 1.846 3.658a.525.525 0 00.393.288l4.052.575-2.906 2.77a.564.564 0 00-.163.506l.694 3.957-3.686-1.894a.503.503 0 00-.461 0z" clip-rule="evenodd"/>
                                </svg>
                            </div>                        
                        </div>
                    </div>
                </div>
                <div class="col col-12 col-lg-9 margin-movieserie">
                    <div>
                        <h3 v-if="type == 'movie'"><strong>{{MovieSerie.title}}</strong></h3>
                        <h3 v-if="type == 'serie'"><strong>{{MovieSerie.name}}</strong></h3>
                    </div>
                    <div>
                        <button v-on:click="addFavorite()" v-if="favoriteUser == false" class="btn btn-dark">
                            Agregar a favoritos
                            <svg class="bi bi-heart-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" clip-rule="evenodd"/>
                            </svg>
                        </button>
                        <button v-on:click="deleteFavorite()" v-if="favoriteUser == true" class="btn btn-dark">
                            Eliminar de favoritos
                            <svg class="bi bi-heart-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" clip-rule="evenodd"/>
                            </svg>
                        </button>
                    </div>
                    <div>
                        <h4><strong>Sinopsis:</strong></h4>
                        <p>{{MovieSerie.overview}}</p>
                    </div>
                    <div v-if="type == 'serie'">
                        <p><strong>Fecha de estreno: </strong> {{MovieSerie.first_air_date}}</p>
                        <p><strong>Numero de temporadas: </strong>{{MovieSerie.number_of_seasons}}</p>
                        <p><strong>Numero de episodios: </strong> {{MovieSerie.number_of_episodes}}</p>
                        <h4><strong>Generos:</strong></h4>
                    </div>
                    <div v-if="type == 'movie'">
                        <p><strong>Fecha de estreno: </strong> {{MovieSerie.release_date}}</p>
                        <p><strong>Título original: </strong> {{MovieSerie.original_title}}</p>
                        <p><strong>Duración: </strong>{{MovieSerie.runtime}} minutos</p>
                        <h4><strong>Generos:</strong></h4>
                    </div>
                    <div>
                        <button v-on:click="seeCategories(genre.id)" class="btn btn-dark button-genre" v-bind:key="genre.id" v-for="genre in MovieSerie.genres">{{genre.name}}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import config from '@/config/configproject.js'

export default {
    props: ['id', 'type'],
    data () {
        return {
            view: this.$props.type,
            MovieSerie: {},
            posterUrl: "https://image.tmdb.org/t/p/w300",
            stars: ["star", "star", "star", "star", "star"],
            starsScore: ["star", "star", "star", "star", "star"],
            score: [],
            totalScore: 0,
            clickStars: false,
            API_KEY_THEMOVIEDB: config.API_KEY_THEMOVIEDB,
            URL_BACKEND: config.URL_BACKEND,
            apiUrl: "",
            scoreUser: false,
            favoriteUser: false,

        }
    },
    created() {

        let temp = 0;
        let total = 0;

        if( this.view == "serie") {
            this.apiUrl = 'https://api.themoviedb.org/3/tv/'+ this.$props.id +'?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES';
            
            axios.get(this.URL_BACKEND + 'user/score/serie/'+this.$props.id+'/')
            .then(response => {
                if(response.data.serie.length > 0){
                    (response.data.serie).forEach(element => {
                        total = total + element.scoreserie
                        temp = temp + 1;
                        if(this.user.isLogged == true){
                            if(this.user.userEmail == element.user){
                                this.score.push({score: element.scoreserie})
                                this.scoreUser = true;
                            }
                            else { 
                                this.score.push({score: element.scoreserie})
                            }
                        }
                        else { 
                            this.score.push({score: element.scoreserie})
                        }
                        
                    })
                    total = total / temp;
                    this.totalScore = total;
                    this.changeScoreIcon(total);
                }
            })
            .catch(function (error) {
                console.log(error);
            })

            if(this.user.isLogged == true){
                axios.post(this.URL_BACKEND + 'user/fav/checkserie/',{
                    "emailuser": this.user.userEmail,
                    "idserie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = response.data.savefavorite
                })
                .catch(error => {
                    console.error(error)
                })
            }
            
        }
        else {
            this.apiUrl = 'https://api.themoviedb.org/3/movie/'+ this.$props.id +'?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES';
            
            axios.get(this.URL_BACKEND + 'user/score/movie/'+this.$props.id+'/')
            .then(response => {
                if(response.data.movie.length > 0){
                    (response.data.movie).forEach(element => {
                        total = total + element.scoremovie
                        temp = temp + 1;
                        if(this.user.isLogged == true) {
                            if(this.user.userEmail == element.user){
                                this.score.push({score: element.scoremovie})
                                this.scoreUser = true;
                            }
                            else{ 
                                this.score.push({score: element.scoremovie})
                            }
                        }
                        else { 
                            this.score.push({score: element.scoremovie})
                        }
                    })
                    total = total / temp;
                    this.totalScore = total;
                    this.changeScoreIcon(total);
                }
            })
            .catch(function (error) {
                console.log(error);
            })

            if(this.user.isLogged == true) {
                axios.post(this.URL_BACKEND + 'user/fav/checkmovie/',{
                    "emailuser": this.user.userEmail,
                    "idmovie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = response.data.savefavorite
                })
                .catch(error => {
                    console.error(error)
                })
            }
            
        }

        axios.get(this.apiUrl)
        .then(response => {
            this.MovieSerie = response.data
        })
        .catch(error => {
            console.log(error);
        })
    },
    methods: {
        changeIcon(index, icon){

            if(this.clickStars == false){
                for(let i=0; i<index; i++){
                    this.$set(this.stars, i, icon);
                }
            }            
        },
        clickStar(index){

            if(this.clickStars == false) {
                this.clickStars = true;
                this.changeIcon(index, "star-fill");
                this.scoreSubmit(this.$props.id, index);
            }
        },
        seeCategories(id){
            if(this.$props.type == 'serie'){
                this.$router.push('/search/series/'+ id);
            }
            else {
                this.$router.push('/search/movies/'+ id);
            }
        },
        scoreSubmit(id, score){
            this.scoreUser = true;

            if(this.view == 'serie') {

                axios.post(this.URL_BACKEND + 'user/score/serie/', {
                        "idserie": id,
                        "emailuser": this.user.userEmail,
                        "score": score 
                    })
                .then(response => {
                    
                    if(response.data.scoreserie == true){
                        if(this.totalScore == 0) {
                            this.totalScore = score;
                        }
                        else{
                            this.totalScore = (this.totalScore + score)/2;
                        }
                        
                        this.changeScoreIcon(this.totalScore);
                    }
                })
                .catch(error => {
                    console.log(error);
                })
            }
            else {

                axios.post(this.URL_BACKEND + 'user/score/movie/', {
                    "idmovie": id,
                    "emailuser": this.user.userEmail,
                    "score": score 
                })
                .then(response => {

                    if(response.data.scoremovie == true){
                        if(this.totalScore == 0) {
                            this.totalScore = score;
                        }
                        else{
                            this.totalScore = (this.totalScore + score)/2;
                        }
                        
                        this.changeScoreIcon(this.totalScore);
                    }
                })
                .catch(error => {
                    console.log(error);
                })
            }            
        },
        changeScoreIcon(total){

            if(total > 0 && total < 2){
                this.$set(this.starsScore, 0, "star-fill");
            }
            else if(total == 2 && total < 3){
                this.$set(this.starsScore, 0, "star-fill");
                this.$set(this.starsScore, 1, "star-fill");
            }
            else if(total == 3 && total < 4){
                this.$set(this.starsScore, 0, "star-fill");
                this.$set(this.starsScore, 1, "star-fill");
                this.$set(this.starsScore, 2, "star-fill");
            }
            else if(total == 4 && total < 5){
                this.$set(this.starsScore, 0, "star-fill");
                this.$set(this.starsScore, 1, "star-fill");
                this.$set(this.starsScore, 2, "star-fill");
                this.$set(this.starsScore, 3, "star-fill");
            }
            else if(total == 5){
                this.$set(this.starsScore, 0, "star-fill");
                this.$set(this.starsScore, 1, "star-fill");
                this.$set(this.starsScore, 2, "star-fill");
                this.$set(this.starsScore, 3, "star-fill");
                this.$set(this.starsScore, 4, "star-fill");
            }
        },
        addFavorite() {
            if(this.view == 'serie') {

                axios.post(this.URL_BACKEND + 'user/fav/series/',{
                    "emailuser": this.user.userEmail,
                    "idserie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = true
                })
                .catch(error => {
                    console.error(error)
                })
            }
            else{

                axios.post(this.URL_BACKEND + 'user/fav/movies/',{
                    "emailuser": this.user.userEmail,
                    "idmovie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = true
                })
                .catch(error => {
                    console.error(error)
                })
            }
            
        },
        deleteFavorite() {
            if(this.view == 'serie') {

                axios.post(this.URL_BACKEND + 'user/fav/series/delete/',{
                    "emailuser": this.user.userEmail,
                    "idserie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = false
                })
                .catch(error => {
                    console.error(error)
                })
            }
            else{

                axios.post(this.URL_BACKEND + 'user/fav/movies/delete/',{
                    "emailuser": this.user.userEmail,
                    "idmovie": this.$props.id
                })
                .then(response => {
                    this.favoriteUser = false
                })
                .catch(error => {
                    console.error(error)
                })
            }
        }
    },
    computed: {
        ...mapState(['user'])
    }

}
</script>

<style>
.container-info{
  padding-top: 20px;
  padding-bottom: 40px;
}

.information-movieserie{
    margin-bottom: 20px;
}

.image-poster{
    border-radius: 5px;
    width: 250px; 
    height: 375px;
}

.button-genre{
    margin-top: 10px;
    margin-right: 10px;
}

.container-stars-islogged div{
    display: inline-block;
    margin-top: 15px;
    margin-left: 10px;
    margin-right: 10px;
}

.container-stars-isntlogged{
    margin-top: 15px;
    margin-bottom: 0px;
}

.container-score{
    margin-top: 15px;
    padding-top: 5px;
    padding-bottom: 15px;
    border-radius: 5px;
}

.container-score div div{
    display: inline-block;
    margin-top: 0px;
    margin-left: 10px;
    margin-right: 10px;
}

.margin-movieserie{
    margin-top: 20px;
}
</style>