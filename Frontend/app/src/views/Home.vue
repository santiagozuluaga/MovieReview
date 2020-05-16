<template>
    <div class="home">
        <div v-if="Movies[0] != null && Series[0] != null" id="carousel" class="carousel-bootstrap carousel slide" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img :src="backgroundUrl+Movies[0].backdrop_path" class="d-block w-100" />
                </div>
                <div class="carousel-item">
                    <img :src="backgroundUrl+Series[0].backdrop_path" class="d-block w-100" />
                </div>
                <div class="carousel-item">
                    <img :src="backgroundUrl+Movies[1].backdrop_path" class="d-block w-100" />
                </div>
                <div class="carousel-item">
                    <img :src="backgroundUrl+Series[1].backdrop_path" class="d-block w-100" />
                </div>
                <div class="carousel-item">
                    <img :src="backgroundUrl+Movies[2].backdrop_path" class="d-block w-100" />
                </div>
                <div class="carousel-item">
                    <img :src="backgroundUrl+Series[2].backdrop_path" class="d-block w-100" />
                </div>
                <div class="panel-carousel">
                </div>
            </div>
            <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>

        <!--PELICULAS-->
        <div class="container-home">

            <div class="container-title">
            <h3 class="title-recent">Peliculas recomendadas</h3>
            </div>

            
            <div class="container-recent">
            
            <button v-on:click="changePageMovie('left')" class="left">
                <svg class="bi bi-chevron-left" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 010 .708L5.707 8l5.647 5.646a.5.5 0 01-.708.708l-6-6a.5.5 0 010-.708l6-6a.5.5 0 01.708 0z" clip-rule="evenodd"/>
                </svg>
            </button>
            <button v-on:click="changePageMovie('right')" class="right">
                <svg class="bi bi-chevron-right" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 01.708 0l6 6a.5.5 0 010 .708l-6 6a.5.5 0 01-.708-.708L10.293 8 4.646 2.354a.5.5 0 010-.708z" clip-rule="evenodd"/>
                </svg>
            </button>

            <div v-if="currentPageMovie == 1 && !viewinsmall" class="recents">
                <div v-bind:key="n" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n-1].id)">
                <img v-bind:src="posterUrl+Movies[n-1].poster_path" alt="" />
                </div>
            </div>

            <div v-if="currentPageMovie == 2 && !viewinsmall" class="recents">
                <div v-bind:key="n+5" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+4].id)">
                <img v-bind:src="posterUrl+Movies[n+4].poster_path" alt="" />
                </div>
            </div>

            <div v-if="currentPageMovie == 3 && !viewinsmall" class="recents">
                <div v-bind:key="n+9" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+9].id)">
                <img v-bind:src="posterUrl+Movies[n+9].poster_path" alt="" />
                </div>
            </div>

            <div v-if="currentPageMovie == 4 && !viewinsmall" class="recents">
                <div v-bind:key="n+14" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+14].id)">
                <img v-bind:src="posterUrl+Movies[n+14].poster_path" alt="" />            
                </div>
            </div>

            <div v-if="viewinsmall" class="recents">
                <div v-bind:key="movie.id" v-for="movie in Movies" v-on:click="seeMovieSerie('/movie/'+movie.id)">
                <img v-bind:src="posterUrl+movie.poster_path" alt="" />            
                </div>
            </div>
            </div>
        </div>

        <!--SERIES-->
        <div class="container-home">

            <div class="container-title">
            <h3 class="title-recent">Series recomendadas</h3>
            </div>

            <div>
            <div class="container-recent">
                
                <button v-on:click="changePageSerie('left')" class="left">
                    <svg class="bi bi-chevron-left" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 010 .708L5.707 8l5.647 5.646a.5.5 0 01-.708.708l-6-6a.5.5 0 010-.708l6-6a.5.5 0 01.708 0z" clip-rule="evenodd"/>
                    </svg>
                </button>
                <button v-on:click="changePageSerie('right')" class="right">
                    <svg class="bi bi-chevron-right" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 01.708 0l6 6a.5.5 0 010 .708l-6 6a.5.5 0 01-.708-.708L10.293 8 4.646 2.354a.5.5 0 010-.708z" clip-rule="evenodd"/>
                    </svg>
                </button>

                <div v-if="currentPageSerie == 1 && !viewinsmall" class="recents">
                <div v-bind:key="n" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n-1].id)">
                    <img v-bind:src="posterUrl+Series[n-1].poster_path" alt="" />
                </div>
                </div>

                <div v-if="currentPageSerie == 2 && !viewinsmall" class="recents">
                <div v-bind:key="n+5" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+4].id)">
                    <img v-bind:src="posterUrl+Series[n+4].poster_path" alt="" />
                </div>
                </div>

                <div v-if="currentPageSerie == 3 && !viewinsmall" class="recents">
                <div v-bind:key="n+9" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+9].id)">
                    <img v-bind:src="posterUrl+Series[n+9].poster_path" alt="" />
                </div>
                </div>

                <div v-if="currentPageSerie == 4 && !viewinsmall" class="recents">
                <div v-bind:key="n+14" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+14].id)">
                    <img v-bind:src="posterUrl+Series[n+14].poster_path" alt="" />            
                </div>
                </div>

                <div v-if="viewinsmall" class="recents">
                <div v-bind:key="serie.id" v-for="serie in Series" v-on:click="seeMovieSerie('/serie/'+serie.id)">
                <img v-bind:src="posterUrl+serie.poster_path" alt="" />            
                </div>
            </div>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import config from '@/config/configproject.js'

