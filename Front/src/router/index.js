import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/Profile.vue'),
      meta: {
        auth: true
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: () => import('../views/Signin.vue'),
      meta: {
        auth: false
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue'),
      meta: {
        auth: false
      }
    },
    {
      path: '/searchmovie',
      name: 'searchmovie',
      component: () => import('../views/SearchMovie.vue'),
      props: true
    },
    {
      path: '/searchmovie/:genre',
      name: 'searchmoviegenre',
      component: () => import('../views/SearchMovie.vue'),
      props: true
    },
    {
      path: '/searchserie',
      name: 'searchserie',
      component: () => import('../views/SearchSerie.vue')
    },
    {
      path: '/searchserie/:genre',
      name: 'searchseriegenre',
      component: () => import('../views/SearchSerie.vue'),
      props: true
    },
    {
      path: '/serie/:id',
      name: 'serie',
      component: () => import('../views/Serie.vue')
    },
    {
      path: '/movie/:id',
      name: 'movie',
      component: () => import('../views/Movie.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  
  var usuario = localStorage.getItem("isLogged");
  var autenticacion = to.matched.some(record => record.meta.auth);

  if(!usuario && autenticacion) {
    next('signin');
  }
  else if (usuario && !autenticacion) {
    if(to.name == 'signin' || to.name == 'signup') {
      next('');
    }
    else {
      next();
    }
  }
  else {
    next();
  }
})


export default router
