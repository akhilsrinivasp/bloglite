import { createStore } from 'vuex'

export default createStore({
  state: {
    access_token: localStorage.getItem('access_token') || null,
    refresh_token: localStorage.getItem('refresh_token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
    isLogged: localStorage.getItem('isLogged') || false,
    url: "http://127.0.0.1:5050/api/v1/",
    // url: "http://192.168.0.101:5050/api/v1/",    
    blogs: [],
    feed: [],
    followers: [],
    following: [],
  },
  getters: {
  },
  mutations: {
    setBlogs(state, blogs) {
      state.blogs = blogs
    },
    setUser(state, user) {
      state.user = user
      localStorage.setItem('user', JSON.stringify(user))
    },
    setTokens(state, tokens) {
      state.access_token = tokens.access_token
      state.refresh_token = tokens.refresh_token
      state.isLogged = true
      localStorage.setItem('access_token', tokens.access_token)
      localStorage.setItem('refresh_token', tokens.refresh_token)
      localStorage.setItem('isLogged', true)
    },
    setFeed(state, feed) {
      state.feed = feed
    }
  },
  actions: {
    async getBlogs({ commit }) {
      const response = await fetch( this.state.url + 'public',
      { 
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Cross-Origin-Resource-Policy': 'cross-origin'
        }
      })
      const data = await response.json()
      commit('setBlogs', data)
    },
    async login({ commit }, user) {
      const response = await fetch( this.state.url + 'login',
      { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user)
      })
      const data = await response.json()
      commit('setTokens', data)
      const response2 = await fetch( this.state.url + 'user', 
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + this.state.access_token
        }
      })
      const data2 = await response2.json()
      commit('setUser', data2)
    },
    async refresh({ commit }) { 
      const response = await fetch( this.state.url + 'refresh',
      { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + this.state.refresh_token
        },
      })
      // if error then return 
      if (!response.ok) {
        this.state.isLogged = false
        localStorage.setItem('isLogged', false)
        return
      }
      const data = await response.json()
      commit('setTokens', data)
    },
    logout({ commit }) {
      this.state.isLogged = false
      localStorage.setItem('isLogged', false)
      localStorage.setItem('access_token', null)
      localStorage.setItem('refresh_token', null)
      localStorage.setItem('user', null)
      
      const token = {
        access_token: null,
        refresh_token: null
      }
      commit('setTokens', token)
      commit('setUser', null)
    }, 
    async getFeed({ commit }) {
      fetch( this.state.url + 'user/feed',
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + this.state.access_token,
        }
      })
      .then(response => response.json())
      .then(data => {
        commit('setFeed', data)
      }
      )
    },
  },
  modules: {
  }
})
