<template>
    <b-container class="container-news">
        <b-row class="justify-content-center">
            <b-col cols="12">
                <b-carousel
                    class="container-carousel"
                    :interval="3000"
                    indicators
                    controls>
                    <b-carousel-slide v-bind:img-src="baseUrl+Movies[0].backdrop_path">
                        <div>
                            <h3>{{Movies[0].title}}</h3>
                            <b-button variant="danger" v-on:click="seeMovie(Movies[0].id)">MAS INFORMACION</b-button>
                        </div>
                    </b-carousel-slide>
                    <b-carousel-slide v-bind:img-src="baseUrl+Movies[1].backdrop_path">
                        <div>
                            <h3>{{Movies[1].title}}</h3>
                            <b-button variant="danger" v-on:click="seeMovie(Movies[1].id)">MAS INFORMACION</b-button>
                        </div>
                    </b-carousel-slide>
                    <b-carousel-slide v-bind:img-src="baseUrl+Movies[2].backdrop_path">
                        <div>
                            <h3>{{Movies[2].title}}</h3>
                            <b-button variant="danger" v-on:click="seeMovie(Movies[2].id)">MAS INFORMACION</b-button>
                        </div>
                    </b-carousel-slide>
                    <b-carousel-slide v-bind:img-src="baseUrl+Movies[3].backdrop_path">
                        <div>
                            <h3>{{Movies[3].title}}</h3>
                            <b-button variant="danger" v-on:click="seeMovie(Movies[3].id)">MAS INFORMACION</b-button>
                        </div>
                    </b-carousel-slide>
                    <b-carousel-slide v-bind:img-src="baseUrl+Movies[4].backdrop_path">
                        <div>
                            <h3>{{Movies[4].title}}</h3>
                            <b-button variant="danger" v-on:click="seeMovie(Movies[4].id)">MAS INFORMACION</b-button>
                        </div>
                    </b-carousel-slide>
                    <div class="background-image">
                    </div>
                </b-carousel>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return{
            Movies: [],
            baseUrl: "https://image.tmdb.org/t/p/w1280/",
        }
    },
    created() {

        let vue = this;
        axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=1')
        .then(function(response) {
            vue.Movies = response.data.results;
        })
        .catch(function (error) {
            console.log(error);
        })
    },
    methods: {
        seeMovie(id){
            this.$router.push('/movie/'+id);
        }
    }
}
</script>

<style>
.image-carousel:hover{
    cursor: pointer;
}

.background-image{
    position: absolute;
    width: 100%;
    height: 100%;
    background: black;
    opacity: 0.5;
}
</style>