<template>
  <div>
    <div class="container-info-movie info-movie">  
      <MovieComponent v-bind:Id="IdMovie" Type="Movie"/>
    </div>

    <div>
      <b-container class="container-info-movie">
        <b-row class="justify-content-center">
          <b-col lg="10">
            <b-embed
              type="iframe"
              aspect="16by9"
              v-bind:src="UrlVideo+KeyVideos[0].key"
              allowfullscreen>
            </b-embed>
          </b-col>
        </b-row>
      </b-container>  
    </div>

    <div>
      <Comments />
    </div>
  </div>
</template>

<script>
import MovieComponent from "../components/MovieSerie.vue"
import Comments from "../components/Comments.vue"
import axios from 'axios'

export default {
  data() {
    return{
      IdMovie: 0,
      UrlVideo: "https://www.youtube.com/embed/",
      KeyVideos: []
    }
  },
  components: {
    MovieComponent,
    Comments
  },
  created() {

    this.IdMovie = this.$route.params.id;
    let vue = this;
    axios.get('https://api.themoviedb.org/3/movie/'+ this.$route.params.id +'/videos?api_key=eac810b6ade616ce25d01396797173f0')
    .then(function(response) {
      vue.KeyVideos = response.data.results;
    })
    .catch(function (error) {
      console.log(error);
    })
  },
  methods:{
  }
}
</script>

<style>
.info-movie{
  background: #dc3545; 
}

.container-info-movie{
  margin-top: 40px;
}
</style>