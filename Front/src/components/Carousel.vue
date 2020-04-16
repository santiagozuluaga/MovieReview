<template>
    <b-carousel
        class="carousel-bootstrap bg-dark"
        v-model="slide"
        :iterval="4000"
        controls
        indicators>
        <b-carousel-slide v-bind:key="movie.id" v-for="movie in Movies">
            <template v-slot:img>
                <img class="img-carousel" v-bind:src="backgroundUrl + movie.backdrop_path" />
                <div class="panel-carousel">
                    <div class="container h-100">
                        <div class="d-flex align-items-center justify-content-center h-100">
                            <div class="container-info-carousel text-center">
                                <h3>{{movie.title}}</h3>
                                <div>
                                    <b-button v-on:click="seeMovieSerie('/movie/'+movie.id)" variant="danger">Ver informacion</b-button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </b-carousel-slide>
    </b-carousel>
</template>

<script>
export default {
    props: ['Movies'],
    data () {
        return {
            backgroundUrl: 'https://image.tmdb.org/t/p/original/',
            slide: 0,
        }
    },
    methods:{
        seeMovieSerie(url){
            this.$router.push(url);
        }
    }
}
</script>

<style>
.container-info-carousel{
    margin-top: 50vh;
    color: white;
}

.panel-carousel{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0, .6);
}

.img-carousel{
    width: 100%;
}

.carousel-bootstrap{
    height: 100vh;
    overflow: hidden;
}

@media only screen and (max-width: 1200px) {
    .carousel-bootstrap{
        height: 100%;
        overflow: hidden;
    }
}

@media only screen and (max-width: 900px) {
    .container-info-carousel{
        margin-top: 40vh;
    }
}


@media only screen and (max-width: 800px) {
    .carousel-bootstrap{
        margin-top: 7vh;
    }

    .container-info-carousel{
        margin-top: 30vh;
    }
}

@media only screen and (max-width: 600px) {
    .container-info-carousel{
        margin-top: 15vh;
    }
}

@media only screen and (max-width: 500px) {
    .container-info-carousel{
        margin-top: 10vh;
    }
}

@media only screen and (max-width: 400px) {
    .container-info-carousel{
        margin-top: 0vh;
    }
}
</style>
