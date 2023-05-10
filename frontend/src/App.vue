<template>
	<nav class="navbar navbar-expand-lg navbar-light">
		<div class="navbar-brand">
			<router-link class="elements" to="/">Bloglite</router-link>
		</div>
		<router-link id="feed" class="elements" to="/feed" v-if="isLogged">Feed</router-link>
		<li class = "d-flex ms-auto" style = "margin-right: 12px;">
			<SearchUser/>
		</li>
		<router-link id="upload-blog" class="elements " to="/upload" v-if="isLogged" >
			<img :src="upload_icon" alt="Profile" class="profile" width="29" style = "margin-right: 10px;">
		</router-link>

		<li class="nav-item dropdown-combined  justify-content-end dropdown d-flex" v-if="!isLogged">
			<a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
				<img :src="profile" alt="Profile" class="profile" width="35">
			</a>
			<ul class="dropdown-menu">
				<li><router-link id="login" class="elements" to="/login">Login</router-link></li>
				<li v-if="!isLogged">
					<hr class="dropdown-divider">
				</li>
				<li><router-link id="signup" class="elements" to="/signup">Signup</router-link></li>
			</ul>
		</li>
		<li class="nav-item dropdown-combined justify-content-end dropdown d-flex" v-if="isLogged">
			<a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
				<img :src="profile" alt="Profile" class="profile" width="35">
			</a>
			<ul class="dropdown-menu">
				<li><router-link id="profile" class="elements"
						:to="{ name: 'user', params: { username: $store.state.user.username } }">Go to Profile</router-link>
				</li>
				<li style="margin-top:5%"><router-link id="profile" class="elements"
						:to="{ name: 'edit_user', params: { what: 0 } }">Edit Profile</router-link></li>
				<!-- <li style="margin-top:5%"><router-link id="profile" class="elements"
						:to="{ name: 'edit_user', params: { what: 1 } }">Change Password</router-link></li> -->
				<li v-if="isLogged">
					<hr class="dropdown-divider">
				</li>
				<li><router-link id="logout" class="elements" to="/logout">Logout</router-link></li>
			</ul>
		</li>
	</nav>
	<router-view />
</template>

<script>
import SearchUser from './components/SearchUser.vue';

export default {
	name: 'App',
	data() {
		return {
			msg: 'Welcome to Your Vue.js App'
		}
	},
	components: {
		SearchUser
	},
	methods: {
	},
	computed: {
		isLogged() {
			return this.$store.state.isLogged;
		},
		profile() {
			const image_url = this.$store.state.url + "/image/" + "account.png";
			return image_url;
		},
		upload_icon() {
			const image_url = this.$store.state.url + "/image/" + "upload.png";
			return image_url;
		},
	},
	created() {
		if (localStorage.getItem('isLogged')) {
			this.$store.dispatch('refresh');
		}
	},
}
</script>

<style scoped>
#app {
	font-family: "Montserrat", sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	/* text-align: center; */
	color: #2c3e50;
}

h1,
h2,
h3 {
	font-weight: normal;
	font-family: "Montserrat";
}

nav {
	padding: 0.5% 2%;
	background-color: #87CEEB;
}

nav a {
	font-weight: bold;
	color: #2c3e50;
}

nav a.router-link-exact-active {
	color: #FF7F50;
}

.elements {
	margin: 0 10px;
	text-decoration: none;
}

.dropdown:hover>.dropdown-menu {
	margin-top: 20px;
	display: block;
	animation: dropdown-animation 0.3s ease;
}

@keyframes dropdown-animation {
	0% {
		opacity: 0;
	}

	100% {
		opacity: 1;
	}
}

.dropdown-combined {
	border-radius: 5;
	padding: 0.2%;
}

.dropdown-combined .dropdown-toggle::after {
	display: none;
}

.dropdown-menu {
	width: 200px;
}

</style>
