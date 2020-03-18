<template>
    <div>
        <b-container class="container-news">
            <h3>Recomendaciones de la semana</h3>
            <b-carousel
                class="container-carousel"
                :interval="3000"
                controls
                style="text-shadow: 1px 1px 2px #333;">
                <b-carousel-slide v-bind:caption="Movies[0].title">
                    <template v-slot:img>
                        <img class="image-carousel" v-on:click="seeMovie(Movies[0].id)" width="100%" v-bind:src="baseUrl+Movies[0].backdrop_path">
                    </template>
                </b-carousel-slide>
                <b-carousel-slide v-bind:caption="Movies[1].title">
                    <template v-slot:img>
                        <img class="image-carousel" v-on:click="seeMovie(Movies[1].id)" width="100%" v-bind:src="baseUrl+Movies[1].backdrop_path">
                    </template>
                </b-carousel-slide>
                <b-carousel-slide v-bind:caption="Movies[2].title">
                    <template v-slot:img>
                        <img class="image-carousel" v-on:click="seeMovie(Movies[2].id)" width="100%" v-bind:src="baseUrl+Movies[2].backdrop_path">
                    </template>
                </b-carousel-slide>
                <b-carousel-slide v-bind:caption="Movies[3].title">
                    <template v-slot:img>
                        <img class="image-carousel" v-on:click="seeMovie(Movies[3].id)" width="100%" v-bind:src="baseUrl+Movies[3].backdrop_path">
                    </template>
                </b-carousel-slide>
                <b-carousel-slide v-bind:caption="Movies[4].title">
                    <template v-slot:img>
                        <img class="image-carousel" v-on:click="seeMovie(Movies[4].id)" width="100%" v-bind:src="baseUrl+Movies[4].backdrop_path">
                    </template>
                </b-carousel-slide>
            </b-carousel>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return{
            Movies: [],
            baseUrl: "https://image.tmdb.org/t/p/original/",
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
</style>