import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/login/signin',
      name: 'Signin',
      component: () => import('../views/Login.vue'),
      props: {
        currentView: 'signin'
      },
      meta: {
        auth: false
      }
    },
    {
      path: '/login/signup',
      name: 'Signup',
      component: () => import('../views/Login.vue'),
      props: {
        currentView: 'signup'
      },
      meta: {
        auth: false
      }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('../views/Profile.vue'),
      meta: {
        auth: true
      }
    },
    {
      path: '/search/movies',
      name: 'SearchMovies',
      component: () => import('../views/ViewSearch.vue'),
      props: {
        currentView: 'searchmovies'
      }
    },
    {
      path: '/search/series',
      name: 'SearchSeries',
      component: () => import('../views/ViewSearch.vue'),
      props: {
        currentView: 'searchseries'
      }
    },
    {
      path: '/search/movies/:genre',
      name: 'SearchMoviesgenre',
      component: () => import('../views/ViewSearch.vue'),
      props: {
        currentView: 'searchmovies'
      }
    },
    {
      path: '/search/series/:genre',
      name: 'SearchSeriesgenre',
      component: () => import('../views/ViewSearch.vue'),
      props: {
        currentView: 'searchseries'
      }
    },
    {
      path: '/serie/:id',
      name: 'Series',
      component: () => import('../views/MovieSerie.vue'),
      props: {
        currentView: 'serie'
      }
    },
    {
      path: '/movie/:id',
      name: 'Movies',
      component: () => import('../views/MovieSerie.vue'),
      props: {
        currentView: 'movie'
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  
  var usuario = localStorage.getItem("isLogged");
  var autenticacion = to.matched.some(record => record.meta.auth);

  if(!usuario && autenticacion) {
    next('Signin');
  }
  else if (usuario && !autenticacion) {
    if(to.name == 'Signin' || to.name == 'Signup') {
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
