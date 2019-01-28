<template>
    <div class="container">
        <template v-if="error.statusCode === 404">
            <div class="error-page">
                <img src="~/assets/images/icons/icon-error.svg" alt=""/>
                <h1>Page not found</h1>
                <nuxt-link class="error-link" to="/">Go back to home page</nuxt-link>
            </div>
        </template>
        <template v-else>
            <div class="error-page">
                <img src="~/assets/images/icons/icon-error.svg" alt=""/>
                <h1>An error occurred</h1>
                <p>{{message}}</p>
            </div>
        </template>
    </div>
</template>

<script>
export default {
    props: {
        error: {
            type: Object
        }
    },
    computed: {
        statusCode() {
            return (this.error && this.error.statusCode) || 500
        },
        message() {
            return this.error.message || '<%= messages.client_error %>'
        }
    }
}
</script>
