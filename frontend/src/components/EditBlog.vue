<template>
    <div class="edit-blog">
        <div class="header">
            <h1 class="title">Edit Blog</h1>
        </div>
        <div class="form">
            <div class="error">
                {{ error }}
            </div>
            <div class="input">
                <label for="title">Title</label>
                <input type="text" id="title" v-model="title" />
            </div>
            <div class="input">
                <label for="content">Content</label>
                <textarea id="content" v-model="content"></textarea>
            </div>
            <img src="image_url" alt="image">
            <div class="input">
                <button @click="editBlog">Edit Blog</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'EditBlog',
        props: ['blog'],
        data() {
            return {
                title: '',
                content: '',
                image: '',
                error: '',
                file: null,
            }
        },
    }
</script>

<style scoped>
    .edit-blog {
        width: 60%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);
    }
</style>