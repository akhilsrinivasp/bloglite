<template>
    <div class="upload-blog">
        <form @submit.prevent="uploadBlog">
            <h3 style="margin-bottom: 40px;">Upload</h3>
            <div class="form-group">
                <label for="title">Title</label>
                <input type="text" class="form-control" id="title" v-model="title">
            </div>
            <div class="form-group">
                <label for="content">Content</label>
                <textarea class="form-control" id="content" v-model="content"></textarea>
            </div>
            <div class="form-group">
                <label for="image">Image</label>
                <input type="file" class="form-control" id="image" ref="fileInput" @change="handleFileUpload">
            </div> 
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>
    export default {
        name: 'UploadBlog',
        data() {
            return {
                title: '',
                content: '',
                file: null,
            }
        },
        methods: {
            handleFileUpload() {
                this.file = this.$refs.fileInput.files[0];
            },
            uploadBlog() {
                const formData = new FormData();
                formData.append('title', this.title);
                formData.append('content', this.content);
                formData.append('image', this.file);
                fetch(this.$store.state.url + 'blog', {
                    method: 'POST',
                    headers: {
                        "Authorization": "Bearer " + this.$store.state.access_token,
                    },
                    body: formData,
                },
                ).then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.$router.push(`/user/${this.$store.state.user.username}`)
                })
                .catch(error => {
                    console.error(error);
                });
            },
        },
    }
</script>

<style>
    .upload-blog {
        margin: 0 auto;
        width: 50%; 
        font-family: 'Montserrat'; 
    }
    
    .upload-blog form {
        margin-top: 5%;
    }

    .upload-blog form .form-group {
        margin-bottom: 5%;
    }
    
    .upload-blog form .form-group label {
        display: block;
        margin-bottom: 1%;
    }
    
    .upload-blog form .form-group input {
        width: 100%;
    }
    
    .upload-blog form .form-group textarea {
        width: 100%;
        height: 100px;
    }
    
    .upload-blog form .form-group button {
        width: 100%;
    }
     
    
</style>