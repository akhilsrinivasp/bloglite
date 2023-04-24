<template>
    <div class="signup">
        <h1>Sign Up</h1>
        <form @submit.prevent="signup">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" placeholder="alexus">
            </div>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="name" class="form-control" id="name" v-model="name" placeholder="Alex U S">
            </div>
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" v-model="email" placeholder="alex@bloglite.com">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="shh secret!">
            </div>
            <div class="form-group">
                <label for="image">Profile Picture</label>
                <input type="file" class="form-control" ref = "fileInput" id="image" @change="handleFileUpload">
            </div>
            <button type="submit" class="btn btn-primary" @click="handleSubmit">Submit</button>
            <!-- error from the server -->
            <div class="invalid-feedback">
                <p v-if="error">{{ error }}</p>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'SignupComp',
        data() {
            return {
                username: '',
                name: '',
                email: '',
                image: 'noimage',
                password: '',
                error: '',
                file: null,
            }
        },
        computed() {
            return {
                
            }
        },
        methods: {
            validateName() {
                if (this.name.length < 1) {
                    this.error = 'Please enter your name';
                    alert(this.error);
                    return false;
                }
                return true;
            },
            validateUsername() {
                if (this.username.length < 1) {
                    this.error = 'Please enter a username';
                    alert(this.error);
                    return false;
                }
                return true;
            },
            validateEmail() {
                if (this.email.length < 1) {
                    this.error = 'Please enter an email';
                    alert(this.error);
                    return false;
                }
                return true;
            },
            validatePassword() {
                if (this.password.length < 1) {
                    this.error = 'Please enter a password';
                    alert(this.error);
                    return false;
                }
                return true;
            },
            validateData() {
                if (!this.validateName() || !this.validateUsername() || !this.validateEmail() || !this.validatePassword()) {
                    return false;
                }
                return true;
            },
            handleFileUpload() {
                this.file = this.$refs.fileInput.files[0];
            },
            handleSubmit() {
                if (!this.validateData()) {
                    return;
                }
                const formData = new FormData();
                formData.append('image', this.file);
                formData.append('username', this.username);
                formData.append('email', this.email);
                formData.append('password', this.password);
                formData.append('name', this.name);
                
                fetch(this.$store.state.url + 'register', {
                    method: 'POST',
                    body: formData
                }
                ).then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.error(error);
                });
            },
        }
    }
</script>

<style scoped>
    .signup {
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
    /* .invalid-feedback {
        font-family: "Montserrat", sans-serif;
        font-size: 15px;
        color: red;
        margin: 1%;
        margin-top: 10px;
    } */
</style>