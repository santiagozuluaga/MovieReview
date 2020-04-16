<template>
  <div class="header">
    <header>
      <b-navbar class="bg-navbar" fixed="top" toggleable="md" type="dark" v-bind:variant="window.currentWindow">
        <b-container>

          <b-navbar-brand to="/">
            <img center src="@/assets/MovieReviewLogo.png" class="align-top" alt="Center image" />
          </b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item to="/searchmovie">
                  <span class="font-nav">
                    Películas
                  </span>
                </b-nav-item>
                <b-nav-item to="/searchserie">
                  <span class="font-nav">
                    Series
                  </span>
                </b-nav-item>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
              <b-button v-if="user.isLogged == false" to="/signin" class="font-nav button-nav" variant="danger">Iniciar sesión</b-button>
              <b-button v-if="user.isLogged == false" to="/signup" class="font-nav button-nav"  variant="danger">Crear cuenta</b-button>
              <button v-on:click="goProfile()" v-if="user.isLogged == true" class="font-nav button-nav avatar btn-danger">
                <b-icon icon="person"></b-icon>
              </button>
              <b-button class="font-nav button-nav" v-if="user.isLogged == true" v-on:click="logout()" variant="danger">Cerrar sesion</b-button>
            </b-navbar-nav>
          </b-collapse>
        </b-container>
      </b-navbar>
    </header>

    
    <!--MODALES-->
    <!--
    <b-modal id="signin" hide-header hide-footer>
      <div class="text-center">
        
      </div>
    </b-modal>

    <b-modal id="signup" hide-header hide-footer>
      <div class="text-center">
        
      </div>
    </b-modal>
    -->
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    created() {
      this.$store.dispatch('checkLogin')
    },
    methods: {
      logout() {
        this.$store.dispatch('signoutUser')
        this.$router.push("/")
      },
      goProfile() {
        this.$router.push("/profile")
      }
    },
    computed: {
        ...mapState(['user']),
        ...mapState(['window']),
    }
}
</script>

<style>
.font-nav{
  font-family: 'Roboto', sans-serif;
  color: white;
}

.button-nav{
  margin: 10px;
}

.input-form-nav{
  font-family: 'Roboto', sans-serif;
  margin-top: 15px;
  margin-bottom: 15px;
}

.title-modal-nav{
  font-family: 'Roboto', sans-serif;
  margin-top: 10px;
  margin-bottom: 20px;
}

.avatar{
  border-radius: 100%;
  border: 0px;
  width: 40px;
  height: 40px;
}
</style>