export default {
    data() {
        return{
            Movies: [],
            Series: [],
            posterUrl: "https://image.tmdb.org/t/p/w300",
            backgroundUrl: 'https://image.tmdb.org/t/p/original/',
            API_KEY_THEMOVIEDB: config.API_KEY_THEMOVIEDB,
            currentPageMovie: 1,
            currentPageSerie: 1,
            viewinsmall: false,
        }
    },
    created() {
        window.scrollTo(0, 0);
        if(screen.width <= 800){
            this.$store.commit('updateNavbarIndex', 0);
            this.viewinsmall = true
        }
        else {
            window.addEventListener('scroll', this.scrollHandler)
            this.$store.commit('updateNavbarIndex', 1);
        }

        axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-CO')
        .then(response => {
            this.Movies = response.data.results
        })
        .catch(error => {
            console.log(error);
        })

        axios.get('https://api.themoviedb.org/3/tv/on_the_air?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-CO')
        .then(response => {
            this.Series = response.data.results
        })
        .catch(error => {
            console.log(error);
        })

    },
    beforeDestroy() {
        if(screen.width > 800){
            window.removeEventListener('scroll', this.scrollHandler)
        }
    },
    methods: {
        seeMovieSerie(url) {
            this.$router.push(url);
        },
        changePageMovie(button) {
            if(button == "left"){
                if(this.currentPageMovie != 1){
                this.currentPageMovie = this.currentPageMovie - 1;
                }
                else{
                this.currentPageMovie = 4;
                }
            }
            else {
                if(this.currentPageMovie != 4){
                this.currentPageMovie = this.currentPageMovie + 1;
                }
                else{
                this.currentPageMovie = 1;
                }
            }
        },
        changePageSerie(button) {
            if(button == "left"){
                if(this.currentPageSerie != 1){
                this.currentPageSerie = this.currentPageSerie - 1;
                }
                else{
                this.currentPageSerie = 4;
                }
            }
            else {
                if(this.currentPageSerie != 4){
                this.currentPageSerie = this.currentPageSerie + 1;
                }
                else{
                this.currentPageSerie = 1;
                }
            }
        },
        scrollHandler() {
            if(window.scrollY == 0){
                this.$store.commit('updateNavbarIndex', 1);
            }
            else {
                this.$store.commit('updateNavbarIndex', 2);
            }
        }
    }
}
</script>

<style>
.panel-carousel{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0, .6);
}

.carousel-bootstrap{
    height: 100vh;
    overflow: hidden;
}

.title-recent{
    margin-top: 20px;
    margin-bottom: 10px;
}

.container-recent{
    position: relative;
    display: flex;
	align-items: center;
    justify-content: center;
}

.recents{
    text-align: center;
}

.recents div{
    display: inline-block;
    margin: 10px 10px;
}

.recents div:hover{
    cursor: pointer;
    transform: scale(1.1);
    transform-origin: center;
}

.recents div img{
    border-radius: 5px;
    width: 190px;
    height: 285px;
}

.left, .right {
    position: absolute;
    height: 50%;
    background: rgba(0,0,0,0.3);
    border: none;
    color: black;
}

.left:hover, .right:hover{
    background: rgba(0,0,0, .9);
    color: white;
}

.left{
    left: 0;
}

.right{
    right: 0;
}

.container-home{
    width: 85%;
    margin: 0 auto;
}
</style>