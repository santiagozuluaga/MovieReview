<template>
  <div class="container-allmovies">
    <b-container class="container-filter-movie">
      <h3>Descrubir</h3>
      <b-row>
        <b-col class="filter-margin" lg="2">
          <span>Categoria</span>
          <b-form-select v-model="selected" :options="options"></b-form-select>
        </b-col>
        <b-col class="filter-margin" lg="2">
          <span>Año</span>
          <b-form-select v-model="selectedYear" :options="optionsYear"></b-form-select>
        </b-col>
        <b-col lg="2">
          <br>
          <b-button block v-on:click="applyFilter()" variant="danger">Filtrar</b-button>
        </b-col>
      </b-row>
    </b-container>
    <b-container>
      <h3>Peliculas</h3>
      <b-pagination-nav v-model="currentPage" v-bind:number-of-pages="totalPages" use-router v-bind:base-url="currentUrl" align="center">
      </b-pagination-nav>
      <b-row>
        <b-col col="6" class="container-movie text-center" v-bind:key="movie.id" v-for="movie in Movies">
          <div class="container-movie-img" v-on:click="seeMovie(movie.id)">
            <b-img-lazy rounded width="180" v-bind:src="baseUrl+movie.poster_path"></b-img-lazy>
            <div class="title-img">
              <span><strong>{{movie.title}}</strong></span>
            </div>
          </div>
        </b-col>
      </b-row>
      <b-pagination-nav v-model="currentPage" :number-of-pages="totalPages" use-router v-bind:base-url="currentUrl" align="center">
      </b-pagination-nav>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      Movies: [],
      baseUrl: "https://image.tmdb.org/t/p/w200/",
      Genres: [],
      selected: null,
      options: [
        {value: null, text: "Categoria"}
      ],
      selectedYear: null,
      optionsYear: [
        {value: null, text: "Año"}
      ],
      totalPages: 1,
      currentPage: 1,
      previousPage: 1,
      currentUrl: "/allmovies/page="
    }
  },
  created(){

    if(this.$route.params.number != undefined) {

      this.currentPage = this.$route.params.number;
      this.previousPage = this.$route.params.number;
    }
    else {
      
      this.currentPage = 1;
      this.previousPage = 1;
    }


    if(this.$route.params.category == undefined && this.$route.params.year == undefined){

      //GET GENRES
      this.getGenres();

      //GET MOVIES
      this.getMovies();

      //SET YEARS
      this.setYears();
    }
    else{

        this.selected = this.$route.params.category;
        this.selectedYear = this.$route.params.year;
        //GET GENRES
        this.getGenres();

        //GET MOVIES
        this.getMovies();

        //SET YEARS
        this.setYears();
    }
    
  },
  updated() {
    if(this.currentPage != this.previousPage){

      this.previousPage = this.currentPage;
      this.getMovies()
    }
  },
  methods:{
    seeMovie(id){

      this.$router.push('/movie/'+id);
    },
    applyFilter() {
      
      this.$router.push('/allmovies/category=' + this.selected + '/year=' + this.selectedYear);
      if(this.selected != null || this.selectedYear != null) {

        this.currentUrl = "/allmovies/category=" + this.selected + "/year=" + this.selectedYear + "/page=";
      }
      else {

        this.currentUrl = "/allmovies/page=";
      }
      this.currentPage = 1;
      this.previousPage = 1;
      this.getMovies();
    },
    getGenres() {
      let vue = this;
      axios.get('https://api.themoviedb.org/3/genre/movie/list?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
      .then(function(response) {
        (response.data.genres).forEach(genre => {
          vue.options.push({value: genre.id, text: genre.name});
        })
      })
      .catch(function (error) {
        console.log(error);
      })
    },
    getMovies() {

      let vue = this;
      var apiUrl;
      if(this.selected != null && this.selectedYear != null){

        apiUrl = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&primary_release_year=' + this.selectedYear + '&with_genres=' + this.selected
      }
      else if(this.selected == null && this.selectedYear != null){

        apiUrl = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&primary_release_year=' + this.selectedYear
      }
      else if(this.selected != null && this.selectedYear == null){

        apiUrl = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&with_genres=' + this.selected
      }
      else{

        apiUrl = 'https://api.themoviedb.org/3/discover/movie?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage
      }

      axios.get(apiUrl)
      .then(function(response) {
        vue.Movies = response.data.results
        vue.totalPages = response.data.total_pages
      })  
      .catch(function (error) {
        console.log(error);
      })
    },
    setYears() {

      for(var i=new Date().getFullYear(); i>=1900; i--){
        this.optionsYear.push({value: i, text: i});
      }
    }
  }
}
</script>

<style>
.container-allmovies{
  margin-top: 30px;
  margin-bottom: 30px;
}

.container-movie{
  margin: 20px 0px 20px 0px;
}

.container-movie-img:hover{
  cursor: pointer;
}

.filter-margin{
  margin-bottom: 10px;
}

.container-filter-movie{
  margin-bottom: 20px;
}

.title-img{
  margin: 0 auto;
  width: 180px;
  white-space: nowrap; 
  overflow: hidden;
  text-overflow: ellipsis; 
}
</style>
