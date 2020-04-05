<template>
    <div class="container-info-movie info-movie">  
        <b-container class="container-info"> 
            <b-row>
                <b-col class="text-center" lg="4">
                    <div>
                        <b-img class="image-ms" rounded width="300" v-bind:src="baseUrl+ContentComponent.poster_path" alt=""></b-img>
                    </div>
                    <div class="calification-ms">
                        <h4 class="text-inf-ms">¿Ya la viste? Puntuala</h4>
                        <div>
                        <b-icon 
                            @mouseover="mouseover('star1')" 
                            @mouseleave="mouseleave('star1')" 
                            @click="changeStar('star1')"
                            font-scale="2" 
                            class="star-ms" 
                            variant="light"
                            v-bind:icon="stars.pos1">
                        </b-icon>
                        <b-icon 
                            @mouseover="mouseover('star2')" 
                            @mouseleave="mouseleave('star2')" 
                            @click="changeStar('star2')"
                            font-scale="2" 
                            class="star-ms" 
                            variant="light"
                            v-bind:icon="stars.pos2">
                        </b-icon>
                        <b-icon 
                            @mouseover="mouseover('star3')" 
                            @mouseleave="mouseleave('star3')" 
                            @click="changeStar('star3')"
                            font-scale="2" 
                            class="star-ms" 
                            variant="light"
                            v-bind:icon="stars.pos3">
                        </b-icon>
                        <b-icon 
                            @mouseover="mouseover('star4')" 
                            @mouseleave="mouseleave('star4')" 
                            @click="changeStar('star4')"
                            font-scale="2" 
                            class="star-ms" 
                            variant="light"
                            v-bind:icon="stars.pos4">
                        </b-icon>
                        <b-icon 
                            @mouseover="mouseover('star5')" 
                            @mouseleave="mouseleave('star5')" 
                            @click="changeStar('star5')"
                            font-scale="2" 
                            class="star-ms" 
                            variant="light"
                            v-bind:icon="stars.pos5">
                        </b-icon>
                        </div>
                    </div>
                </b-col>
                <b-col>
                    <h3 v-if="Type == 'Movie'" class="title-ms text-info-ms"><strong>{{ContentComponent.title}}</strong></h3>
                    <h3 v-if="Type == 'Serie'" class="title-ms text-info-ms"><strong>{{ContentComponent.original_name}}</strong></h3>
                    <div>
                        <h4 class="text-info-ms"><strong>Sinopsis:</strong></h4>
                        <p class="text-info-ms">{{ContentComponent.overview}}</p>
                    </div>
                    <div v-if="Type == 'Serie'">
                        <p class="text-info-ms"><strong>Fecha de estreno: </strong> {{ContentComponent.first_air_date}}</p>
                        <p class="text-info-ms"><strong>Numero de temporadas: </strong>{{ContentComponent.number_of_seasons}}</p>
                        <p class="text-info-ms"><strong>Numero de episodios: </strong> {{ContentComponent.number_of_episodes}}</p>
                        <h4 class="text-info-ms"><strong>Generos:</strong></h4>
                    </div>
                    <div v-if="Type == 'Movie'">
                        <p class="text-info-ms"><strong>Fecha de estreno: </strong> {{ContentComponent.release_date}}</p>
                        <p class="text-info-ms"><strong>Título original: </strong> {{ContentComponent.original_title}}</p>
                        <p class="text-info-ms"><strong>Duración: </strong>{{ContentComponent.runtime}} minutos</p>
                        <h4 class="text-info-ms"><strong>Generos:</strong></h4>
                    </div>
                    <div>
                        <b-button variant="dark" v-on:click="seeCategories(genre.id)" class="text-info-ms button-ms" v-bind:key="genre.id" v-for="genre in ContentComponent.genres">{{genre.name}}</b-button>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['Id', 'Type'],
    data () {
        return {
            ContentComponent: {},
            baseUrl: "https://image.tmdb.org/t/p/w300/",
            hover: false,
            stars: {
                pos1: "star",
                pos2: "star",
                pos3: "star",
                pos4: "star",
                pos5: "star"
            },
            clickStars: {
                pos1: false,
                pos2: false,
                pos3: false,
                pos4: false,
                pos5: false,
            }
        }
    },
    created() {
        if(this.$props.Type == 'Serie') {
            let vue = this;
            axios.get('https://api.themoviedb.org/3/tv/'+ this.$props.Id +'?api_key=eac810b6ade616ce25d01396797173f0&language=es')
            .then(function(response) {
                console.log(response)
                vue.ContentComponent = response.data
            })
            .catch(function (error) {
                console.log(error);
            })
        }
        else {
            let vue = this;
            axios.get('https://api.themoviedb.org/3/movie/'+ this.$props.Id +'?api_key=eac810b6ade616ce25d01396797173f0&language=es')
            .then(function(response) {
                console.log(response)
                vue.ContentComponent = response.data
            })
            .catch(function (error) {
                console.log(error);
            })
        }        
    },
    methods:{
        mouseover(id){

            this.hover = true;
            if(id == "star1"){
                this.stars.pos1 = "star-fill"
            }
            else if(id == "star2"){
                this.stars.pos1 = "star-fill"
                this.stars.pos2 = "star-fill"
            }
            else if(id == "star3"){
                this.stars.pos1 = "star-fill"
                this.stars.pos2 = "star-fill"
                this.stars.pos3 = "star-fill"
            }
            else if(id == "star4"){ 
                this.stars.pos1 = "star-fill"
                this.stars.pos2 = "star-fill"
                this.stars.pos3 = "star-fill"
                this.stars.pos4 = "star-fill"
            }
            else if(id == "star5"){
                this.stars.pos1 = "star-fill"
                this.stars.pos2 = "star-fill"
                this.stars.pos3 = "star-fill"
                this.stars.pos4 = "star-fill"
                this.stars.pos5 = "star-fill"
            }
        },
        mouseleave(id){

            this.hover = false;
            if(id == "star1"){
                if(this.clickStars.pos1 == false){
                this.stars.pos1 = "star"
                }        
            }
            else if(id == "star2"){
                if(this.clickStars.pos2 == false){
                this.stars.pos1 = "star"
                this.stars.pos2 = "star"
                }
            }
            else if(id == "star3"){
                if(this.clickStars.pos3 == false){
                this.stars.pos1 = "star"
                this.stars.pos2 = "star"
                this.stars.pos3 = "star"
                }
            }
            else if(id == "star4"){ 
                if(this.clickStars.pos4 == false){
                this.stars.pos1 = "star"
                this.stars.pos2 = "star"
                this.stars.pos3 = "star"
                this.stars.pos4 = "star"
                }
            }
            else if(id == "star5"){
                if(this.clickStars.pos5 == false){
                this.stars.pos1 = "star"
                this.stars.pos2 = "star"
                this.stars.pos3 = "star"
                this.stars.pos4 = "star"
                this.stars.pos5 = "star"
                }
            }
        },
        changeStar(id){

            if(id == "star1"){
                this.clickStars.pos1 = true;
            }
            else if(id == "star2"){
                this.clickStars.pos2 = true;
            }
            else if(id == "star3"){
                this.clickStars.pos3 = true;
            }
            else if(id == "star4"){ 
                this.clickStars.pos4 = true;
            }
            else if(id == "star5"){
                this.clickStars.pos5 = true;
            }
        },
        seeCategories(id){
            var url = "/allmovies/category=" + id + "/year=null"
            this.$router.push(url);
        }
    }
}
</script>

<style>
.info-movie{
  background: #dc3545; 
}

.container-info-movie{
  margin-bottom: 40px;
}

.container-info{
  padding-top: 40px;
  padding-bottom: 40px;
}

.ms-genres{
  display: flex;
}

.text-info-ms{
  color: white;
  font-family: 'Roboto', sans-serif;
}

.title-ms{
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 30px;
}

.button-ms{
  margin-top: 10px;
  margin-right: 10px;
}

.star-ms{
  margin-top: 10px;
  margin-right: 10px;
  margin-left: 10px;
  cursor: pointer;
}

.image-ms:hover{
  cursor: pointer;
}

.calification-ms{
  margin-top: 20px;
}
</style>