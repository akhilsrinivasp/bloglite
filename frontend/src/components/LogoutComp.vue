<template>
    <div class="logout">
    </div>
</template>

<script>
    export default {
        name: 'LogoutComp',
        methods: {
            logout() {
                this.$store.dispatch('logout');
                this.$router.push('/');
            },
        },
        created() {
            this.logout();
        },
        beforeUnmount() {
            location.reload();
        },
    }
</script>