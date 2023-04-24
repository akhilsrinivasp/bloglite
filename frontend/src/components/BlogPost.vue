<template>
    <div class = 'post'>
        <div class = "header"> 
            <h1 class = "title">{{ blog.title }}</h1>
            <!-- <p class = "author">{{ blog.author }}</p> -->
            <!-- link to redirect to UserView -->
            <router-link class = "author" :to="{name: 'user', params: {username: blog.author}}">{{ blog.author }}</router-link>
        </div>
        <div @click="() => $router.push(`/blog/${blog.id}`)">
            <img class = "image-post" :src="image_url" alt="Blog Image">
             <div class="footer">
                <p class = "date">{{ date_formatted }}</p>
                <p class = "content">{{ blog.content }}</p>
             </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'BlogPost',
        props: {
            blog: Object
        },
        computed : {
            image_url() {
                const image_url = this.$store.state.url + "/image/" + this.blog.image;
                return image_url;
            }, 
            date_formatted() {
                const date = new Date(this.blog.created_at);
                // if it's the previous day, return "Yesterday at " + date.toLocaleTimeString("en-US");
                if (date.getDate() == new Date().getDate() - 1) {
                    return "Yesterday at " + date.toLocaleTimeString("en-US");
                }
                if (date.getDate() == new Date().getDate()) {
                    return "Today at " + date.toLocaleTimeString("en-US");
                }
                // else format the date to "March 21, 2023 at 12:00 AM"
                const date_formatted = date.toLocaleDateString("en-US", {month: "long", day: "numeric", year: "numeric"}) + " at " + date.toLocaleTimeString("en-US", {hour: "numeric", minute: "numeric"});
                return date_formatted;
            }
        }
    }
</script>

<style scoped>
    /* .post {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    } */

    @media (max-width: 768px) {
        .header {
            align-items: center;
            margin-bottom: 2%;
            display: none;
        }
        .title {
            font-family: "Montserrat", sans-serif;
            font-weight: bold;
            font-size: 30px;
            color: #87CEEB;
            margin: 1%;
        }
    }
    .header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2%;
    }

    .header > div {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    
    .title {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 40px;
        color: #87CEEB;
        margin: 1%;
    }
    .author {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
        color: #2c3e50;
        margin: 1%;
        text-decoration: none;
    }

    .image-post {
        width:90%;
        height: 90%;
        object-fit: cover;
        margin: 2%;
        border-radius: 10px;
    }
    
    .footer {
        /* display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center; */
        margin-top: 2%;
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
        text-overflow: ellipsis;
        justify-content: left;
    }
</style>
