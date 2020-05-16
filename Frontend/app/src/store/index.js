import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      userNickname: null,
      userEmail: null,
      isLogged: false
    },
    navbarIndex: 0
  },
  mutations: {
    login(state) {
      state.user.isLogged = true
    },
    signout(state) {
      state.user.userEmail = null
      state.user.userNickname = null
      state.user.isLogged = false
    },
    updateEmail(state, newEmail) {
      state.user.userEmail = newEmail
    },
    updateNickname(state, newNickname) {
      state.user.userNickname = newNickname
    },
    updateNavbarIndex(state, newIndex) {
      state.navbarIndex = newIndex
    }
  },
  actions: {
    signinUser({commit}, {Nickname, Email, Token}) {
      localStorage.setItem("nickname", Nickname)
      localStorage.setItem("email", Email)
      localStorage.setItem("isLogged", true)
      commit('login')
      commit('updateNickname', Nickname)
      commit('updateEmail', Email)
    },
    signupUser({commit}, {Nickname, Email, Token}) {
      localStorage.setItem("nickname", Nickname)
      localStorage.setItem("email", Email)
      localStorage.setItem("isLogged", true)
      commit('login')
      commit('updateNickname', Nickname)
      commit('updateEmail', Email)
    },
    signoutUser({commit}){
      localStorage.removeItem("nickname")
      localStorage.removeItem("email")
      localStorage.removeItem("isLogged")
      commit('signout')
    },
    checkLogin({commit}) {
      
      if(localStorage.getItem("isLogged")){
        commit('login')
        commit('updateNickname', localStorage.getItem("nickname"))
        commit('updateEmail', localStorage.getItem("email"))
      }
    }
  },
  modules: {
  }
})
