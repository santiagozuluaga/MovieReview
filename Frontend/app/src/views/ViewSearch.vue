<template>
    <div class="searchview">
        <div class="container">
            <div class="row">
                <div class="input-filter col col-lg-12">
                    <h3>Descubrir</h3>
                </div>
                <div class="input-filter col col-12 col-lg-3">
                    <select class="custom-select" v-model="selectedgenre">
                        <option selected disabled :value="null">Seleccione un género</option>
                        <option v-bind:key="option.value" v-for="option in optionsGenres" :value="option.value">
                            {{option.text}}
                        </option>
                    </select>
                </div>
                <div class="input-filter col col-12 col-lg-3">
                    <select class="custom-select" v-model="selectedYear">
                        <option selected disabled :value="null">Seleccione un año</option>
                        <option v-bind:key="option.value" v-for="option in optionsYear" :value="option.value">
                            {{option.text}}
                        </option>
                    </select>
                </div>
                <div class="input-filter col col-12 col-lg-2">
                    <button v-on:click="applyFilter()" class="btn btn-danger btn-block">Filtrar</button>
                </div>
                <div class="input-filter col col-12">
                    <h3 v-if="currentView == 'searchmovies'">Peliculas</h3>
                    <h3 v-if="currentView == 'searchseries'">Series</h3>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="container-movie-serie text-center" v-bind:key="element.id" v-for="element in MoviesSeries">
                    <div v-if="currentView == 'searchmovies'" v-on:click="seeMovieSerie('/movie/' + element.id)">
                        <img v-bind:src="posterUrl+element.poster_path" alt=""/>
                    </div>
                    <div v-if="currentView == 'searchseries'" v-on:click="seeMovieSerie('/serie/' + element.id)">
                        <img v-bind:src="posterUrl+element.poster_path" alt=""/>
                    </div>
                </div>
            </div>  
            <div class="row">
                <div class="col col-12 text-center">
                    <div class="btn-group pagination-buttons" role="group">
                        
                        <button class="btn btn-outline-danger" v-on:click="changePage(1)">
                            <svg class="bi bi-chevron-left" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 010 .708L5.707 8l5.647 5.646a.5.5 0 01-.708.708l-6-6a.5.5 0 010-.708l6-6a.5.5 0 01.708 0z" clip-rule="evenodd"/>
                            </svg>
                        </button>

                        <button v-on:click="changePage('first')" v-if="currentPage == pagesCurrent[0]" class="btn btn-danger" v-bind:id="pagesCurrent[0]">
                            {{pagesCurrent[0]}}
                        </button>
                        <button v-on:click="changePage('first')" v-if="currentPage != pagesCurrent[0]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[0]">
                            {{pagesCurrent[0]}}
                        </button>

                        <button v-on:click="changePage('second')" v-if="currentPage == pagesCurrent[1]" class="btn btn-danger" v-bind:id="pagesCurrent[1]">
                            {{pagesCurrent[1]}}
                        </button>
                        <button v-on:click="changePage('second')" v-if="currentPage != pagesCurrent[1]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[1]">
                            {{pagesCurrent[1]}}
                        </button>

                        <button v-on:click="changePage('third')" v-if="currentPage == pagesCurrent[2]" class="btn btn-danger" v-bind:id="pagesCurrent[2]">
                            {{pagesCurrent[2]}}
                        </button>
                        <button v-on:click="changePage('third')" v-if="currentPage != pagesCurrent[2]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[2]">
                            {{pagesCurrent[2]}}
                        </button>
                        
                        <button v-on:click="changePage('fourth')" v-if="currentPage == pagesCurrent[3]" class="btn btn-danger" v-bind:id="pagesCurrent[3]">
                            {{pagesCurrent[3]}}
                        </button>
                        <button v-on:click="changePage('fourth')" v-if="currentPage != pagesCurrent[3]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[3]">
                            {{pagesCurrent[3]}}
                        </button>
                        
                        <button v-on:click="changePage('fifth')" v-if="currentPage == pagesCurrent[4]" class="btn btn-danger" v-bind:id="pagesCurrent[4]">
                            {{pagesCurrent[4]}}
                        </button>
                        <button v-on:click="changePage('fifth')" v-if="currentPage != pagesCurrent[4]" class="btn btn-outline-danger" v-bind:id="pagesCurrent[4]">
                            {{pagesCurrent[4]}}
                        </button>

                        <button class="btn btn-outline-danger" v-on:click="changePage(totalPages)">
                            <svg class="bi bi-chevron-right" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 01.708 0l6 6a.5.5 0 010 .708l-6 6a.5.5 0 01-.708-.708L10.293 8 4.646 2.354a.5.5 0 010-.708z" clip-rule="evenodd"/>
                            </svg>
                        </button>
                        
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
    props: ['currentView'],
    data() {
        return{
            View: this.$props.currentView,
            MoviesSeries: [],
            posterUrl: "https://image.tmdb.org/t/p/w300",
            Genres: [],
            optionsGenres: [],
            optionsYear: [],
            selectedgenre: null,
            selectedYear: null,
            totalPages: 1,
            pagesCurrent: [1, 2, 3, 4, 5],
            currentPage: 1,
            keyword: null,
            API_KEY_THEMOVIEDB: config.API_KEY_THEMOVIEDB,
            API_URL: ""
        }
    },
    updated() {
        if(this.View != this.$props.currentView){
            this.resetData();
            this.checkCurrentView();
            this.createYears();
            this.createGenre();
        }
    },
    created() {
        window.scrollTo(0, 0);
        this.$store.commit('updateNavbarIndex', 0);
        this.checkCurrentView();
        this.createYears();
        this.createGenre();
    },
    methods: {
        checkCurrentView() {
            if(this.$props.currentView == "searchseries"){
                if(this.$route.params.genre != null){
                    this.selectedgenre = this.$route.params.genre;
                    this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES' + '&with_genres=' + this.selectedgenre;
                }
                else{
                    this.API_URL = 'https://api.themoviedb.org/3/discover/tv?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES';   
                }
            }
            else if(this.$props.currentView == "searchmovies"){
                if(this.$route.params.genre != null){
                    this.selectedgenre = this.$route.params.genre;
                    this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES' + '&with_genres=' + this.selectedgenre;
                }
                else{
                    this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES';
                }
            }
            else{

            }   
            this.getAPIData(this.API_URL);
        },
        resetData() {
            this.View = this.$props.currentView
            this.MoviesSeries = []
            this.Genres = []
            this.optionsGenres = [],
            this.optionsYear = [],
            this.selectedgenre = null
            this.selectedYear = null
            this.totalPages = 1,
            this.pagesCurrent = [1, 2, 3, 4, 5]
            this.currentPage = 1
            this.keyword = null
        },
        seeMovieSerie(url){
            this.$router.push(url);
        },
        getAPIData(url){

            this.MoviesSeries = [];

            axios.get(url)
            .then(response => {
                (response.data.results).forEach(element => {
                    if(element.poster_path != null){
                        this.MoviesSeries.push(element)
                    }                    
                })
                this.totalPages = response.data.total_pages
            })  
            .catch(function (error) {
                console.log(error);
            })
        },
        createYears() {
            for(let i=new Date().getFullYear(); i>=1900; i--){
                this.optionsYear.push({value: i, text: i});
            }
        },
        createGenre() {

            if(this.$props.currentView == "searchseries") {
                axios.get('https://api.themoviedb.org/3/genre/tv/list?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES')
                .then(response => {
                    (response.data.genres).forEach(genre => {
                        this.optionsGenres.push({value: genre.id, text: genre.name});
                    })
                })
                .catch(function (error) {
                    console.log(error);
                })
            }
            else {
                axios.get('https://api.themoviedb.org/3/genre/movie/list?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES')
                .then(response => {
                    (response.data.genres).forEach(genre => {
                        this.optionsGenres.push({value: genre.id, text: genre.name});
                    })
                })
                .catch(function (error) {
                    console.log(error);
                })
            }
            
        },
        searchKeyword() {
            this.MoviesSeries = []

            if(this.$props.currentView == "searchseries") {
                axios.get('https://api.themoviedb.org/3/search/tv?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES&query=' + this.keyword)
                .then(response => {
                    (response.data.results).forEach(element => {
                        if(element.poster_path != null){
                            this.MoviesSeries.push(element)
                        }                    
                    })
                    this.totalPages = response.data.total_pages
                })  
                .catch(error => {
                    console.log(error);
                }) 
            }
            else {
                axios.get('https://api.themoviedb.org/3/search/movie?api_key=' + this.API_KEY_THEMOVIEDB + '&language=es-ES&query=' + this.keyword)
                .then(response => {
                    (response.data.results).forEach(element => {
                        if(element.poster_path != null){
                            this.MoviesSeries.push(element)
                        }                    
                    })
                    this.totalPages = response.data.total_pages
                })  
                .catch(error => {
                    console.log(error);
                }) 
            }
        },
        applyFilter() {

            if(this.selectedYear != null && this.selectedgenre != null){
                this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&primary_release_year=' + this.selectedYear + '&with_genres=' + this.selectedgenre;
            }
            else if(this.selectedYear == null && this.selectedgenre != null){
                this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&with_genres=' + this.selectedgenre;
            }
            else if(this.selectedYear != null && this.selectedgenre == null){
                this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&primary_release_year=' + this.selectedYear;
            }
            else{
                this.API_URL = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO';
            }                 
            this.getAPIData(this.API_URL);
            this.changePage(1);
        },
        changePage(number) {

            if(number == this.totalPages){
                this.pagesCurrent = []
                for(var i=4; i>=0; i--){
                    this.pagesCurrent.push(number - i);
                }

                this.currentPage = this.totalPages
                
            }
            else if(number === 'first'){

                if(this.pagesCurrent[0] === 1) {
                    this.currentPage = this.pagesCurrent[0]
                }
                else {
                    if(this.pagesCurrent[0] > 2){

                        this.currentPage = this.pagesCurrent[0]
                        this.pagesCurrent = []
                        for(var i=(this.currentPage - 2); i<(this.currentPage + 3); i++){
                            this.pagesCurrent.push(i);
                        }
                    }
                    else {

                        this.currentPage = this.pagesCurrent[0]
                        this.pagesCurrent = []
                        for(var i=(this.currentPage - 1); i<(this.currentPage + 4); i++){
                            this.pagesCurrent.push(i);
                        }
                    }
                }
            }
            else if(number === 'second'){

                if(this.pagesCurrent[0] === 1) {
                    this.currentPage = this.pagesCurrent[1]
                }
                else {
                    this.currentPage = this.pagesCurrent[1]
                    this.pagesCurrent = []
                    for(var i=(this.currentPage - 2); i<(this.currentPage + 3); i++){
                        this.pagesCurrent.push(i);
                    }

                }
            }
            else if(number === 'third'){

                this.currentPage = this.pagesCurrent[2]
            }
            else if(number === 'fourth'){

                if(this.pagesCurrent[4] === this.totalPages) {
                    this.currentPage = this.pagesCurrent[3]
                }
                else {
                    this.currentPage = this.pagesCurrent[3]
                    this.pagesCurrent = []
                    for(var i=(this.currentPage - 2); i<(this.currentPage + 3); i++){
                        this.pagesCurrent.push(i);
                    }
                }
            }
            else if(number === 'fifth'){

                if(this.pagesCurrent[4] === this.totalPages) {
                    this.currentPage = this.pagesCurrent[4]
                }
                else {
                    if(this.pagesCurrent[4] < this.totalPages-2) {
                        this.currentPage = this.pagesCurrent[4]
                        this.pagesCurrent = []
                        for(var i=(this.currentPage - 2); i<(this.currentPage + 3); i++){
                            this.pagesCurrent.push(i);
                        }   
                    }
                    else{
                        this.currentPage = this.pagesCurrent[4]
                        this.pagesCurrent = []
                        for(var i=(this.currentPage - 3); i<(this.currentPage + 2); i++){
                            this.pagesCurrent.push(i);
                        }
                    }
                }
            }
            else if(number == 1){
                this.pagesCurrent = []
                for(var i=1; i<6; i++){
                    this.pagesCurrent.push(i);
                }

                this.currentPage = 1
            }

            this.API_URL = this.API_URL + "&page=" + this.currentPage;
            this.getAPIData(this.API_URL);

        }
    }

}
</script>

<style>
.container-movie-serie{
    margin: 15px 15px;
}

.container-movie-serie div img:hover{
    cursor: pointer;
    transform: scale(1.1);
    transform-origin: center;
}

.container-movie-serie div img{
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