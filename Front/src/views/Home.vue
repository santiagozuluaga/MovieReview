<template>
  <div class="home">

    <div class="loading-screen" v-if="Movies[0] == null && Series[0] == null">
      <img src="../assets/refresh.png" width="100">
    </div>

    <div v-if="Movies[0] != null && Series[0] != null">
      <Carousel 
      v-bind:Movies="[Movies[0], Movies[1], Movies[2], Movies[3], Movies[4]]"/>

      <!--PELICULAS-->
      <div class="container-home">

        <div class="container-title">
          <h3 class="title-recent">Peliculas recientes</h3>
        </div>

        
        <div class="container-recent">
          
          <button v-on:click="changePageMovie('left')" class="left">
            <b-icon icon="chevron-left"></b-icon>
          </button>
          <button v-on:click="changePageMovie('right')" class="right">
            <b-icon icon="chevron-right"></b-icon>
          </button>

          <div v-if="currentPageMovie == 1 && !viewinsmall" class="recents">
            <div v-bind:key="n" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n-1].id)">
              <img v-bind:src="baseUrl+Movies[n-1].poster_path" alt="" />
            </div>
          </div>

          <div v-if="currentPageMovie == 2 && !viewinsmall" class="recents">
            <div v-bind:key="n+5" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+4].id)">
              <img v-bind:src="baseUrl+Movies[n+4].poster_path" alt="" />
            </div>
          </div>

          <div v-if="currentPageMovie == 3 && !viewinsmall" class="recents">
            <div v-bind:key="n+9" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+9].id)">
              <img v-bind:src="baseUrl+Movies[n+9].poster_path" alt="" />
            </div>
          </div>

          <div v-if="currentPageMovie == 4 && !viewinsmall" class="recents">
            <div v-bind:key="n+14" v-for="n in 5" v-on:click="seeMovieSerie('/movie/'+Movies[n+14].id)">
              <img v-bind:src="baseUrl+Movies[n+14].poster_path" alt="" />            
            </div>
          </div>

          <div v-if="viewinsmall" class="recents">
            <div v-bind:key="movie.id" v-for="movie in Movies" v-on:click="seeMovieSerie('/movie/'+movie.id)">
              <img v-bind:src="baseUrl+movie.poster_path" alt="" />            
            </div>
          </div>
        </div>
      </div>

      <!--SERIES-->
      <div class="container-home">

        <div class="container-title">
          <h3 class="title-recent">Series recientes</h3>
        </div>

        <div>
          <div class="container-recent">
            
            <button v-on:click="changePageSerie('left')" class="left">
              <b-icon icon="chevron-left"></b-icon>
            </button>
            <button v-on:click="changePageSerie('right')" class="right">
              <b-icon icon="chevron-right"></b-icon>
            </button>

            <div v-if="currentPageSerie == 1 && !viewinsmall" class="recents">
              <div v-bind:key="n" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n-1].id)">
                <img v-bind:src="baseUrl+Series[n-1].poster_path" alt="" />
              </div>
            </div>

            <div v-if="currentPageSerie == 2 && !viewinsmall" class="recents">
              <div v-bind:key="n+5" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+4].id)">
                <img v-bind:src="baseUrl+Series[n+4].poster_path" alt="" />
              </div>
            </div>

            <div v-if="currentPageSerie == 3 && !viewinsmall" class="recents">
              <div v-bind:key="n+9" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+9].id)">
                <img v-bind:src="baseUrl+Series[n+9].poster_path" alt="" />
              </div>
            </div>

            <div v-if="currentPageSerie == 4 && !viewinsmall" class="recents">
              <div v-bind:key="n+14" v-for="n in 5" v-on:click="seeMovieSerie('/serie/'+Series[n+14].id)">
                <img v-bind:src="baseUrl+Series[n+14].poster_path" alt="" />            
              </div>
            </div>

            <div v-if="viewinsmall" class="recents">
            <div v-bind:key="serie.id" v-for="serie in Series" v-on:click="seeMovieSerie('/serie/'+serie.id)">
              <img v-bind:src="baseUrl+serie.poster_path" alt="" />            
            </div>
          </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template> 

<script>
import axios from 'axios'
import Carousel from '@/components/Carousel.vue'

export default {
  components:{
    Carousel
  },
  data(){
    return{
      Movies: [],
      Series: [],
      baseUrl: "https://image.tmdb.org/t/p/w300",
      currentPageMovie: 1,
      viewinsmall: false,
      currentPageSerie: 1
    }
  },
  created(){
    window.addEventListener('resize', this.resizeHandler)

    if(screen.width <= 800){
      this.$store.commit('updateWindow', 'dark')
      this.viewinsmall = true
    }
    else {
      window.addEventListener('scroll', this.scrollHandler)
      this.$store.commit('updateWindow', null)
    }

    let vue = this;

    axios.get('https://api.themoviedb.org/3/movie/now_playing?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
    .then(function(response) {
      vue.Movies = response.data.results
    })
    .catch(function (error) {
      console.log(error);
    })

    axios.get('https://api.themoviedb.org/3/tv/on_the_air?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
    .then(function(response) {
      vue.Series = response.data.results
    })
    .catch(function (error) {
      console.log(error);
    })
    
  },
  beforeDestroy() {

    if(screen.width > 800){
      window.removeEventListener('scroll', this.scrollHandler)
    }
  },
  methods:{
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
        this.$store.commit('updateWindow', null)
      }
      else {
        this.$store.commit('updateWindow', 'dark')
      }
    },
    resizeHandler() {
      if(screen.width <= 800){
        this.viewinsmall = true
        this.$store.commit('updateWindow', 'dark')
        window.removeEventListener('scroll', this.scrollHandler)
      }
      else {
        this.viewinsmall = false
        window.addEventListener('scroll', this.scrollHandler)
        this.$store.commit('updateWindow', null)
      }
    }
  }
}
</script>

<style>
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
}

.left, .right {
  position: absolute;
  height: 50%;
  background: rgba(0,0,0,0.3);
  border: none;
  color: black
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

.loading-screen{
  height: 100vh;
  position: relative;
  text-align: center;
}

.loading-screen img{
  position: absolute;
  top: calc(40%);
  animation: rotation 2s infinite linear;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}


@media only screen and (min-width: 1200px) {
  .recents div img{
    width: 190px;
    height: 285px;
  }

  .container-home{
    width: 85%;
    margin: 0 auto;
  }
}

@media only screen and (max-width: 1200px) {
  .recents div img{
    width: 165px;
    height: 248px;
  }

  .container-home{
    width: 95%;
    margin: 0 auto;
  }
}

@media only screen and (max-width: 1100px) {
  .recents div img{
    width: 160px;
    height: 240px;
  }
}

@media only screen and (max-width: 1000px) {
  .recents div img{
    width: 148px;
    height: 222px;
  }
}

@media only screen and (max-width: 900px) {
  .recents div img{
    width: 135px;
    height: 203px;
  }

  .recents div{
    display: inline-block;
    margin: 10px 8px;
  }
}

@media only screen and (max-width: 800px) {
  .left{
    display: none;
  }

  .right{
    display: none;
  }
}
</style>
