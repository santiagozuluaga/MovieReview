<template>
  <div class="home">
    <CardCarousel />

    <b-container class="container-news">
      <h3>Últimas películas</h3>
      <b-pagination-nav v-model="currentPage" v-bind:number-of-pages="totalPages" use-router base-url="/page=" align="center">
      </b-pagination-nav>
      <b-row>
        <b-col col="6" lg="2" class="container-movie text-center" v-bind:key="movie.id" v-for="movie in Movies">
          <div>
            <b-img v-on:click="seeMovie(movie.id)" class="container-movie-img" rounded width="160" v-bind:src="baseUrl+movie.poster_path" alt=""></b-img>
          </div>
        </b-col>
      </b-row>
      <b-pagination-nav v-model="currentPage" :number-of-pages="totalPages" use-router base-url="/page=" align="center">
      </b-pagination-nav>
    </b-container>
  </div>
</template> 

<script>
import CardCarousel from '@/components/CardCarousel.vue'
import Language from '@/assets/Language.json'
import axios from 'axios'

export default {
  components:{
    CardCarousel
  },
  data(){
    return{
      Movies: [],
      baseUrl: "https://image.tmdb.org/t/p/w200/",
      LanguageJson: Language,
      totalPages: 1,
      currentPage: 1,
      previousPage: 1
    }
  },
  created(){

    let vue = this;
    if(this.$route.params.number != undefined) {

      this.currentPage = this.$route.params.number
      this.previousPage = this.$route.params.number      
    }
    else {

      this.currentPage = 1;
      this.previousPage = 1;
    }

    axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage)
    .then(function(response) {
      vue.Movies = response.data.results
      vue.totalPages = response.data.total_pages
    })
    .catch(function (error) {
      console.log(error);
    })
    
  },
  updated() {
    if(this.currentPage != this.previousPage){
      this.changePage(this.currentPage);
      this.previousPage = this.currentPage;
    }
  },
  methods:{
    seeMovie(id){

      this.$router.push('/movie/'+id);
    },
    changePage(current) {
      
      let vue = this;
      axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + current)
      .then(function(response) {
        vue.Movies = response.data.results
        vue.totalPages = response.data.total_pages
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  }
}
</script>

<style>
.container-movie{
  margin: 20px 0px 20px 0px;
}

.container-movie-img:hover{
  cursor: pointer;
}

.container-news{
  margin-top: 30px;
}
</style>