<template>
    <div class = "home">
        <div class="header">
            <h1>A Photo Blogging Platform</h1>
            <p>Bloglite is a simple blog application that allows users to create, edit, and delete blog posts.</p>
            <p>Bloglite is built with Vue.js and Flask.</p>
        </div>
        <!-- For loop through blogs using v-for -->
        <div class = "blog-grid">
            <div class = "blog-posts" v-for="blog in $store.state.blogs" :key="blog.id">
                <BlogPost :blog="blog"/>
            </div>
        </div>

    </div>
</template>

<script>
    import BlogPost from '../components/BlogPost.vue'

    export default {
        name: 'HomeView',
        components: {
            BlogPost,
        },
        created() {
            this.$store.dispatch('getBlogs')
        }
    }
</script>

<style scoped>
    .header {
        margin: 5%;
        margin-bottom: 2%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    }

    h1 {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 50px;
        color: #87CEEB;
    }
    p {
        font-family: "Montserrat", sans-serif;
        font-size: 20px;
        color: #2c3e50;
    }

    .blog-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(600px, 1fr));
        grid-gap: 1rem;
        margin: 5%;
        margin-top: 0;
    }

    .blog-posts {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    }
    
    @media screen and (max-width: 768px) {
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            grid-gap: 1rem;
            margin: 5%;
        }
    }
</style>