<template>
  <div class="profile">
    <b-container>
      <b-row>
        <b-col cols="12">
          <div style="display: inline-block;">
            <img src="../assets/user(2).png" width="150"/>
          </div>  
          <div style="display: inline-block;">
            <h3>Usuario: {{User.nickname}}</h3>
          </div>        
        </b-col>
        <b-col cols="6">
          <b-form>
            <h3>Actualizar informacion</h3>
            <b-form-input type="password" class="input-login" required v-model="User.password" placeholder="Nueva contraseña"></b-form-input>
            <b-form-input type="password" class="input-login" required v-model="User.confirmPassword" placeholder="Confirmar contraseña"></b-form-input>
            <b-button block variant="danger">Actualizar contraseña</b-button>
          </b-form>
        </b-col>
        <b-col cols="12">
          <h4>Peliculas favoritas</h4>
          <hr>
          <div>
            Aqui van las peliculas
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      User: {
        nickname: null, 
        email: null,
        password: null, 
        confirmPassword: null
      }
    }
  },
  created() {
      this.$store.commit('updateWindow', 'dark')
      this.User.nickname = localStorage.getItem('nickname')
      this.User.email = localStorage.getItem('email')

  },
  methods: {
    updatePassword() {
      var vue = this

      axios.put('http://127.0.0.1:8000/moviereview/update/password/',{
          "email": this.ser.email,
          "password": this.User.password,
          "newpassword": this.User.confirmPassword})
      .then(response => {
        response
      })
      .catch(error => {
          console.log(error);
      })

    }
  }

}
</script>

<style>
.profile{
  margin-top: 15vh;
}
</style>