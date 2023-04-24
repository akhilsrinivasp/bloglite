<template>
    <div class="login">
        <h1>Login</h1>
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required placeholder="shriramg">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required placeholder="again! shh secret">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            <div class="invalid-feedback">
                <p v-if="error">{{ error }}</p>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'LoginComp',
        data() {
            return {
                username: '',
                password: '',
                error: '',
            }
        },
        methods: {
            validateData() {
                if (this.username.length < 1 || this.password.length < 1) {
                    this.error = 'Please fill in all the fields';
                    alert(this.error);
                    return false;
                }
                return true;
            },
            handleSubmit() {
                if (!this.validateData()) {
                    return;
                }
                this.$store.dispatch('login', {
                    username: this.username,
                    password: this.password,
                }).then(() => {
                    this.$router.push('/');
                }).catch((err) => {
                    this.error = err.response.data.message;
                });
            },
        },
        created() {
            if (this.$store.state.isLogged) {
                this.$router.push('/');
            }
        },
    }
</script>

<style scoped>
    .login {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        width:50%;
    }
    h1 {
        font-family: "Montserrat", sans-serif;
        font-size: 40px;
        color: #87CEEB;
        margin: 1%;
        margin-left: 0;
        font-weight: bold;
    }
    input {
        margin-bottom: 10px;
        margin-top: 10px;
        font-family: "Montserrat", sans-serif;
        font-size: 15px;
        color: #2c3e50;
        margin: 1%;
    }
    label {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
        color: #2c3e50;
        margin: 1%;
    }
    button {
        font-family: "Montserrat", sans-serif;
        font-size: 20px;
        margin: 1%;
        margin-top: 10px;
        padding : 1% 5%;
    }
    
</style>