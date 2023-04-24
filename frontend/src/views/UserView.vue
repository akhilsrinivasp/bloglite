<template>
    <div class="user">
        <div class="header">
            <div class="profile-pic">
                <img class="dp-image" :src="profile_pic_url" alt="Profile Picture">
            </div>
            <div class="user-details">
                <h1 class="author">{{ user.username }}</h1>
                <p class="date">Joined: {{ date_formatted }}</p>
            </div>
            <div class="follow-user" v-if="is_same_user == false">
                <button class="follow-button" v-if="!is_following" @click="follow_user">Follow</button>
                <button class="unfollow-button" v-else @click="unfollow_user">Unfollow</button>
            </div>
            <div class="edit-user" v-if="is_same_user == true">
                <button class="edit-button" @click="edit_user">Edit Profile</button>
            </div>
            <div class="edit-user-container" v-if="show_edit_user == true">
                <EditUser :user="user"/>
            </div>
        </div>
        
        <div class="details">
            <div class="name">
                <h3 class="public-user-name">{{ user.name }}</h3>
            </div>
            <div class="followers">
                <p class="follower-count">{{ follower_count }}</p>
                <p style = "font-size: 18px; padding-top: 1%;" class="follower-text">Followers</p>
            </div>
            <div class="following">
                <p class="following-count">{{ following_count }}</p>
                <p style = "font-size: 18px; padding-top: 1%;" class="following-text">Following</p>
            </div>
        </div>
        <div class = "blog-grid">
            <div class = "blog-posts" v-for="blog in blogs" :key="blog.id">
                <BlogPost :blog="blog"/>
            </div>
        </div>
    </div>
</template>

<script>
    import BlogPost from '../components/BlogPost.vue'
    import EditUser from '../components/EditUser.vue'

    export default {
        name: 'UserView',
        components: {
            BlogPost,
            EditUser
        },
        data() {
            return {
                user: null,
                blogs: null,
                followers: null,
                following: null,
                follower_count: null,
                following_count: null,
                is_following: false,
                show_edit_user: false,
            }
        },
        computed: {
            username() {
                return this.$route.params.username;
            },
            date_formatted() {
                const date = new Date(this.user.created_at);
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
            },
            profile_pic_url() {
                const profile_pic_url = this.$store.state.url + "/image/" + this.user.image;
                return profile_pic_url;
            },
            is_same_user() {
                if(!this.$store.state.isLogged) return false;
                return this.$store.state.user.username == this.username
            }
        },
        methods: {
            getUser() {
                fetch(this.$store.state.url + "/user/" + this.username)
                .then(response => response.json())
                .then(data => {
                    this.user = data.user;
                    this.blogs = data.blogs;
                    this.followers = data.followers;
                    this.following = data.follows;
                    this.follower_count = data.followers_count;
                    this.following_count = data.follow_count;
                })
                .catch(error => {
                    console.log(error);
                })
            },
            follow_user() {
                if(!this.$store.state.isLogged) {
                    alert("Login to follow user");
                    this.$router.push("/login");
                    return;
                }
                // access API with json data with username (following tag)
                //api end point is /follow
                const data = {
                    "following": this.username
                }
                fetch(this.$store.state.url + 'follow',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + this.$store.state.access_token 
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    if(data.status == 200) {
                        console.log("Followed");
                    }
                    this.getUser();
                    this.is_following = true;
                })
                .catch(error => {
                    console.log(error);
                })
            }, 
            unfollow_user() {
                const data = {
                    "following": this.username
                }
                fetch(this.$store.state.url + 'unfollow',
                {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + this.$store.state.access_token 
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    if(data.status == 200) {
                        console.log("Unfollowed");
                    }
                    this.getUser();
                    this.is_following = false;
                })
                .catch(error => {
                    console.log(error);
                })
            },
            edit_user() {
                this.show_edit_user = true;
            },
        },
        created() {
            this.getUser();
            this.is_following = false;
        },
        mounted() {
            if(this.followers == null) {
                this.is_following = false;
                return;
            }
            if(this.$store.state.isLogged){
                for(let i = 0; i < this.followers.length; i++) {
                    if(this.followers[i].username == this.$store.state.username) {
                        this.is_following = true;
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .header {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        margin-bottom: 3%;

        /* display: flex; */
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        /* margin-bottom: 2%; */
    }
    .header > div {
        display: flex;
        flex-direction: column;
    }
    .dp-image {
        width: 130px;
        height: 130px;
        border-radius: 100%;
    }
    .user-details {
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
        color: #2c3e50;
        margin: 2% 5% 0%;
        align-items: center;
        /* text-decoration: none; */
    }
    .follow-user {
        margin-left: 2%;
    }
    .follow-button {
        background-color: #87CEEB;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .unfollow-button {
        /* background-color: #87CEEB; */
        border-color: #2196F3;
        border: 4px;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .follow-button:hover {
        background-color: #2196F3;
    }
    .unfollow-button:hover {
        background-color: #2c3e50
    }
    .details {
        margin: 1% 5%;
        padding: 3% 10%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2%;
    }
    .followers {
        display: flex;
        flex-direction: column;
        align-items: center;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .followers > p {
        margin: 0;
    }
    .following{
        display: flex;
        flex-direction: column;
        align-items: center;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .following > p {
        margin: 0;
    }
    .public-user-name{
        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 25px;
        margin: 0;
    }
    .blog-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(600px, 1fr));
        grid-gap: 1rem;
        margin: 5%;
        margin-top: 2%;
    }
    .blog-posts {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
    }
    .edit-button {
        background-color: #2c3e50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;

        font-family: "Montserrat", sans-serif;
        font-weight: bold;
        font-size: 20px;
    }
    .edit-button:hover {
        background-color: #2196F3;
    }

    .edit-button:active {
        background-color: #2c3e50;
    }

    .edit-user-container {
        margin: 5%;
        padding: 5%;
        text-decoration: none;
        box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
        border-radius: 6px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2%;

        z-index: -1;
        position: absolute;
    }
</style>