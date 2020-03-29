<template>
  <div>
    <!--NAVBAR-->
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-container>

        <b-navbar-brand to="/">
          <img center src="@/assets/MovieReviewLogo.png" class="align-top" alt="Center image" />
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <!--
              <b-nav-item to="/news">
                <span class="font-nav">
                  Novedades
                </span>
              </b-nav-item>
              -->
              <b-nav-item to="/allmovies">
                <span class="font-nav">
                  Películas
                </span>
              </b-nav-item>
              <b-nav-item to="/allseries">
                <span class="font-nav">
                  Series
                </span>
              </b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown class="button-nav" text="Idioma">
                <b-dropdown-item href="#">Español</b-dropdown-item>
                <b-dropdown-item href="#">English</b-dropdown-item>
                <b-dropdown-item href="#">Français</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-button v-on:click="openModal('signin')" class="font-nav button-nav" variant="danger">Iniciar sesión</b-button>
            <b-button v-on:click="openModal('signup')" class="font-nav button-nav" variant="danger">Crear cuenta</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>

    
    <!--MODALES-->
    <b-modal id="signin" hide-header hide-footer>
      <div class="text-center">
        <h3 class="title-modal-nav">Iniciar sesión</h3>
        <b-form @submit="onSubmit">
            <b-form-input required class="input-form-nav" size="lg" v-model="User.Email" placeholder="Correo electrónico"></b-form-input>
            <b-form-input required class="input-form-nav" size="lg" v-model="User.Password" placeholder="Contraseña"></b-form-input>
            <b-button class="font-nav" size="lg" type="submit" block variant="danger">Iniciar sesión</b-button>
        </b-form>
        <hr /> 
        <p>¿Aún no tienes cuenta?</p>
        <b-button v-on:click="openModal('signup'), closeModal('signin')" class="font-nav" size="lg" block variant="dark">Crear cuenta</b-button>
      </div>
    </b-modal>

    <b-modal id="signup" hide-header hide-footer>
      <div class="text-center">
        <h3 class="title-modal-nav">Crear cuenta</h3>
        <b-form @submit="onSubmit">
          <b-form-input required class="input-form-nav" size="lg" v-model="User.Nickname" placeholder="Nombre de usuario"></b-form-input>
            <b-form-input required class="input-form-nav" size="lg" v-model="User.Email" placeholder="Correo electrónico"></b-form-input>
            <b-form-input required class="input-form-nav" size="lg" v-model="User.Password" placeholder="Contraseña"></b-form-input>
            <b-form-input required class="input-form-nav" size="lg" v-model="User.ConfirmPassword" placeholder="Confirmar contraseña"></b-form-input>
            <b-button class="font-nav" size="lg" type="submit" block variant="danger">Crear cuenta</b-button>
        </b-form>
        <hr /> 
        <p>¿Ya tienes una cuenta?</p>
        <b-button v-on:click="openModal('signin'), closeModal('signup')" class="font-nav" size="lg" block variant="dark">Iniciar sesión</b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
    name: "Navbar",
    data(){
      return{
        User: {
          Nickname: "",
          Email: "",
          Password: "",
          ConfirmPassword: ""
        }
      }
    },
    methods: {
      onSubmit(){
        console.log("Hola")
      },
      openModal(nombre){
        this.$bvModal.show(nombre);
      },
      closeModal(nombre){
        this.$bvModal.hide(nombre);
      }
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
</style>