<template>
  <div class="searchserie">
      <b-container>
            <h3>Descubrir</h3>
            <b-row>
            <b-col class="input-filter" lg="3">
                <b-form-select  v-model="selectedgenre" :options="optionsGenres"></b-form-select>
            </b-col>
            <b-col class="input-filter" lg="3">
                <b-form-select  v-model="selectedYear" :options="optionsYear"></b-form-select>
            </b-col>
            <b-col class="input-filter" lg="2">
                <b-button block v-on:click="applyFilter()" variant="danger">Filtrar</b-button>
            </b-col>
            <b-col class="input-filter" lg="6">
                <b-form-input v-model="keyword" placeholder="Ingresa una palabra clave"></b-form-input>
            </b-col>
            <b-col class="input-filter" lg="2">
                <b-button block v-on:click="searchSeries()" variant="danger">Buscar</b-button>
            </b-col>
            <b-col cols="12">   
                <h3>Peliculas</h3>
            </b-col>
            <b-col class="container-serie text-center" v-bind:key="serie.id" v-for="serie in Series">
                <div v-on:click="seeSerie(serie.id)">
                    <img v-bind:src="baseUrl+serie.poster_path" alt=""/>
                </div>
            </b-col>
            <!--
            <b-col cols="12">
                Paginacion
            </b-col>
            -->
          </b-row>
      </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['genre'],
    data() {
        return{
            Series: [],
            baseUrl: "https://image.tmdb.org/t/p/w300/",
            Genres: [],
            selectedgenre: null,
            optionsGenres: [
                {value: null, text: "Categoria"}
            ],
            selectedYear: null,
            optionsYear: [
                {value: null, text: "Año"}
            ],
            totalPages: 1,
            keyword: null
        }
    },
    created() {

        this.$store.commit('updateWindow', 'dark')

        for(var i=new Date().getFullYear(); i>=1900; i--){
            this.optionsYear.push({value: i, text: i});
        }

        let vue = this;
        var apiUrlSerie;    

        if(this.$props.genre != null){
            this.selectedgenre = this.$props.genre;
            apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&with_genres=' + this.$props.genre;
        }
        else{
            apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO';
        }

        axios.get(apiUrlSerie)
        .then(function(response) {
            (response.data.results).forEach(serie => {
                if(serie.poster_path != null){
                    vue.Series.push(serie)
                }                    
            })
            vue.totalPages = response.data.total_pages
        })  
        .catch(function (error) {
            console.log(error);
        })

        axios.get('https://api.themoviedb.org/3/genre/tv/list?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO')
        .then(function(response) {
            (response.data.genres).forEach(genre => {
            vue.optionsGenres.push({value: genre.id, text: genre.name});
            })
        })
        .catch(function (error) {
            console.log(error);
        })
        
    },
    methods: {
        seeSerie(id){
            this.$router.push('/serie/'+id);
        },
        searchSeries() {
            let vue = this;
            vue.Series = []
            
            axios.get('https://api.themoviedb.org/3/search/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO&query=' + vue.keyword)
            .then(function(response) {
                (response.data.results).forEach(serie => {
                    if(serie.poster_path != null){
                        vue.Series.push(serie)
                    }                    
                })
                vue.totalPages = response.data.total_pages
            })  
            .catch(function (error) {
                console.log(error);
            })
        },
        applyFilter() {

            let vue = this;
            vue.Series = []
            var apiUrlSerie;

            if(vue.selectedYear != null && vue.selectedgenre != null){
                apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&first_air_date_year=' + this.selectedYear + '&with_genres=' + this.selectedgenre
            }
            else if(vue.selectedYear == null && vue.selectedgenre != null){
                apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&with_genres=' + this.selectedgenre
            }
            else if(vue.selectedYear != null && vue.selectedgenre == null){
                apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO' + '&first_air_date_year=' + this.selectedYear
            }
            else{
                apiUrlSerie = 'https://api.themoviedb.org/3/discover/tv?api_key=eac810b6ade616ce25d01396797173f0&language=es-CO'
            }

            axios.get(apiUrlSerie)
            .then(function(response) {
                (response.data.results).forEach(serie => {
                    if(serie.poster_path != null){
                        vue.Series.push(serie)
                    }                    
                })
                vue.totalPages = response.data.total_pages
            })  
            .catch(function (error) {
                console.log(error);
            })
        },
        changePage() {

        }
    }
}
</script>

<style>
.searchserie{
    margin-top: 15vh;
}

.container-serie{
    margin: 10px 0;
    text-align: center;
}

.container-serie div img:hover{
    cursor: pointer;
    transform: scale(1.1);
    transform-origin: center;
}

.container-serie div img{
    border-radius: 5px;
    width: 190px;
    height: 285px;

}

.input-filter{
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
