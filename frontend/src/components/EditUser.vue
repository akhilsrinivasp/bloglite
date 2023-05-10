<template>
    <div class="edit-user-comp">
        <div class="left-pane">
            <span id="edit-profile" @click="edit_profile = true;">
                Edit Profile
            </span>
            <span id="change-password" @click="edit_profile = false;">
                Change Password
            </span>
        </div>
        <div class="right-pane">
            <form @submit.prevent="editUserProfile" v-if="edit_profile" style="margin-top: 4%;">
                <h3 style="margin-bottom: 40px;">User Profile</h3>
                <div class="form-group">
                    <label for="title">Username</label>
                    <input type="text" class="form-control" id="title" v-model="edited.username">
                </div>
                <div class="form-group">
                    <label for="content">Name</label>
                    <input type="text" class="form-control" id="content" v-model="edited.name">
                </div>
                <div class="form-group">
                    <label for="image">Profile Pic</label>
                    <span style="display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
                        <img :src="profile_pic" alt="profile pic"
                            style="width: 100px; height: 100px; border-radius: 50%; margin: 1%;">
                        <input type="file" class="form-control" id="image" ref="fileInput" @change="handleFileUpload">
                    </span>
                </div>
                <button type="submit" class="btn btn-primary">Update</button>
            </form>

            <form @submit.prevent="changePassword" v-if="!edit_profile" style="margin-top: 4%;" id = "change-password">
                <h3 style="margin-bottom: 40px;">User Profile</h3>
                <div class="form-group">
                    <label for="oldpwd">Old Password</label>
                    <input type="password" class="form-control" id="oldpwd" v-model="old_password">
                </div>
                <div class="form-group">
                    <label for="newpwd">New Password</label>
                    <input type="password" class="form-control" id="newpwd" v-model="new_password">
                </div>
                <div class="form-group">
                    <label for="cnfmpwd">Confirm New Password</label>
                    <input type="password" class="form-control" id="cnfmpwd" v-model="confirm_password">
                </div>
                <button type="submit" class="btn btn-primary">Change</button>
            </form>
        </div>
    </div>
</template>

<script>

export default {
    'name': 'EditUser',
    data() {
        return {
            user: null,
            edited: null,
            error: '',
            edit_profile: true,
            image_was_changed: false,
            old_password: '',
            new_password: '',
            confirm_password: '',
        }
    },
    computed: {
        profile_pic() {
            return this.$store.state.url + 'image/' + this.edited.image;
        }
    },
    methods: {
        loadUser() {
            if (this.$store.state.user) {
                this.user = JSON.parse(JSON.stringify(this.$store.state.user));
                this.edited = JSON.parse(JSON.stringify(this.$store.state.user));
            }
        },
        validateProfileData() {
            if (this.user.username === this.edited.username && this.user.name === this.edited.name && !this.image_was_changed) {
                this.error = 'No changes made';
                // delay 
                setTimeout(() => {
                    this.error = '';
                }, 3000);
                this.error = '';
                return false;
            }
        },
        handleFileUpload() {
            this.edited.image = this.$refs.fileInput.files[0];
        },
        imageChanged() {
            this.edited.image = this.$store.dispatch('uploadImage', this.edited.image);
            this.image_was_changed = true;
        },
        editUserProfile() {
            this.validateProfileData();
            const data = {
                username: this.edited.username,
                name: this.edited.name,
                image: this.edited.image,
            }
            fetch(this.$store.state.url + 'user', {
                method: 'PUT',
                body: JSON.stringify(data),
                headers: {
                    'Authorization': 'Bearer ' + this.$store.state.access_token,
                    'Content-Type': 'application/json',
                }
            })
                .then(res => res.json())
                .then(data => {
                    if (this.edited.username !== this.user.username) {
                        this.$router.push('/logout');
                        alert("You have changed yout username. Please login again.")
                    }
                    else alert("Profile updated successfully");
                    this.error = data.message;
                })
            
        },
        changePassword() {
            if(this.new_password !== this.confirm_password) {
                this.error = 'Passwords do not match';
                alert('Passwords do not match');
                // delay 
                setTimeout(() => {
                    this.error = '';
                }, 3000);
                return;
            }
            const data = {
                old_password: this.old_password,
                new_password: this.new_password,
            }
            fetch(this.$store.state.url +"password/reset", {
                method: 'PUT',
                body: JSON.stringify(data),
                headers: {
                    "Authorization": "Bearer " + this.$store.state.access_token,
                    "Content-Type": "application/json",
                }
            })
                .then(res => res.json())
                .then(data => {
                    // get form and add child with data's message 
                    alert(data.message);
                })
                .catch(err => {
                    this.error = err.response.data.message;
                    console.log(err);
                });
            this.old_password = '';
            this.new_password = '';
            this.confirm_password = '';
        }
    },
    created() {
        this.loadUser();
    },
    mounted() {
        // on change of image call validate data
        this.$refs.fileInput.addEventListener('change', this.imageChanged);
    }
}
</script>

<style scoped>
.error_message {
    color: red;
    font-size: 1.2em;
    font-weight: 700;
    margin: 2%;
}

.edit-user-comp {
    margin: 3% 7%;
    /* padding: 3%; */
    /* margin-top: 4%; */
    text-decoration: none;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
    border-radius: 10px;
    background-color: #fff;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.left-pane {
    background-color: #f1f1f1;
    display: flex;
    flex-direction: column;

    font-family: "Montserrat", sans-serif;
    font-weight: 700;
    color: #2c3e50;
    height: 700px;
    border-radius: 10px 0 0 10px;
}

.left-pane span {
    margin-bottom: 10px;
    padding: 20%;
    cursor: pointer;
}

.left-pane span:hover {
    background-color: #ff9c78
}

.right-pane {
    flex-grow: 1;
    padding: 0 5%;
    padding-left: 5%;
    margin-top: 0;
    width: 50%;
    font-family: 'Montserrat';
    height: 700px;
    background-color: #f7f7f7;
    border-radius: 0 10px 10px 0;
}

.right-pane form {
    margin-top: 5%;
}

.right-pane form .form-group {
    margin-bottom: 5%;
}

.right-pane form .form-group label {
    display: block;
    margin-bottom: 1%;
}

.right-pane form .form-group input {
    width: 100%;
}

.right-pane form .form-group textarea {
    width: 100%;
    height: 100px;
}

.right-pane form .form-group button {
    width: 100%;
}

form {
    margin-top: 0;
}
</style>