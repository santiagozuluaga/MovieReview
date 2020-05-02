<template>
  <div class="searchmovie">
      <b-container>
            <h3>Descubrir</h3>
            <b-row>
            <b-col class="input-filter" lg="3">
                <b-form-select v-model="selectedgenre" :options="optionsGenres"></b-form-select>
            </b-col>
            <b-col class="input-filter" lg="3">
                <b-form-select v-model="selectedYear" :options="optionsYear"></b-form-select>
            </b-col>
            <b-col class="input-filter" lg="2">
                <b-button block v-on:click="applyFilter()" variant="danger">Filtrar</b-button>
            </b-col>
            <b-col class="input-filter" lg="6">
                <b-form-input v-model="keyword" placeholder="Ingresa una palabra clave"></b-form-input>
            </b-col>
            <b-col class="input-filter" lg="2">
                <b-button block v-on:click="searchMovies()" variant="danger">Buscar</b-button>
            </b-col>
            <b-col cols="12">   
                <h3>Peliculas</h3>
            </b-col>
            <b-col class="container-movie text-center" v-bind:key="movie.id" v-for="movie in Movies">
                <div v-on:click="seeMovie(movie.id)">
                    <img v-bind:src="baseUrl+movie.poster_path" alt=""/>
                </div>
            </b-col>
            <!--
            <b-col cols="12 text-center">
                <b-button-group class="pagination-buttons">
                    <b-button variant="outline-danger" v-on:click="changePage(1)">
                        <b-icon icon="chevron-left">
                        </b-icon>
                    </b-button>

                    <button v-if="currentPage == pagesCurrent[0]" class="btn btn-danger" v-bind:id="pagesCurrent[0]">
                        {{pagesCurrent[0]}}
                    </button>
                    <button v-if="currentPage != pagesCurrent[0]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[0]">
                        {{pagesCurrent[0]}}
                    </button>

                    <button v-if="currentPage == pagesCurrent[1]" class="btn btn-danger" v-bind:id="pagesCurrent[1]">
                        {{pagesCurrent[1]}}
                    </button>
                    <button v-if="currentPage != pagesCurrent[1]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[1]">
                        {{pagesCurrent[1]}}
                    </button>

                    <button v-if="currentPage == pagesCurrent[2]" class="btn btn-danger" v-bind:id="pagesCurrent[2]">
                        {{pagesCurrent[2]}}
                    </button>
                    <button v-if="currentPage != pagesCurrent[2]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[2]">
                        {{pagesCurrent[2]}}
                    </button>
                    
                    <button v-if="currentPage == pagesCurrent[3]" class="btn btn-danger" v-bind:id="pagesCurrent[3]">
                        {{pagesCurrent[3]}}
                    </button>
                    <button v-if="currentPage != pagesCurrent[3]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[3]">
                        {{pagesCurrent[3]}}
                    </button>
                    
                    <button v-if="currentPage == pagesCurrent[4]" class="btn btn-danger" v-bind:id="pagesCurrent[4]">
                        {{pagesCurrent[4]}}
                    </button>
                    <button v-if="currentPage != pagesCurrent[4]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[4]">
                        {{pagesCurrent[4]}}
                    </button>

                    <b-button variant="outline-danger" v-on:click="changePage(totalPages)">
                        <b-icon icon="chevron-right">
                        </b-icon>
                    </b-button>
                </b-button-group>
            </b-col>
            -->
          </b-row>
      </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['genre'],
    data() {
        return{
            Movies: [],
            baseUrl: "https://image.tmdb.org/t/p/w300/",
            Genres: [],
            selectedgenre: null,
            optionsGenres: [
                {value: null, text: "Categoria"}
            ],
            selectedYear: null,
            optionsYear: [
                {value: null, text: "Año"}
            ],
            totalPages: 1,
            keyword: null,
            pagesCurrent: [1, 2, 3, 4, 5],
            currentPage: 1
        }
    },
    created() {

        this.$store.commit('updateWindow', 'dark')

        for(var i=new Date().getFullYear(); i>=1900; i--){
            this.optionsYear.push({value: i, text: i});
        }

        let vue = this;
        var apiUrlMovie;    

        if(this.$props.genre != null){

            this.selectedgenre = this.$props.genre;

            apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&with_genres=' + this.$props.genre;
        }
        else{
            apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO';
        }

        axios.get(apiUrlMovie)
        .then(response => {
            (response.data.results).forEach(movie => {
                if(movie.poster_path != null){
                    vue.Movies.push(movie)
                }                    
            })
            vue.totalPages = response.data.total_pages
        })  
        .catch(function (error) {
            console.log(error);
        })

        axios.get('https://api.themoviedb.org/3/genre/movie/list?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
        .then(function(response) {
            (response.data.genres).forEach(genre => {
            vue.optionsGenres.push({value: genre.id, text: genre.name});
            })
        })
        .catch(function (error) {
            console.log(error);
        })
        
    },
    methods: {
        seeMovie(id){
            this.$router.push('/movie/'+id);
        },
        searchMovies() {
            let vue = this;
            vue.Movies = []
            
            axios.get('https://api.themoviedb.org/3/search/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&query=' + vue.keyword)
            .then(function(response) {
                (response.data.results).forEach(movie => {
                    if(movie.poster_path != null){
                        vue.Movies.push(movie)
                    }                    
                })
                vue.totalPages = response.data.total_pages
            })  
            .catch(function (error) {
                console.log(error);
            })
        },
        applyFilter() {

            let vue = this;
            vue.Movies = []
            var apiUrlMovie;

            if(vue.selectedYear != null && vue.selectedgenre != null){
                apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&primary_release_year=' + this.selectedYear + '&with_genres=' + this.selectedgenre
            }
            else if(vue.selectedYear == null && vue.selectedgenre != null){
                apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&with_genres=' + this.selectedgenre
            }
            else if(vue.selectedYear != null && vue.selectedgenre == null){
                apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&primary_release_year=' + this.selectedYear
            }
            else{
                apiUrlMovie = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO'
            }

            axios.get(apiUrlMovie)
            .then(function(response) {
                (response.data.results).forEach(movie => {
                    if(movie.poster_path != null){
                        vue.Movies.push(movie)
                    }                    
                })
                vue.totalPages = response.data.total_pages
            })  
            .catch(function (error) {
                console.log(error);
            })
        },
        changePage(number) {

            this.pagesCurrent = []

            if(number == this.totalPages){
                for(var i=4; i>=0; i--){
                    this.pagesCurrent.push(number - i);
                }

                this.currentPage = 500
                
            }
            else if(number == 1){
                for(var i=1; i<6; i++){
                    this.pagesCurrent.push(i);
                }

                this.currentPage = 1
            }
        }
    }
}
</script>

<style>
.searchmovie{
    margin-top: 15vh;
}

.container-movie{
    margin: 10px 0;
}

.container-movie div img:hover{
    cursor: pointer;
    transform: scale(1.1);
    transform-origin: center;
}

.container-movie div img{
    border-radius: 5px;
    width: 190px;
    height: 285px;

}

.pagination-buttons{
    margin-top: 30px;
    margin-bottom: 30px;
}

.input-filter{
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>