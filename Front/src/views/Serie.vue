<template>
  <div>
    <div class="container-info-serie info-serie">  
      <SerieComponent v-bind:Id="IdSerie" Type="Serie"/>
    </div>

    <div>
      <b-container class="container-info-serie">
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
import SerieComponent from "../components/MovieSerie.vue"
import Comments from "../components/Comments.vue"
import axios from 'axios'

export default {
  data() {
    return{
      IdSerie: 0,
      UrlVideo: "https://www.youtube.com/embed/",
      KeyVideos: []
    }
  },
  components: {
    SerieComponent,
    Comments
  },
  created() {
    this.IdSerie = this.$route.params.id;

    let vue = this;
    axios.get('https://api.themoviedb.org/3/tv/'+ this.$route.params.id +'/videos?api_key=eac810b6ade616ce25d01396797173f0')
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
.info-serie{
  background: #dc3545; 
}

.container-info-serie{
  margin-top: 40px;
}
</style>