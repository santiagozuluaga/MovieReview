import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      userNickname: null,
      userEmail: null,
      isLogged: false
    },
    window: {
      currentWindow: 'dark'
    }
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
      state.user.userEmail = newNickname
    },
    updateToken(state, newNickname) {
      state.user.userEmail = newNickname
    },
    updateWindow(state, newWindow) {
      state.window.currentWindow = newWindow
    }
  },
  actions: {
    signinUser({commit}, {Nickname, Email, Token}) {
      localStorage.setItem("nickname", Nickname)
      localStorage.setItem("email", Email)
      localStorage.setItem("tokenId", Token)
      localStorage.setItem("isLogged", true)
      commit('login')
      commit('updateNickname', Nickname)
      commit('updateEmail', Email)
    },
    signupUser({commit}, {Nickname, Email, Token}) {
      localStorage.setItem("nickname", Nickname)
      localStorage.setItem("email", Email)
      localStorage.setItem("tokenId", Token)
      localStorage.setItem("isLogged", true)
      commit('login')
      commit('updateNickname', Nickname)
      commit('updateEmail', Email)
    },
    signoutUser({commit}){
      localStorage.removeItem("nickname")
      localStorage.removeItem("email")
      localStorage.removeItem("tokenId")
      localStorage.removeItem("isLogged")
      commit('signout')
    },
    checkLogin({commit}) {
      
      if(localStorage.getItem("isLogged")){
        commit('login')
      }
    }
  },
  modules: {
  }
})
