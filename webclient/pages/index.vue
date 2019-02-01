<template>
    <div>
        <b-jumbotron header="Test Task Ariana" lead="Simple questionnaire system">
            <p>Select one of <nuxt-link :to="{name: 'questionnaires'}">questionnaire</nuxt-link> to get started</p>
        </b-jumbotron>
    </div>
</template>
<script>
import {waitFor} from 'vue-wait'

export default {
}
</script>
