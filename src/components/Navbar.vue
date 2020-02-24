<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="danger">
      <b-container>

        <b-navbar-brand href="#">MovieReview</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
              <b-nav-item href="#">Novedades</b-nav-item>
              <b-nav-item href="#">Películas</b-nav-item>
              <b-nav-item href="#">Series</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item href="#">Iniciar sesión</b-nav-item>
            <b-nav-item href="#">Registrarse</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
      
    </b-navbar>
  </div>
</template>

<script>
export default {
    name: "Navbar"
}
</script>

<style>

</style>