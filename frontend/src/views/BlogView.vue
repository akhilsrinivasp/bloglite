<template>
    <div class="view-blog" align="center">
        <div class="blog" v-if="!edit">
            <div class="header">
                <h1 class="title">{{ blog.title }}</h1>
                <router-link class="author" :to="{ name: 'user', params: { username: blog.author } }">{{ blog.author }}</router-link>
            </div>
            <img class="image-post" :src="image_url" alt="Blog Image">
            <div class="footer">
                <p class="date">{{ date_formatted }}</p>
                <p class="content">{{ blog.content }}</p>
            </div>
            <div class="blog-buttons" v-if="blog.author == $store.state.user.username">
                <button class="btn btn-primary btn-edit" @click="edit = !edit">Edit</button>
                <button class="btn btn-danger btn-delete" @click="confirmDelete()">Delete</button>
            </div>
            <div class="error">
                {{ error }}
            </div>
        </div>
        
        <div class="edit" v-if="edit">
            <div class="header">
                <h1 class="title"><input type="text" v-model="blog.title" placeholder="Title"></h1>
                
            </div>
            <img class="image-post" :src="image_url" alt="Blog Image">
            <div class="footer">
                <p class="date">{{ date_formatted }}</p>
                <p class="content"><input type="text" v-model="blog.content" placeholder="Content"></p>
            </div>
            <div class="blog-buttons" v-if="blog.author == $store.state.user.username">
                <button class="btn btn-secondary btn-cancel" @click="edit = !edit">Cancel</button>
                <button class="btn btn-success btn-edit" @click="updateBlog()">Save</button>
            </div>
            </div>
    </div>
</template>

<script>
export default {
    name: 'ViewBlog',
    components: {
    },
    data() {
        return {
            blog: null,
            error: '',
            edit: false,
        }
    },
    methods: {
        async loadBlog() {
            await fetch(this.$store.state.url + 'blog/' + this.$route.params.id, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => response.json())
                .then(data => {
                    this.blog = data;
                })
                .catch(error => {
                    this.error = error;
                })
        },
        confirmDelete() {
            const data = {
                id: this.blog.id
            }
            if (confirm('Are you sure you want to delete this blog?')) {
                fetch(this.$store.state.url + 'blog', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": "Bearer " + this.$store.state.access_token,
                    },
                    body: JSON.stringify(data)
                })
                this.$router.push(`/user/${this.$store.state.user.username}`)
            }
        },
        updateBlog() {
            this.edit = !this.edit;
            const data = {
                id: this.blog.id,
                title: this.blog.title,
                content: this.blog.content,
            }
            fetch(this.$store.state.url + 'blog', {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + this.$store.state.access_token,
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => {
                    this.blog = data;
                    this.loadBlog();
                })
                .catch(error => {
                    this.error = error;
                })
        },
    },
    computed: {
        image_url() {
            const image_url = this.$store.state.url + "/image/" + this.blog.image;
            return image_url;
        },
        date_formatted() {
            const date = new Date(this.blog.created_at);
            const date_formatted = date.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" }) + " at " + date.toLocaleTimeString("en-US", { hour: "numeric", minute: "numeric", timeZone: "Asia/Kolkata"});
            return date_formatted;
        }
    },
    created() {
        this.loadBlog()
    },
}
</script>

<style scoped>
.view-blog {
    margin: 0 auto;
    padding: 5%;
    margin-top: 4%;
    text-decoration: none;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    border-radius: 6px;
    background-color: #fff;
    width: 60%;
    position: relative;
}

.header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2%;
}

.title {
    font-family: "Montserrat", sans-serif;
    font-weight: bold;
    font-size: 45px;
    color: #87CEEB;
    margin: 1%;
}

.author {
    font-family: "Montserrat", sans-serif;
    font-weight: bold;
    font-size: 30px;
    color: #2c3e50;
    margin: 1%;
    text-decoration: none;
}

.image-post {
    width: 90%;
    height: 90%;
    object-fit: cover;
    margin: 2%;
    border-radius: 10px;
    align-items: center;
    justify-content: center;
}
.date {
    font-family: "Montserrat", sans-serif;
    font-weight: bold;
    font-size: 20px;
    color: #2c3e50;
}

.content {
    font-family: "Montserrat", sans-serif;
    font-size: 20px;
    color: #2c3e50;
    margin-top: 2%;
}

.blog-buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 2%;
}

.blog-buttons button {
    font-family: "Montserrat", sans-serif;
    font-size: 20px;
    color: #fff;
    border-radius: 4px;
    padding: 10px 20px;
    cursor: pointer;
}

.blog-buttons button.btn-edit {
    background-color: #3498db;
    border: 2px solid #3498db;
    margin-right: 10px;
}

.blog-buttons button.btn-delete {
    background-color: #e74c3c;
    border: 2px solid #e74c3c;
}

.blog-buttons button:hover {
    opacity: 0.8;
}
.edit-comp {
    margin: 0 auto;
    padding: 5%;
    margin-top: 4%;
    text-decoration: none;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    border-radius: 6px;
    background-color: #fff;
    width: 60%;
    position: relative;
}

input {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

</style>