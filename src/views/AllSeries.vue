<template>
  <div class="container-allseries">
    <b-container class="container-filter-serie">
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
      <h3>Series</h3>
      <b-pagination-nav v-model="currentPage" :number-of-pages="totalPages" use-router v-bind:base-url="currentUrl" align="center">
      </b-pagination-nav>
      <b-row>
        <b-col col="6" lg="2" class="container-serie text-center" v-bind:key="serie.id" v-for="serie in Series">
          <div>
            <b-img class="container-serie-img" v-on:click="seeSerie(serie.id)" rounded width="160" v-bind:src="baseUrl+serie.poster_path"></b-img>
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
      Series: [],
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
      totalPages: 0,
      currentPage: 1,
      previousPage: 1,
      currentUrl: "/allseries/page="
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

      //GET SERIES
      this.getSeries();

      //SET YEARS
      this.setYears();
    }
    else{

        this.selected = this.$route.params.category;
        this.selectedYear = this.$route.params.year;
        //GET GENRES
        this.getGenres();

        //GET SERIES
        this.getSeries();

        //SET YEARS
        this.setYears();
    }
    
  },
  updated() {
    if(this.currentPage != this.previousPage){

      this.previousPage = this.currentPage;
      this.getSeries();
    }
  },
  methods:{
    seeSerie(id){

      this.$router.push('/serie/'+id);
    },
    applyFilter() {
      
      this.$router.push('/allseries/category=' + this.selected + '/year=' + this.selectedYear);
      if(this.selected != null || this.selectedYear != null) {

        this.currentUrl = "/allseries/category=" + this.selected + "/year=" + this.selectedYear + "/page=";
      }
      else {

        this.currentUrl = "/allseries/page=";
      }  
      this.currentPage = 1;
      this.previousPage = 1;
      this.getSeries();
    },
    getGenres() {

      let vue = this;
      axios.get('https://api.themoviedb.org/3/genre/tv/list?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
      .then(function(response) {
        (response.data.genres).forEach(genre => {
          vue.options.push({value: genre.id, text: genre.name});
        })
      })
      .catch(function (error) {
        console.log(error);
      })
    },
    getSeries() {

      let vue = this;
      var apiUrl;
      if(this.selected != null && this.selectedYear != null){

        apiUrl = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&primary_release_year=' + this.selectedYear + '&with_genres=' + this.selected
      }
      else if(this.selected == null && this.selectedYear != null){

        apiUrl = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&primary_release_year=' + this.selectedYear
      }
      else if(this.selected != null && this.selectedYear == null){

        apiUrl = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage + '&with_genres=' + this.selected
      }
      else{

        apiUrl = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage
      }

      axios.get(apiUrl)
      .then(function(response) {
        vue.Series = response.data.results
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
.container-allseries{
  margin-top: 30px;
  margin-bottom: 30px;
}

.container-serie{
  margin: 20px 0px 20px 0px;
}

.container-serie-img:hover{
  cursor: pointer;
}

.filter-margin{
  margin-bottom: 10px;
}

.container-filter-serie{
  margin-bottom: 20px;
}
</style>
