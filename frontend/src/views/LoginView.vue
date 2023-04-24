<template> 
    <div class="auth" align = center>
        <LoginComp />
    </div>
</template>

<script>
    import LoginComp from '@/components/LoginComp.vue'
    export default {
        name: 'LoginView', 
        components: {
            LoginComp
        }
    }
</script>

<style scoped>
</style>