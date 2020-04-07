<template>
  <div class="home">

    <CardCarousel />

    <b-container class="container-news">
      <h3>Últimas películas</h3>
      <b-row>
        <b-col class="container-movie text-center" v-bind:key="movie.id" v-for="movie in Movies">
          <div class="container-movie-img" v-on:click="seeMovie(movie.id)">
            <b-img-lazy rounded height="280" v-bind:src="baseUrl+movie.poster_path" alt=""></b-img-lazy>
            <div class="title-img">
              <span><strong>{{movie.title}}</strong></span>
            </div>
          </div>
        </b-col>
      </b-row>
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
      LanguageJson: Language
    }
  },
  created(){

    let vue = this;

    axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&page=' + this.currentPage)
    .then(function(response) {
      vue.Movies = response.data.results
    })
    .catch(function (error) {
      console.log(error);
    })
    
  },
  methods:{
    seeMovie(id){

      this.$router.push('/movie/'+id);
    }
  }
}
</script>

<style>
.container-movie{
  margin: 20px 0px 20px 0px;
}

.title-img{
  margin: 0 auto;
  width: 180px;
  white-space: nowrap; 
  overflow: hidden;
  text-overflow: ellipsis; 
}

.container-movie-img:hover{

  cursor: pointer;
}

.container-news{
  margin-top: 30px;
}
</style>